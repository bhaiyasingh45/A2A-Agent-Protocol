"""Minimal task model inspired by A2A task-oriented communication."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class TaskState(str, Enum):
    SUBMITTED = "submitted"
    WORKING = "working"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELED = "canceled"


@dataclass
class Task:
    task_id: str
    state: TaskState = TaskState.SUBMITTED
    metadata: dict[str, Any] = field(default_factory=dict)

    def start(self) -> None:
        if self.state != TaskState.SUBMITTED:
            raise ValueError(f"Cannot start task from {self.state}")
        self.state = TaskState.WORKING

    def complete(self, **metadata: Any) -> None:
        if self.state != TaskState.WORKING:
            raise ValueError(f"Cannot complete task from {self.state}")
        self.metadata.update(metadata)
        self.state = TaskState.COMPLETED

    def fail(self, reason: str) -> None:
        if self.state not in {TaskState.SUBMITTED, TaskState.WORKING}:
            raise ValueError(f"Cannot fail task from {self.state}")
        self.metadata["error"] = reason
        self.state = TaskState.FAILED


if __name__ == "__main__":
    task = Task(task_id="task-001")
    print(task)

    task.start()
    print(task)

    task.complete(result="Agent completed the requested work")
    print(task)
