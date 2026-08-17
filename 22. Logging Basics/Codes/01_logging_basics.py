import logging

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

# LOGGING MODULE
# logging records events/messages that happen while a program runs.
# It is preferred over print() in real applications because messages
# can be categorized by severity and controlled/saved easily.

# Logging levels:
# DEBUG    -> detailed information useful for developers
# INFO     -> normal information about program execution
# WARNING  -> something unexpected, but the program can continue
# ERROR    -> something failed
# CRITICAL -> very serious problem that may stop the program

# By default, Python shows WARNING and above.
# Therefore DEBUG and INFO may not appear in the output.