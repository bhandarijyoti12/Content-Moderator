## Content Moderation : 

This project is done as the requirement for the first semster of the master's program for the course Into to Artificial Intelligence. We have made  a platform  that allows for content filtering that detects and filters abusive and offensive contents which can be in text or audio format. We got twitter Hate Speech and Offensive Language Dataset called labeled_data.csv and Twitter Sentiment Analysis data (train.csv and test.csv) from Kaggle. 

### 1. Prerequisite
- Python
- Pip

Commands

    py -m pip --version

#### if not install pip
    py -m pip install --upgrade pip

### 2. Install and Activate Environment

    py -m venv venv
    venv\Scripts\activate

To deactivate the environment use
    
    deactivate

### 4. Install flask server to run the application
    pip install flask

### 5. Install required packages
    pip install sklearn 
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

### 6. Run Application
    flask run

### 7. Access the project at
    http://127.0.0.1:5000/

Note: If you want to run the project via flask environment 

### Install python-dotenv for using enviroment (optional)
    pip install python-dotenv

#### Then set the Environment 
    set FLASK_APP=app.py

## Deployment guide

    pip install gunicorn
    pip freeze > requirements.txt

## Deployment to heroku guide

    heroku login
    git commit -m "herokyu deployment-test added files" -a // Note: only if required to commit
    heroku git:remote -a web-content-moderation
    
    git push heroku master:main

## Useful Heroku commands
    heroku run bash -a web-content-moderation // to view all folder structures
