# Code Nexus: Enterprise Data Pipeline System

Code Nexus is a high-performance Python framework designed to handle polymorphic data streams through a unified, stage-based processing architecture. It leverages advanced Object-Oriented Programming (OOP) patterns to ensure scalability, type safety, and error resilience.

## 🏗 Architecture Overview

The system is built on three core pillars of modern Python development:

### 1. The Pipeline Pattern
Each pipeline consists of multiple stages that follow the `StageProtocol`. Data flows sequentially from one stage to the next, allowing for a clean separation of concerns.



### 2. Adapters & Streams
Specialized adapters (JSON, CSV, Stream) wrap the core pipeline logic to handle format-specific output. Meanwhile, `DataStream` subclasses handle domain-specific logic like environmental sensor parsing or financial transaction net-flow.

### 3. Nexus Management
The `NexusManager` acts as the central orchestrator. It registers pipelines and provides a `run_safe` execution layer to prevent system-wide crashes during data processing.



---

## 🚀 Key Features

* **Polymorphic Processing:** Process diverse data formats using a single, consistent interface.
* **Stage-Based Pipeline:** Modular architecture allowing you to chain "Stages" (Input, Transform, Output) dynamically.
* **Abstract Foundation:** Uses Python’s `abc.ABC` to enforce strict implementation contracts.
* **Static Duck Typing:** Implements `typing.Protocol` to ensure pipeline stages are compatible without rigid inheritance.
* **Fault Tolerance:** Built-in error recovery mechanisms within the manager to handle pipeline failures gracefully.

---

## Author

- Mohamad Daakour

## Resources

- Youtube Videos
- Gemini to learn the new concepts

