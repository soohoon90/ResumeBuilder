import os

class Config(object):
    DEBUG = True
    TESTING = False
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
    FBAPI_SCOPE = ['user_about_me', 'user_work_history', 'user_website', 'user_interests',
                   'user_education_history', 'user_activities']
    FBAPI_APP_ID = 204430279623711
    FBAPI_APP_SECRET = '95619848e20b9c7110c54d57ff673ffb'
