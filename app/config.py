class Config(object):
    ENV = 'production'
    DEBUG = False
    TESTING = False
    MINIFY_HTML = True
    SESSION_COOKIE_SECURE = True
    SEND_FILE_MAX_AGE_DEFAULT = 43200


class ProdConfig(Config):
    pass


class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True

    SESSION_COOKIE_SECURE = False
