# A2A Agent Protocol

A hands-on repository for learning and implementing the **Agent2Agent (A2A) protocol**.

## What is A2A?

A2A is an open protocol for enabling AI agents built by different frameworks, vendors, and teams to communicate and collaborate with each other.

Instead of forcing agents to share internal implementation details, A2A provides a common communication contract around capabilities, tasks, messages, and artifacts.

## Repository Goals

- Understand the A2A protocol from fundamentals to implementation.
- Build A2A-compatible agents in Python.
- Understand Agent Cards and agent discovery.
- Implement task lifecycle and state transitions.
- Exchange messages and artifacts between agents.
- Explore synchronous, asynchronous, and streaming interactions.
- Build multi-agent workflows using A2A.
- Add tests that validate protocol behavior.

## Learning Path

1. A2A fundamentals
2. Agent Cards and discovery
3. Messages, Parts, and Artifacts
4. Tasks and task lifecycle
5. Request/response communication
6. Streaming and asynchronous tasks
7. Multi-agent collaboration
8. Authentication and production considerations
9. Protocol testing and interoperability

## Planned Structure

```text
A2A-Agent-Protocol/
├── README.md
├── docs/
│   ├── a2a-overview.md
│   ├── agent-cards.md
│   ├── tasks-and-lifecycle.md
│   ├── messages-and-artifacts.md
│   ├── streaming.md
│   └── multi-agent-communication.md
├── examples/
│   ├── basic-agent/
│   ├── agent-discovery/
│   └── multi-agent/
├── src/
│   └── a2a_demo/
└── tests/
```

## Status

🚧 Initial setup. Implementation examples will be added incrementally.

## Scope

This repository is specifically about **A2A / Agent2Agent communication**. It intentionally does not include the separate SDD workstream.
