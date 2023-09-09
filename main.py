import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "apiKey":os.getenv('apiKey'),           
    "authDomain":os.getenv('authDomain'),   
    "storageBucket":os.getenv('storageBucket'),     
    "messagingSenderId":os.getenv('messagingSenderId'), 
    "appId":os.getenv('appId'),            
    "measurementId":os.getenv('measurementId'),
    "keyFirebase": "keyFirebase.json"
}