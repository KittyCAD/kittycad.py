from enum import Enum


class ExecutionJobStatus(str, Enum):
    """Customer-visible execution lifecycle state."""  # noqa: E501

    """# Waiting for an orchestrator to claim the job."""  # noqa: E501

    QUEUED = "queued"

    """# Allocating isolated compute and staging inputs."""  # noqa: E501

    PROVISIONING = "provisioning"

    """# Customer code is running."""  # noqa: E501

    RUNNING = "running"

    """# Cancellation has been requested and compute is being terminated."""  # noqa: E501

    CANCELING = "canceling"

    """# Outputs, logs, and trusted usage are being finalized."""  # noqa: E501

    FINALIZING = "finalizing"

    """# The job was canceled."""  # noqa: E501

    CANCELED = "canceled"

    """# The job exceeded its requested timeout."""  # noqa: E501

    TIMED_OUT = "timed_out"

    """# The command and output finalization succeeded."""  # noqa: E501

    SUCCEEDED = "succeeded"

    """# The job failed."""  # noqa: E501

    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
