from dataclasses import dataclass


@dataclass
class BotConfig:
    """Bot config"""

    api_token: str


@dataclass
class RedisConfig:
    """Redis Connection config"""

    redis_host: str
    redis_pass: str
    redis_port: str
    redis_numb: str

    def get_connection_url(self) -> str:
        return f"redis://:{self.redis_pass}@{self.redis_host}:{self.redis_port}/{self.redis_numb}"


@dataclass
class Config:
    """App config"""

    bot: BotConfig
    redis: RedisConfig
