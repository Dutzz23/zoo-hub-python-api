from typing import Optional

from bson import ObjectId

from app.models.Account.Usr import Usr
from app.repositories import RepositoryAbstract


class AccountRepository(RepositoryAbstract):
    def __init__(self):
        table_name = 'accounts'
        super().__init__(table_name, Usr)

    def create_account(self, account: Usr) -> Optional[str]:
        """
        Create a new account.
        """
        try:
            account_dict = account.dict(exclude={"id"})  # Exclude the id field
            result = self.collection.insert_one(account_dict)
            return str(result.inserted_id)
        except Exception as e:
            print(e)
        return None
    
    def read_account_by_id(self, account_id: str) -> Optional[Usr]:
        """
            Retrieve an account by their ID.
        """
        try:
            account = self.collection.find_one({'_id': ObjectId(account_id)})
            return account
        except Exception as e:
            print(e)
        return None

    def read_account_by_email(self, email: str) -> Optional[Usr]:
        """
            Retrieve an account by its email.
        """
        try:
            account = self.collection.find_one({"email": email})
            return Usr(**account)
        except Exception as e:
            print(e)
        return None

    def update_account(self, account: Usr) -> bool:
        """
        Update an account.
        """
        updated_fields = {}

        for key, value in account.dict(exclude={"id"}).items():
            if value is not None:
                updated_fields[key] = value

        # Update the user in the database
        try:
            result = self.collection.update_one({"_id": account.id}, {"$set": updated_fields})
            return result.modified_count > 0
        except Exception as e:
            print(e)
        return False

    def delete_account(self, account: Usr) -> bool:
        pass
