class NewLogger:
    def log(self,message):
        print(f"New Logger: {message}")

class OldLogger:
    def log_message(self,message):
        print(f"Old Logger: {message}")

class Adapter(NewLogger):
    def __init__(self,old_logger):
        self.old_logger=old_logger
    def log(self,message):
        print("Adapter is used")
        self.old_logger.log_message(message)
def client_code(logger):
    logger.log("This is a log message")

old_logger=OldLogger()
adapter=Adapter(old_logger)
client_code(adapter)
