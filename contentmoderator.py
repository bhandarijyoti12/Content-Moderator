# pip install requests
# get API key from https://www.thetextapi.com
# imports
import requests
import json
from config import apikey
# create headers
headers = {
    "Content-Type": "application/json",
    "apikey": "e5254df0-1374-4e6f-839a-34d6fc6a4183"
}
# create keywords
keywords = ["fuck", "damn", "shit", "sexual assault", "rape", "gun"]
# url
url = "https://app.thetextapi.com/text/sentences_with_keywords"
 
moderation = {
    0: "safe",
    1: "13+"
}
# create function
def moderate(text: str):
    # create the body from the text
    body = {
        "text": text,
        "keywords": keywords
    }
    # pass in with keywords
    response = requests.post(url=url, headers=headers, json=body)
    # receive response and check for returned sentences
    _dict = json.loads(response.text)
 
    # grade returned sentences for 13+, 18+
    rating = 0
    mod_status = ""
    for kw in keywords[:3]:
        rating += len(_dict[kw])
    if rating in moderation:
        mod_status = moderation[rating]
    else:
        mod_status = "18+"
   
    # grade for trigger warning
    triggers = 0
    trigger_warning = False
    for kw in keywords[3:]:
        triggers += len(_dict[kw])
    if triggers > 0:
        trigger_warning = True
   
    # return response
    return mod_status, trigger_warning