import requests
import json
from Password import PassWord, UserName

print("Start 12-Adding Features")
x = 4.480795
y = 51.920929
   
layerUrl = "http://services.arcgis.com/emS4w7iyWEQiulAb/arcgis/rest/services/Windmills_EGT16/FeatureServer/1"

print("Creating Feature")
features = []

feature ={}
feature["attributes"] = {}
feature["attributes"]["NAME"] = "Onze GisTech Molen, Dene bedankt!"
feature["geometry"] = {}
feature["geometry"]["x"] = x
feature["geometry"]["y"] = y
feature["geometry"]["spatialReference"] = {"wkid" : 4326}


features.append(feature)

print("Getting token")
#get Token
token_URL = 'https://www.arcgis.com/sharing/generateToken'
token_params = {'username':UserName,'password': PassWord,'referer': 'http://www.arcgis.com','f':'json','expiration':60}
r = requests.post(token_URL,token_params)
token_obj= r.json()
token = token_obj["token"]

print("sending request")
addFeatureUrl = "{}/AddFeatures".format(layerUrl,token)
params = {'token':token,'features':json.dumps(features),'f':'json'}
    
r = requests.post(addFeatureUrl,params)
print(r.json())

print("Script complete")