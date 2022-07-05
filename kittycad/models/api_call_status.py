from enum import Enum


class ApiCallStatus(str, Enum):
    QUEUED = 'Queued'
    UPLOADED = 'Uploaded'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'
    FAILED = 'Failed'

    def __str__(self) -> str:
        return str(self.value)
