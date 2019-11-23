import os


class Config:
    SECRET_KEY = 'super_secret_key'


class TestConfig:
    SECRET_KEY = 'super_secret_test_key'


class ProdConfig:
    SECRET_KEY = 'super_secret_prod_key'


def run_config():
    env = os.environ.get("ENV")
    if env == "TEST":
        return TestConfig
    elif env == "PROD":
        return ProdConfig
    else:
        return Config
