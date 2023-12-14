

class InvalidLoanException(Exception):
    def __init__(self, message="Invalid loan exception"):
        self.message = message
        super().__init__(self.message)
