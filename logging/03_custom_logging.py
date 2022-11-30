import logging

extra_data = {"user": "user@example.com"}
fmtstr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User: %(user)s %(message)s"
datestr = "%m/%d/%Y %I:%M:%S %p"
logging.basicConfig(level=logging.DEBUG,
                    filename="output.log", filemode="w", format=fmtstr, datefmt=datestr)


def custom_logging():
    logging.debug("This is a debug message", extra=extra_data)
    logging.info(f"{123} This is a {'info'} message", extra=extra_data)
    logging.warning("This is a warning message", extra=extra_data)
    logging.error("This is a error message", extra=extra_data)
    logging.critical("This is a critical message", extra=extra_data)


custom_logging()
