import importlib.machinery
import os

from loguru import logger

if "APP_CONFIG_FILE" in os.environ:
    logger.info(f"Load config from {os.environ['APP_CONFIG_FILE']}")
    loader = importlib.machinery.SourceFileLoader(
        "production_config", os.environ["APP_CONFIG_FILE"]
    )
    production_config = loader.load_module()
    globals().update(vars(production_config))
else:
    logger.info(f"Load config from default")
    from exchange_items.config.default import *
