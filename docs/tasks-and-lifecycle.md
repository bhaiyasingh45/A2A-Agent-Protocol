# A2A Tasks and Lifecycle

A2A communication is task-oriented. A client agent sends a request to a remote agent, and the remote agent may process the work synchronously, asynchronously, or through streaming updates.

## Core lifecycle

A task can be thought of as moving through states such as:

```text
submitted → working → completed
                    ↘ failed
                    ↘ canceled
```

The exact transition behavior depends on the operation and implementation, but the important idea is that the client should not assume every request finishes immediately.

## Task identity

A task has a stable identifier so the client and server can correlate follow-up requests and status updates.

A useful implementation model is:

```python
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
```

## Why this matters

The task abstraction allows agents to support long-running work without keeping an HTTP request open for the entire computation.

Examples include:

- A research agent generating a large report.
- A data agent running a multi-step analysis.
- A planning agent coordinating several downstream agents.
- An automation agent waiting for an external system to finish.

## Client responsibilities

A client should:

1. Create or submit a task request.
2. Capture the returned task identifier.
3. Observe task state when work is asynchronous.
4. Consume resulting messages or artifacts.
5. Handle failure and cancellation explicitly.

## Server responsibilities

A server should:

1. Validate the incoming request.
2. Create or resolve the task.
3. Report meaningful state transitions.
4. Produce messages or artifacts as work progresses.
5. Finish with a terminal state.

## Design principle

Do not model an agent call as only `request -> response`. A2A becomes useful for agentic systems when the protocol can represent **ongoing work, state, and results**.
