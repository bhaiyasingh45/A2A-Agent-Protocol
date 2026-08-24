"""Simulate a small A2A-style agent exchange without an external framework."""

from message_model import Artifact, Message, Part
from task_model import Task


def research_agent(task: Task, request: Message) -> Artifact:
    task.start()

    query = next(
        (part.content for part in request.parts if part.kind == "text"),
        "",
    )

    artifact = Artifact(
        artifact_id=f"artifact-{task.task_id}",
        name="research-result",
        parts=[
            Part(
                kind="text",
                content=f"Research agent processed: {query}",
            )
        ],
    )

    task.complete(artifact_id=artifact.artifact_id)
    return artifact


if __name__ == "__main__":
    task = Task(task_id="task-002")
    request = Message(role="user")
    request.add_text("Find the latest A2A protocol concepts")

    result = research_agent(task, request)

    print("Task state:", task.state.value)
    print("Result:", result)
