import sys
from networksecurity.logging.logger import logging

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_detail:sys):
        self.error_message=error_message
        super().__init__(error_message)
        _,_,exc_tb=error_detail.exc_info()
        file_name=exc_tb.tb_frame.f_code.co_filename
        self.lineno=exc_tb.tb_lineno

    def __str__(self):
        return f"Error occured in python script {[0]} at line number {[1]} with error message {[2]}".format(
            self.file_name,self.lineno,str(self.error_message)
        )
    