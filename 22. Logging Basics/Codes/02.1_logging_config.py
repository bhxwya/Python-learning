import logging

logging.basicConfig(
    level=logging.INFO,
    filename="log.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

# format= controls how each log message is written.

# %(asctime)s     -> time/date when the log was created
# %(levelname)s   -> logging level (INFO, WARNING, ERROR, etc.)
# %(message)s     -> actual message we wrote

# Example:
# 2022-04-18 19:13:39,277 - ERROR - error

# This tells us:
# WHEN     -> 2022-04-18 19:13:39,277
# LEVEL    -> ERROR
# MESSAGE  -> error


# %(name)s -> name of the logger.
# "root" is the default/root logger used by logging.info(), logging.error(), etc.