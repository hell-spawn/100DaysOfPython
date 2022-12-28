"""
Exercise 93: Using a logger Object
"""

import logging

logger = logging.getLogger("my_logger")

logger.debug("Logging at debug")
logger.info("Logging at info")
logger.warning("Logging at warning")
logger.error("Logging at error")
logger.fatal("Logging at fatal")

system = "moon"
for number in range(3):
    logger.warning("%d errors reported in %s", number, system)

try:
    int("nope")
except Exception:
    logging.error("Something bad happened", exc_info=True)

try:
    int("nope")
except Exception:
    logging.exception("Something bad happened")

variable = "for logger"
# prefer
logging.info("string template %s", variable)
# to
logging.info("string template {}".format(variable))

d = dict()
# Prefer
try:
    d["missing_key"] += 1
except Exception:
    logging.error("Something bad happened", exc_info=True)
# to
try:
    d["missing_key"] += 1
except Exception as e:
    logging.error("Something bad happened: %s", e)
