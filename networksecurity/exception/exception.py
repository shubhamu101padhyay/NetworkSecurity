import sys
from networksecurity.logging.logger import logging

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_detail:sys):
        self.error_message=error_message
        super().__init__(error_message)
        _,_,exc_tb=error_detail.exc_info()
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        self.lineno=exc_tb.tb_lineno

    def __str__(self):
        # Ekdum simple f-string format bina kisi .format() ke
        return f"Error occurred in python script name [{self.file_name}] at line number [{self.lineno}] with error message [{str(self.error_message)}]"
    