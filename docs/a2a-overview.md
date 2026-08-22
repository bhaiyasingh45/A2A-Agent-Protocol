# A2A Protocol Fundamentals

## Agent2Agent communication

A2A defines a common way for one agent (the client) to interact with another agent (the remote/server agent) without requiring knowledge of the remote agent's internal implementation.

The remote agent can use any suitable framework or model internally. A2A focuses on the interaction boundary.

## Core concepts

### Agent

An autonomous software component that can perform work on behalf of a user or another agent.

### Agent Card

A machine-readable description of an agent's identity, capabilities, supported interfaces, and interaction requirements. It allows clients to understand how to interact with an agent before sending work.

### Task

A unit of work requested from an agent. A task can move through multiple states and may produce one or more artifacts.

### Message

A communication unit exchanged during an interaction. Messages contain content parts and can represent requests, responses, or additional communication related to a task.

### Artifact

A resulting output produced while completing a task. Examples include text, structured data, files, or other generated content.

## Typical flow

```text
Client Agent
     |
     | Discover Agent Card
     v
Remote Agent
     |
     | Send task/message
     v
Task Processing
     |
     | status updates / result
     v
Artifact / Final Response
```

## Why A2A matters

Traditional agent systems often become tightly coupled because each agent exposes a custom API and custom payload format. A2A establishes a shared protocol boundary so agents can collaborate without sharing their internal prompts, tools, memory, or framework implementation.

## A2A vs MCP

A2A and MCP solve different problems:

| Protocol | Primary purpose |
|---|---|
| MCP | Agent/application ↔ tools, resources, and context | 
| A2A | Agent ↔ agent collaboration |

A production agent can use MCP internally to access tools while using A2A externally to collaborate with another agent.

## Next

The next module focuses on the **Agent Card**, which is the discovery and capability contract used before an agent interaction begins.
