"""Module that defines the main class Manager."""

from dataclasses import asdict
import json
from pathlib import Path

from src.simple_account_manager.account import Account


class Manager:
    """The account manager class."""

    def __init__(self, master_key: str):
        self._version = '1.0'
        self._accounts = []

    @property
    def version(self) -> str:
        """The version property."""

        return self._version

    @property
    def accounts(self) -> list[Account]:
        """The accounts property."""

        return self._accounts

    def save_json(self, json_path: Path):
        """Save accounts to json file with encryption."""

        doc = {'accounts': {'version': self.version, 'data': []}}
        for account in self._accounts:
            doc['accounts']['data'].append(
                asdict(account,
                       dict_factory=lambda x:
                       {k: v
                        for (k, v) in x if v is not None}))
        with open(json_path, 'w', encoding='UTF-8') as fp:
            json.dump(doc, fp)

    def load_json(self, json_path: Path):
        """Load json file with encrypted fields to accounts."""

        accounts = []
        with open(json_path, 'r', encoding='UTF-8') as fp:
            doc = json.load(fp)
        version = doc['accounts']['version']
        for d in doc['accounts']['data']:
            account = Account(name=d['name'],
                              username=d['username'],
                              password=d['password'],
                              categories=d.get('categories'),
                              domain=d.get('domain'),
                              notes=d.get('notes'))
            accounts.append(account)
        self._version = version
        self._accounts = accounts
