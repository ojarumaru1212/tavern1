# print("this only prints to console")

import logging
# logging.basicConfig(level=logging.DEBUG)

# logging.info("this is info")
# logging.warning("this is warning")
# logging.error("this is error")
# logging.debug("this is debug")
# logging.critical("this is critical")

# initialzing logger object
logger = logging.getLogger(__name__)

# formatting
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S%p')

# root logger level
logger.setLevel(logging.DEBUG)

# handlers
filehandler = logging.FileHandler('test.log', mode='a')
filehandler.setLevel(logging.DEBUG)
filehandler.setFormatter(formatter)

# add handlers to logger
logger.addHandler(filehandler)

logger.info("this is test log")

