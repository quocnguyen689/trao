import logging
import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from loguru import logger

BACKGROUND_THREADS = []
db = SQLAlchemy()

class LoguruHandler(logging.Handler):
    @staticmethod
    def formatter(record):
        if (
            type(record["message"]) is str
            and '"method":' in record["message"]
            and "error" not in record["message"]
        ):
            return '{{"@timestamp":"{time:YYYY-MM-DDTHH:mm:ss.SSSSSSSSS[Z]!UTC}","caller":"{name}/{function}:{line}","error":null,"level":"{level}",{message}}}\n'
        return '{{"@timestamp":"{time:YYYY-MM-DDTHH:mm:ss.SSSSSSSSS[Z]!UTC}","caller":"{name}/{function}:{line}","level":"{level}","message":"{message}"}}\n'

    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno
        logger_opt = logger.opt(exception=record.exc_info)
        logger_opt.log(level, record.getMessage())


def create_app(test_config=None):
    logger.remove()
    logger.add(
        sys.stderr,
        format=LoguruHandler.formatter,
        level="DEBUG",
    )
    gunicorn_logger = logging.getLogger("gunicorn.access")
    if len(gunicorn_logger.handlers) > 0:
        gunicorn_logger.handlers.clear()
        gunicorn_logger.setLevel(logging.INFO)
        gunicorn_logger.addHandler(LoguruHandler())

    # create and configure the app
    app = Flask(__name__)

    if test_config is None:
        # load the config, if it exists, when not testing
        app.config.from_object("exchange_items.config.default")
        if "APP_CONFIG_FILE" in os.environ:
            app.config.from_envvar("APP_CONFIG_FILE")
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # bootstrap database migrate commands
    db.init_app(app)
    # Migrate(app, db)

    from exchange_items.api import (
        api,
        ads,
        collections,
    )

    # Register blueprints
    api_bp = api.api
    api_bp.register_blueprint(ads.ads)
    api_bp.register_blueprint(collections.collections)
    app.register_blueprint(api_bp)

    return app
