# ANIC (AI Natural Intelligence Core)

## Architecture Focus

The core objective of the ANIC architecture is to provide a **swappable intelligence provider** system with **modular system-level capabilities**.

### Key Architectural Patterns:
- **Strategy Pattern**: Abstracting the "Brain" (LLM Provider) to allow seamless switching between Gemini, Ollama, and Qwen without affecting downstream logic.
- **Provider/Plugin Pattern**: Decoupling system interactions (Terminal, Browser, Office) from the core logic to enable high extensibility.
- **Centralized Event Dispatcher**: Managing multimodal inputs (Voice, Text, Vision) via an asynchronous message bus.

---

## Folder Structure

```text
anic-core/
├── src/
│  ├── brain/     # Brain-switching logic and providers
│  ├── plugins/    # System-level capabilities (Office, Terminal, etc.)
│  └── orchestrator/  # Core routing logic
└── README.md      # This file
```

---

*Note: This is a professional architectural showcase. Proprietary algorithms and hardware-specific integration layers are omitted to protect IP.*

