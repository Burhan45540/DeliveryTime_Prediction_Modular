import os
from datetime import datetime
import logging

logs_dir="logs"
logs_dir=os.path.join(os.getcwd(),logs_dir)

os.makedirs(logs_dir,exist_ok=True)

logs_file_path=os.path.join(logs_dir,
                            f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.logs"
                            )

logging.basicConfig(
    filename=logs_file_path,
    format="[%(asctime)s]  %(filename)s %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO

)



logging.debug("This is DEBUG message")
logging.info("This is INFO message")
logging.warning("This is WARNING message")
logging.error("This is ERROR message")
logging.critical("This is CRITICAL message")