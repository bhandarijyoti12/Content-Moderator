## Content Moderation : 

This project is done as the requirement for the first semster of the master's program for the course Intro to Artificial Intelligence. We have made  a platform  that allows for content filtering that detects and filters abusive and offensive contents which can be in text or audio format. We have used twitter Hate Speech and Offensive Language Dataset called labeled_data.csv and Twitter Sentiment Analysis data (train.csv and test.csv) from Kaggle to train our model. We have used Support Vector Classification (SVC) technique to make the model. Other algorithms such as MultinomialNB, LogisticRegression Algorithm, RandomForestClassifier and DecisionTreeClassifier were also used to train the data but we got the highest precision, accurcay, f1 score from SVC so we sticked to the Support Vector Classification (SVC) algorithm to make this system. 

### 1. Prerequisite
- Python
- Pip
- Jupyter notebook

Commands

    py -m pip --version

#### if not install pip
    py -m pip install --upgrade pip

### 2. Install and Activate Environment
    For Windows user : 
    py -m venv venv
    venv\Scripts\activate

    For Mac users: 
    python -m venv venv
    source venv/bin/activate

To deactivate the environment use
    
    deactivate

### 4. Install flask server to run the application
    pip install flask

### 5. Install required packages
    -sklearn 
    -pandas 
    -numpy 
    -webscraper 
    -tensorflow 
    -nltk 
    -sklearn 
    -selenium 
    -bs4 
    -pickle
    -pyaudio

Note: For the Mac users, follow the steps given below to install pyaudio: 
* First we need to install 'portaudio'

* Then we need to find out the path of portaudio in our laptop or pc
 sudo find / -name "portaudio.h"

* After we find the path of portaudio.h , we need to write down the following command format
  pip install --global-option='build_ext' --global-option='-I/opt/homebrew/Cellar/portaudio/19.7.0/include' --global-option='-  L/opt/homebrew/Cellar/portaudio/19.7.0/lib' pyaudio

* What you need to write
pip install --global-option='build_ext' --global-option='-I/------PATH-------' --global-option='-L/-------PATH---------' pyaudio

* I did : pip install --global-option='build_ext' --global-option='-I/opt/homebrew/Cellar/portaudio/19.7.0/include' --global-option='-L/opt/homebrew/Cellar/portaudio/19.7.0/lib' pyaudio

Note: Refer to app.py for more packages to be installed.

### Install python-dotenv for using enviroment (optional)
    pip install python-dotenv

#### Then set the Environment 
    set FLASK_APP=app.py

### 6. Run Application
    flask run

### 7. Access the project at
    http://127.0.0.1:5000/
    
    

Note: If you want to run the project via flask environment 


   
### 8.Presentation file for this project has been added as AI- Content_Moderation_Presentation.pptx. Please have a look at it for more details.

### 9. Future Enhancement :
    We tried to used the neural network to train our model but it was taking very long time to train the data. We could used neural network for the better results. 

   


