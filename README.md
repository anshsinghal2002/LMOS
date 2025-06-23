# LMOS
AI Powered Bot Network


## 1. Framework Overview

A modular automation framework where “bots” execute “limbs” (executable packages for low-level tasks) based on parameters defined in XML launch files. The architecture separates high-level task logic (bots) from low-level execution (limbs), allowing granular permission control and easy extension.

---

## 2. Bot Interface & Execution

- **Main Bot Interface Class:**
    - Core class responsible for actuating limbs based on parameters.
    - Supports multiple template interfaces to distinguish worker bots by function.
    - Common execution flags/presets (e.g., **`task_completed`**, **`waiting_on[]`**) are built-in.
- **Sticky Bots:**
    - Bots persist on a synchronized runtime, enabling ongoing automation beyond simple scripts.
    - Bots can communicate via a topic/subscriber network.
- **Simple by Design:**
    - Bots are intentionally simple; complex workflows are divided among multiple bots for control and clarity.
    - XML build files remain simple, supporting future orchestration by intelligent layers.

---

## 3. Limbs

- **Definition:**
    - Limbs are simple executables performing low-level tasks given input.
- **Assignment & Permissions:**
    - Bots only have access to a pool of assigned limbs, controlling permissions and capabilities.
- **Execution:**
    - Limbs are actuated according to parameters in the XML launch file.

---

## 4. XML Launch Files

- **Role:**
    - Define automation type, execution flow, assigned limbs, and actuation parameters for each bot.
- **Simplicity:**
    - Designed to be easy to generate and parse, enabling scalable orchestration by higher-level systems.

---

## 5. Orchestration & Verification Layers

- **Orchestration Layer (Phase 2):**
    - Powered by fine-tuned local LLMs, this layer breaks down natural language tasks into subtasks and spins up bots using XML launch files.
    - Simplicity of XML ensures low failure rates in automated bot generation.
    - Recursively breaks down tasks and evaluates at each level if n-subtask is simple enough to delegate to a bot
- **Verification Layer (Phase 3):**
    - Runs parallel to bots, measuring output accuracy with redundancies.
    - Handles anomalies with semi-automated intervention.
    - Provides automated version control and rollbacks for select use cases.

---

## 6. Intelligent Limbs & LLM Integration

- **Intelligent Limbs:**
    - Limbs that consult LLMs for appropriate responses or execution scripts.
    - Consultant LLMs can be specialized (text-to-text, img-to-text, text-to-image, audio-to-text, audio-to-audio, etc.).
    - Each limb’s “Consultant LLM” is defined in the XML file, choosing from a loaded in LLM at runtime; one bot can use multiple instances of the same limb, each consulting a different LLM. The consultant LLM is essentially a parameter for an intelligent limb.
    - The runtime manages a pool of LLMs, spinning them up or down based on recent usage (up to a max limit).
- **Example Intelligent Actuation:**
    - Bot1: Watches for a **`significant_change`** flag in the runtime; when set, creates a backup of a file.
    - Bot2: Periodically surveys a file, sends previous and latest contents to an LLM to assess for significant change. If detected, flips the **`significant_change`** flag.
    - Enhancement: LLM generates a commit message; Bot2 posts this to a topic that Bot1 watches.

---

## 7. Scalability & Extensibility

- **AI-Driven Improvement:**
    - The framework benefits from ongoing LLM advancements, especially lightweight local models.
- **Beyond File Exploration:**
    - While initial focus is on file automation, the framework can be extended to:
        - Security automation (e.g., controlling a security layer)
        - NPC creation: Narrow interaction-tree NPCs with LLM-powered adaptability
            - Each NPC is a collection of bots (e.g., npc_eye, npc_ears for sensing; npc_arms, npc_mouth, npc_legs for actions)
            - Each NPC action is mapped to a limb
            - Example: npc_ears transcribes audio/conversation via LLM and publishes to a topic; npc_mouth uses an LLM to generate responses; npc_eyes consults an img-to-text LLM; npc_legs/hands coordinate actions.
- **Vertical Orchestration:**
    - Tasks can be broken down into subtasks, sub-subtasks, etc., with each layer spinning up bots for execution, enabling increasingly complex automation.
- **Vision:**
    - The ultimate goal is an OS built around this modular, AI-powered automation framework.

---

## 8. Key Principles

- **Decoupling:**
    - Low-level execution (limbs) is separated from high-level logic (bots) for security and flexibility.
- **Simplicity:**
    - Bots and XML launch files are simple by design, supporting robust orchestration and low failure rates.
- **Persistence & Communication:**
    - Bots persist in a synchronized runtime and communicate via a topic/subscriber model.
- **Intelligent Automation:**
    - Integration of LLMs enables context-aware, adaptive, and scalable automation.


  python lmos/main.py lmos/launch_files/rename_file.xml