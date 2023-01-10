import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"

    MONGODB_SETTINGS = { 'db' : 'myflixvid' } # mongolocal
    
    # MONGODB_SETTINGS = { 'db' : 'myflix', "host":'mongodb://restheart:R3ste4rt!@34.142.32.93:80/myflix'} # gcloud
    # MONGODB_SETTINGS = { 'db' : 'myflix', "host":'http:34.142.32.93/myflix'} # gcloud