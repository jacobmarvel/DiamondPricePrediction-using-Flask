
import logging
import os
from datetime import datetime


LOG_FILE  =f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(),"logs")

os.makedirs(log_path, exist_ok = True)

LOG_FILEPATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(level = logging.INFO,
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s -  %(levelname)s - %(message)s"
                    )

if __name__ == "__main__":
    logging.info("I have just tested agin here")  # if u run this code you cans ee the same file as u did in jupyter nb