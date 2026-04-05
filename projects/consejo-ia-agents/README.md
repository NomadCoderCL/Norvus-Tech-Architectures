# ConsejoIA (Agentic Decision Framework)

## Architecture Focus

ConsejoIA is a specialized framework for **autonomous agentic workflows**, utilizing a graph-based orchestration model to manage complex decision-making processes.

### Key Architectural Patterns:
- **Graph-Based Orchestration**: Modelling agent interactions as nodes and edges in a stateful directed acyclic graph (DAG).
- **State Persistence**: Ensuring agents maintain context across multiple turns of reasoning and external tool calls.
- **Multi-Agent Collaboration**: Enabling specialized agents (Researcher, Critic, Writer) to collaborate through shared state buffers.

---

## Folder Structure

```text
consejo-ia-agents/
├── src/
│  ├── orchestrator/  # Graph management and routing logic
│  ├── agents/     # Individual agent definitions and roles
│  └── state/     # State schemas and persistence layers
└── README.md      # This file
```

---

*Note: This is a professional architectural showcase. Proprietary agentic prompts, graph weights, and specific reasoning trees are omitted to protect IP.*

