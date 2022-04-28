from flask import Flask, render_template, request

app = Flask(__name__, template_folder='Templates')

@app.route('/')
def index():
    return render_template('index.html', data='')

@app.route('/moderate', methods=['GET', 'POST'])
def predict():
    moderation_type = request.form.get('moderation_type') #web,text
    user_input = request.form.get('user_input')

#     call model method
    abuseWord = "shit"
    strick = '*' * len(abuseWord)
    updated_text = user_input.replace(abuseWord, strick)
    output = {
        "type": moderation_type,
        "text": user_input,
        "isAbusive": "true",
        "abuseWord" : abuseWord,
        "accuracy": "95.7",
        "updated_text": updated_text
          }
    return render_template('index.html', data=output)

if __name__ == '__main__':
    app.run(debug=True)