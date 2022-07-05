from enum import Enum


class AccountProvider(str, Enum):
    GOOGLE = 'google'
    GITHUB = 'github'

    def __str__(self) -> str:
        return str(self.value)
