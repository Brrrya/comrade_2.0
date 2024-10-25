import asyncio

from bot.bot import start_bot
from service.config.config_loader import load_config


async def main():
    config = load_config()

    await start_bot(config)


if __name__ == '__main__':
    # try:
    asyncio.run(main())
    # except (KeyboardInterrupt, SystemExit):
    #     logging.info("Manual stop")
    # finally:
    #     logging.info("Bot was stopped")
