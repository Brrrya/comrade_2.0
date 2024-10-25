import os

from service.config.config_structure import Config, BotConfig, RedisConfig
from dotenv import load_dotenv

import logging

def load_config() -> Config:
    """Получить конфиг приложения"""
    logging.info("Loaded config")

    load_dotenv()

    api_token: str = os.getenv("API_TOKEN")

    redis_host: str = os.getenv("REDIS_HOST")
    redis_pass: str = os.getenv("REDIS_PASS")
    redis_port: str = os.getenv("REDIS_PORT")
    redis_numb: str = os.getenv("REDIS_NUMB")

    return Config(
        bot=BotConfig(api_token=api_token),
        redis=RedisConfig(
            redis_host=redis_host,
            redis_pass=redis_pass,
            redis_port=redis_port,
            redis_numb=redis_numb
        )
    )
