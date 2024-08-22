"""Test module for the class Manager."""
from src.simple_account_manager.manager import Manager


class TestManager:

    def test_new_manager_with_defaults(self):
        """Test for creating a new Manager object with defaults."""

        manager = Manager()

        # Verify accounts.
        assert len(manager.accounts) == 0
