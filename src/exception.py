import sys
from src.logger import logging

def error_message_detail(error, error_detail):
    if error_detail is not None:
        _, _, exc_tb = error_detail
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            file_name, exc_tb.tb_lineno, str(error))
        return error_message
    else:
        # Handle the case where error_detail is None (no exception being handled)
        return str(error)

class CustomException(Exception):
    def __init__(self, error_message, error_detail=None):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
