import logging
from logging.config import dictConfig
from logging.config import fileConfig
import sys

#root_logger = logging.getLogger()
#handler = logging.StreamHandler(sys.stdout)
#formatter = logging.Formatter("%(levelname)s: %(message)s")
#handler.setFormatter(formatter)
#root_logger.addHandler(handler)
#root_logger.setLevel("INFO")
#
#logging.info("Hello logging world")

dictConfig({
    "version": 1,
    "formatters": {
        "short":{
            "format": "%(levelname)s: %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "short",
            "stream": "ext://sys.stdout",
            "level": "DEBUG",
        }
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO"
        }   
    }
})
logging.info("Hello logging world")

logging.basicConfig(
        level="INFO",
        format="%(levelname)s: %(message)s",
        stream=sys.stdout
        )


logging.info("Hello logging world")


fileConfig("logging-config.ini")
logging.info("Hello there!")
