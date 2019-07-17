class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    TESTING = True
    PROFILE = False


class TestConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    TESTING = True
    PROFILE = True


class ProductionConfig(Config):
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False
    PROFILE = False
