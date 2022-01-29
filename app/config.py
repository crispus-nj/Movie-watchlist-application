class Config:
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
class ProductionConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True