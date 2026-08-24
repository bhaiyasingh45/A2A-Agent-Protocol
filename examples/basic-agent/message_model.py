"""Small, framework-independent models for A2A-style messages and artifacts."""

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

    def add_text(self, text: str) -> None:
        self.parts.append(Part(kind="text", content=text))

    def add_data(self, data: dict[str, Any]) -> None:
        self.parts.append(Part(kind="data", content=data))


@dataclass
class Artifact:
    artifact_id: str
    name: str
    parts: list[Part] = field(default_factory=list)

    def add_part(self, part: Part) -> None:
        self.parts.append(part)


if __name__ == "__main__":
    request = Message(role="user")
    request.add_text("Analyze the sales data")
    request.add_data({"dataset": "sales_2026"})

    report = Artifact(artifact_id="artifact-001", name="sales-report")
    report.add_part(Part(kind="text", content="Sales increased by 12%."))

    print("Request:", request)
    print("Artifact:", report)
