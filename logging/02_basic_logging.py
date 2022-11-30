import logging

logging.basicConfig(level=logging.DEBUG, filename="output.log", filemode="w")

logging.debug("This is a debug message")
logging.info(f"{123} This is a {'info'} message")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")
