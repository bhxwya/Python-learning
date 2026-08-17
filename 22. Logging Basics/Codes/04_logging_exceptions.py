import logging

logging.basicConfig(
    level=logging.INFO,
    filename="log.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    1 / 0

except ZeroDivisionError as e:
    # Method 1: logging.exception() automatically includes traceback
    logging.exception("ZeroDivisionError")

    # Method 2: Same idea, but using logging.error() + exc_info=True
    # logging.error("ZeroDivisionError", exc_info=True)
    
    
    
# LOGGING EXCEPTIONS
# logging.exception() is used inside an except block.
# It automatically logs the exception and full traceback.

# Alternative:
# logging.error("ZeroDivisionError", exc_info=True)
# This also logs the exception + traceback.

# Therefore:
# logging.exception(...) == logging.error(..., exc_info=True)
# when used inside an except block.

# "as e" stores the exception object in e.
# If we don't use e, we can simply write:
# except ZeroDivisionError: