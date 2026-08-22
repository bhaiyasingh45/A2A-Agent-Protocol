# Agent Cards

An **Agent Card** describes an agent's capabilities and how another agent can connect to it.

## Purpose

A client should be able to discover an agent and understand:

- Who the agent is
- What the agent can do
- Which protocol/interface it supports
- Which skills are available
- How to reach the agent
- What authentication requirements apply

Conceptually:

```text
Agent Card
   |
   +-- Identity
   +-- Endpoint
   +-- Capabilities
   +-- Skills
   +-- Supported interfaces
   +-- Authentication information
```

## Example

A simplified Agent Card might look like:

```json
{
  "name": "Travel Planning Agent",
  "description": "Plans business and leisure travel itineraries",
  "url": "https://example.com/a2a",
  "version": "1.0.0",
  "capabilities": {
    "streaming": true,
    "pushNotifications": false
  },
  "skills": [
    {
      "id": "trip-planning",
      "name": "Trip Planning",
      "description": "Creates travel itineraries from user requirements"
    }
  ]
}
```

> The exact schema should follow the A2A specification version being implemented. This example is intentionally simplified for learning.

## Discovery

A client can discover the Agent Card through a known discovery mechanism or endpoint exposed by the remote agent. After discovery, the client can select an appropriate interaction method based on the advertised capabilities.

## Design principle

The Agent Card describes **what the agent can offer**, not how the agent internally performs the work.

For example, a travel agent might internally use an LLM, APIs, a database, and several MCP tools. None of those implementation details need to be exposed to another A2A client.

## Next

After discovering an agent, the client can create or continue a **task** and exchange messages associated with that task.
