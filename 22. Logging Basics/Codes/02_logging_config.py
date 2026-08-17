import logging

logging.basicConfig(
    level=logging.INFO,
    filename="log.log",
    filemode="w"
)

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")


# basicConfig() configures how logging behaves.
# level=logging.INFO -> records INFO and all levels above it.
# filename="log.log" -> saves logs into log.log instead of the terminal.
# filemode="w" -> overwrites the log file each time the program runs.

# Since level is INFO:
# DEBUG is ignored.
# INFO, WARNING, ERROR and CRITICAL are recorded.