import re
import sklearn
from flask import Flask, render_template, request 
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
import string
from sklearn.model_selection import train_test_split
import tensorflow as tf 
import webscraper

app = Flask(__name__, template_folder='Templates')
loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
loaded_model2 = pickle.load(open('SVC_test_model.sav', 'rb'))

stop_word = stopwords.words('english')
stm = nltk.SnowballStemmer("english")


file = open("moderate_list.txt", "r")
moderate_lists = file.read()
mod_lists = moderate_lists.split(",")
mod_list_modified=[]
for word in mod_lists:
    mod_list_modified.append(word.lstrip())

def addStrick(user_input = ""):
    modified_sentence = ""
    for text in user_input.split():
        if text.lower() in mod_list_modified:
            modified_sentence += text[:1] + '*' * (len(text)-1) + ' ' 
        else:
            modified_sentence += text + ' '            
    return modified_sentence


def text_cleaner(input_text):
    input_text = re.sub(r'@[A-Za-z0-9_]+','',str(input_text))    # Removing @mentions
    input_text = re.sub(r'#','',str(input_text))                 # Removing #tag symbol
    input_text = re.sub(r'RT[\s]+',' ',input_text)          # Remvoing RT
    input_text = re.sub(r'\n','',input_text) 
    input_text = re.sub(r',','',input_text) 
    input_text = re.sub(r'.[.]+','',input_text) 
    input_text = re.sub(r'\w+:\/\/\S+','',input_text) 
    input_text = re.sub(r'https?:\/\/\S+','',input_text)    # Removing hyperlinks
    input_text = re.sub(r'/',' ',input_text)
    input_text = re.sub(r'-',' ',input_text)
    input_text = re.sub(r'_',' ',input_text)
    input_text = re.sub(r'!','',input_text)
    input_text = re.sub(r':',' ',input_text)
    input_text = re.sub(r'$','',input_text)
    input_text = re.sub(r'%','',input_text)
    input_text = re.sub(r'^','',input_text)
    input_text = re.sub(r'&','',input_text)
    input_text = re.sub(r'=',' ',input_text)
    input_text = re.sub(r' +',' ',input_text) 
    input_text = re.sub('\[.*?\]', '', input_text)
    input_text = re.sub('https?://\S+|www\.\S+', '', input_text)
    input_text = re.sub('<.*?>+', '', input_text)
    input_text = re.sub('[%s]' % re.escape(string.punctuation), '', input_text)
    input_text = re.sub('\n', '', input_text)
    input_text = re.sub('[0-9]+', '', input_text) # removing numbers
    input_text = str(input_text).lower() # converting to lowercase 
    input_text = str(input_text).strip()  # Removing all the leading and trailing whitespaces present in the input data 
    input_text = [word for word in input_text.split(' ') if word not in stop_word]
    input_text=" ".join(input_text)
    input_text = [stm.stem(word) for word in input_text.split(' ')]
    input_text=" ".join(input_text)
    return input_text

df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')
df_train.drop_duplicates(subset=['tweet'], keep='last', inplace=True)
df_train.reset_index(inplace=True)
df_offensive =pd.read_csv("labeled_data.csv")
df_offensive["class"].replace({0: 1}, inplace=True)
df_offensive["class"].replace({2: 0}, inplace=True)
df_offensive.drop(['Unnamed: 0','count','hate_speech','offensive_language','neither'],axis=1,inplace=True)
df_offensive.rename(columns ={'class':'label'}, inplace = True)
df_train_final = pd.concat([df_train,df_offensive])
df_train_final.drop(['id'],axis=1,inplace=True)
df_train_final['tweet']=df_train_final['tweet'].apply(text_cleaner)
X = df_train_final['tweet'].astype(str)  # Converting to string, because vectorizer does'nt accept list.
y = df_train_final['label'].astype(str)  # Converting to string, because vectorizer does'nt accept list.
X_train, X_test, y_train, y_test =  train_test_split(X, y, train_size = 0.8, random_state = 3) 

from sklearn.feature_extraction.text import TfidfVectorizer
# Extracting features using TF-IDF (1,2) - unigrams and bigrams
vectoriser = TfidfVectorizer(ngram_range=(1,2), max_features=500000)
vectoriser.fit(X_train)
X_test= vectoriser.transform(X_test)
accuracy = loaded_model.score(X_test, y_test) * 100

@app.route('/')
def index():
    return render_template('index.html', data='')

@app.route('/moderate', methods=['GET', 'POST'])
def predict():
    moderation_type = request.form.get('moderation_type') #web,text
    user_input = request.form.get('user_input')
    if (moderation_type=="web"):
        Webscrappedtext= webscraper.scrape_page_text(user_input)
        clean_user_input= [text_cleaner(Webscrappedtext)]
        updated_text= addStrick(clean_user_input)
        test_vect = vectoriser.transform(clean_user_input)
        pred = loaded_model.predict(test_vect)
        print(pred)
        if (pred == '1'):
            flag = "This page is not safe for children"
        else:
            flag = "This page is safe for children"
    
    else :
        updated_text = addStrick(user_input)
        clean_user_input= [text_cleaner(user_input)]
        test_vect = vectoriser.transform(clean_user_input)
        pred = loaded_model.predict(test_vect)
        print(pred)
        if (pred == '1'):
            flag = "This comment is not safe for children"
        else:
            flag = "This comment is safe for children"

    
    output = {
        "type": moderation_type,
        "text": user_input,
        "Flag": flag,
        "accuracy": accuracy,
        "updated_text": updated_text
          }
    return render_template('index.html', data=output)

if __name__ == '__main__':
    app.run(debug=True)