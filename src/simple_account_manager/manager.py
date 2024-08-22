"""Module that defines the main class Manager."""
from src.simple_account_manager.account import Account


class Manager:
    """The account manager class."""

    def __init__(self, ):
        self._accounts = []

    @property
    def accounts(self) -> list[Account]:
        return self._accounts
