from dao.iloan_repository import ILoanRepository
from entity.model.loan import Loan
from exception.InvalidLoanException import InvalidLoanException

class LoanRepositoryImpl(ILoanRepository):
    def create_loan(self, loan: Loan) -> bool:
        pass

    def get_loan_by_id(self, loan_id: int) -> Loan:
        pass

    def update_loan_status(self, loan_id: int, new_status: str) -> bool:
        pass

    def delete_loan(self, loan_id: int) -> bool:
        pass

    def get_all_loans(self) -> list[Loan]:
        pass

from exception.InvalidLoanException import InvalidLoanException

class LoanRepositoryImpl(ILoanRepository):

    def get_loan_by_id(self, loan_id: int) -> Loan:
        # Logic to retrieve loan from the database
        if loan_not_found:
            raise InvalidLoanException("Loan not found with ID: {}".format(loan_id))
        else:
            return loan
