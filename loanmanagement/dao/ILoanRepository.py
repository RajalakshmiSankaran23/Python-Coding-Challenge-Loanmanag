from entity.model.loan import Loan

class ILoanRepository(ABC):
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
