from typing import Optional

from src.models.Account.Account import Account
from src.repositories.AccountRepository import AccountRepository
from src.services.ServiceAbstract import ServiceAbstract


class AccountService(ServiceAbstract):
    def __init__(self):
        super().__init__(AccountRepository)

    def test_repo(self):
        account: Account
        try:
            account = Account(email='dsdasd@mail.com', password='anaAreMere')
        except Exception as e:
            print("Oopsie", e)
            account: Account = Account(email='dsdasd@mail.com', password='Adsadasd23_')
        # account = (account.model_dump())
        print("Account: ", account)
        account_id = ''
        try:
            print("Trying to create account")
            account_id = self.repository.create(account)
            print("Create succeed")
            print("Account id: ", account_id)
        except Exception as e:
            print(e)
        try:
            print("Trying to get account by id")
            result = self.repository.read_by_id(account_id)
            print("Read by succeed")
            print("Result", result)
        except Exception as e:
            print(e)
        try:
            print("Trying to get all accounts")
            result = self.repository.read_all()
            print("Read all succeed")
            print("Result", result)

        except Exception as e:
            print(e)
        try:
            print("Trying to delete account by id")
            result = self.repository.delete(account_id)
            print("Read all succeed")
            print("Result", result)
        except Exception as e:
            print(e)
        try:
            print("Trying to update account by id")
            account = Account(email='dsdasd2@mail.com', password='anaAreMere2')
            result = self.repository.update(account)
            print("Update succeed")
            print("Result", result)
        except Exception as e:
            print(e)

    def get_all(self):
        return self.repository.read_all()

    def get_by_id(self, account_id: str) -> Optional[Account]:
        return self.repository.read_by_id(account_id)

    def login(self, username, password):
        pass

    def logout(self):
        pass

    def register(self, username, password):
        pass

    def change_password(self, username, password):
        pass
