# A2A Messages and Artifacts

A2A separates the conversation around a task from the concrete results produced by an agent.

## Message

A message carries conversational information between agents. A message can contain one or more parts.

Conceptually:

```text
Message
└── Parts
    ├── Text
    ├── File / binary content
    └── Structured data
```

## Artifact

An artifact represents a result produced while completing a task. Artifacts are useful when an agent generates something that should be consumed independently from the conversational message.

Examples:

- A generated report
- A JSON dataset
- A code file
- A chart
- A document

## Minimal Python representation

```python
from dataclasses import dataclass, field
from typing import Any


@dataclass
class Part:
    kind: str
    content: Any


@dataclass
class Message:
    role: str
    parts: list[Part] = field(default_factory=list)


@dataclass
class Artifact:
    artifact_id: str
    name: str
    parts: list[Part] = field(default_factory=list)
```

## Message vs Artifact

Use a **message** when an agent is communicating with another agent. Use an **artifact** when the interaction produces a durable result that can be referenced, transferred, or consumed separately.

This distinction becomes important in long-running workflows where an agent may send progress messages while producing one or more final artifacts.
