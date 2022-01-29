class Config:
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = '9f9253ffc1a37486ddc41ebbe3d8d5cc'
    SECRET_KEY_KEY = 'this is a secret key'
class ProductionConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True