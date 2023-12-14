from entity.customer import Customer
from entity.Loan import Loan
from entity.HomeLoan import HomeLoan
from entity.CarLoan import CarLoan
from dao.loan_repository_impl import LoanRepositoryImpl
from exception.invalid_loan_exception import InvalidLoanException

class LoanManagement:
    def _init_(self):
        self.loan_repository = ILoanRepositoryImpl()

    def display_menu(self):
        print("\nLoan Management System Menu:")
        print("1. Apply for a Loan")
        print("2. Get All Loans")
        print("3. Get Loan by ID")
        print("4. Loan Repayment")
        print("5. Exit")

    def apply_loan(self):
        try:
            customer_id = input("Enter Customer ID: ")
            name = input("Enter Name: ")
            credit_score = input("Enter Credit Score: ")

            customer = Customer(customer_id, name, credit_score)

            loan_type = input("Enter Loan Type (HomeLoan or CarLoan): ")
            principal_amount = input("Enter Principal Amount: ")
            interest_rate = input("Enter Interest Rate: ")
            loan_term = input("Enter Loan Term (in months): ")

            if loan_type == "HomeLoan":
                property_address = input("Enter Property Address: ")
                property_value = input("Enter Property Value: ")
                loan = HomeLoan(None, customer, principal_amount, interest_rate, loan_term, property_address, property_value, "Pending")
            elif loan_type == "CarLoan":
                car_model = input("Enter Car Model: ")
                car_value = input("Enter Car Value: ")
                Loan = CarLoan(None, customer, principal_amount, interest_rate, loan_term, car_model, car_value, "Pending")


            self.loan_repository.applyLoan(Loan)
            print("Loan application submitted successfully.")
        except InvalidLoanException as e:
            print(f"Error applying for a loan: {e}")

    def get_all_loans(self):
        try:
            loans = self.loan_repository.getAllLoan()
            print("All Loans:")
            for loan in loans:
                print(loan)
        except InvalidLoanException as e:
            print(f"Error getting all loans: {e}")

    def get_loan_by_id(self):
        loan_id = input("Enter Loan ID: ")
        try:
            loan = self.loan_repository.getLoanById(loan_id)
            print("Loan Details:")
            print(loan)
        except InvalidLoanException as e:
            print(f"Error getting loan by ID: {e}")

    def loan_repayment(self):
        loan_id = input("Enter Loan ID for repayment: ")
        amount = input("Enter Repayment Amount: ")
        try:
            self.loan_repository.loanRepayment(loan_id, amount)
            print("Repayment successful.")
        except InvalidLoanException as e:
            print(f"Error processing loan repayment: {e}")

    def main(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.apply_loan()
            elif choice == "2":
                self.get_all_loans()
            elif choice == "3":
                self.get_loan_by_id()
            elif choice == "4":
                self.loan_repayment()
            elif choice == "5":
                print("Exiting Loan Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if _name_ == "_main_":
    loan_management = LoanManagement()
    loan_management.main()