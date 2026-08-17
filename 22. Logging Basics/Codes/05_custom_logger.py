import logging

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler
handler = logging.FileHandler("test.log")

# Create the format
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Apply formatter to handler
handler.setFormatter(formatter)

# Connect handler to logger
logger.addHandler(handler)

# Create log message
logger.info("test the custom logger")

# CUSTOM LOGGER
# logging.getLogger(__name__) -> creates a logger for the current Python file.
# __name__ -> gives the name of the current module.

# Handler -> decides WHERE log messages go.
# FileHandler("test.log") -> sends logs to test.log.

# Formatter -> decides HOW each log message looks.
# %(asctime)s   -> date/time
# %(name)s      -> logger name
# %(levelname)s -> logging level
# %(message)s   -> actual message.

# setFormatter() -> applies the formatter to the handler.
# addHandler() -> connects the handler to the logger.

# logger.info() -> creates an INFO-level log message.


# FLOW:
# logger.info()
#      ↓
# Logger
#      ↓
# Handler
#      ↓
# Formatter
#      ↓
# test.log