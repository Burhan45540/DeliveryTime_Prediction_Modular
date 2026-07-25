import os,sys
from src.logger import logging

def error_message_details(error_message:Exception,error_details:sys):

    _,_,exc_tb=error_details.exc_info()

    filename=exc_tb.tb_frame.f_code.co_filename
    line_no=exc_tb.tb_lineno

    error_message=(
            f"Error occured in file [{filename}]"
            f"and line no [{line_no}]"
            f" with error message [{str(error_message)}]"

         )
    return error_message



class CustomException(Exception):

    def __init__(self, error_message:Exception,error_details:sys):

        super().__init__(error_message)

        self.error_message=error_message_details(
            error_message=error_message,
            error_details=error_details
        )



    def __str__(self):
        return self.error_message



if __name__=="__main__":

    try:
        a=10/0

    except Exception as e:
        logging.error("It gives Infinite Output")
        raise CustomException(e,sys)



