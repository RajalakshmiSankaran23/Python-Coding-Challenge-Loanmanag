from .Customer import Customer
from .Loan import Loan
from .HomeLoan import HomeLoan
from .CarLoan import CarLoan

# model.py
class Customer:
    def __init__(self, customer_id=None, name=None, email=None, phone=None, address=None, credit_score=None):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.credit_score = credit_score

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, " \
               f"Address: {self.address}, Credit Score: {self.credit_score}"

class Loan:
    def __init__(self, loan_id=None, customer=None, principal_amount=None, interest_rate=None, loan_term=None,
                 loan_type=None, loan_status=None):
        self.loan_id = loan_id
        self.customer = customer
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.loan_type = loan_type
        self.loan_status = loan_status

    def __str__(self):
        return f"Loan ID: {self.loan_id}, Customer: {self.customer}, Principal Amount: {self.principal_amount}, " \
               f"Interest Rate: {self.interest_rate}, Loan Term: {self.loan_term}, Loan Type: {self.loan_type}, " \
               f"Loan Status: {self.loan_status}"

class HomeLoan(Loan):
    def __init__(self, loan_id=None, customer=None, principal_amount=None, interest_rate=None, loan_term=None,
                 loan_status=None, property_address=None, property_value=None):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, "HomeLoan", loan_status)
        self.property_address = property_address
        self.property_value = property_value

    def __str__(self):
        return f"{super().__str__()}, Property Address: {self.property_address}, Property Value: {self.property_value}"


class CarLoan(Loan):
    def __init__(self, loan_id=None, customer=None, principal_amount=None, interest_rate=None, loan_term=None,
                 loan_status=None, car_model=None, car_value=None):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, "CarLoan", loan_status)
        self.car_model = car_model
        self.car_value = car_value

    def __str__(self):
        return f"{super().__str__()}, Car Model: {self.car_model}, Car Value: {self.car_value}"


