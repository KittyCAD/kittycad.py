from enum import Enum


class UnitRadioactivityFormat(str, Enum):
    BECQUEREL = 'becquerel'
    CURIE = 'curie'
    RUTHERFORD = 'rutherford'

    def __str__(self) -> str:
        return str(self.value)
