<div align="center">
  <h1>🧬 Open Paper Machine</h1>
  <p><b>How an LLM Agent Wrote This Paper (And What That Means for Science)</b></p>
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![arXiv](https://img.shields.io/badge/arXiv-2603.XXXXX-b31b1b.svg)](https://arxiv.org/)
  [![Orchestrator](https://img.shields.io/badge/Orchestrator-T.B.%20Blask-purple)](https://github.com/ProfDrT)
  [![Reasoning](https://img.shields.io/badge/Reasoning-Claude_Opus_4.6-blue)](https://anthropic.com)
  [![Vision](https://img.shields.io/badge/Vision-Gemini_3.1_Pro-orange)](https://deepmind.google/technologies/gemini/)

  <i>A reference implementation of an observable, modifiable, and replicable AI research infrastructure.</i>
</div>

<br>

> *"This paper was produced by the system it describes. That is not a metaphor. Claude Opus 4.6 searched four academic databases, selected theoretical lenses, built a concept matrix, and drafted every section you are reading. The human orchestrator designed the task and approved the output. The human did not write the prose."* — **Introduction, Open Paper Machine**

---

## 📄 The Artifact
The flagship output of this repository is the complete, 9-page academic manuscript.  
**👉 [Read the Machine-Generated Paper (PDF)](latex/paper.pdf)**

## 🧠 The Orchestrator Paradigm
This project actively rejects the pervasive metaphor of the "AI assistant." Instead, it demonstrates the capacity of a modern autoregressive transformer (specifically **Claude Opus 4.6**) to function as a composable, autonomous research **agent**. 

When orchestrated through the **Model Context Protocol (MCP)** and given access to persistence layers (scratchpads, task lists) and computational tools, the model shifts from passive text-prediction to active scientific execution.

We propose the **Orchestrator Model** for academic authorship: The human who formulates the task, evaluates outputs, and accepts accountability is the author. The AI system is disclosed as the generative engine. The essential distinction is one of *accountability*, not *contribution*.

## 🏗️ The Four Architectural Layers
Agentic research behavior in the Open Paper Machine does not stem from a single algorithm; it *emerges* from the interaction of four critical layers. Remove any layer, and the system degrades.

1. **Transformer Substrate**: Affords extended reasoning across massive context windows and vast implicit factual knowledge.
2. **Alignment (RLHF)**: Provides epistemic dispositions, ensuring the model defaults to "helpful, honest, and harmless" behaviors.
3. **Constitutional AI (CAI)**: Embeds self-monitoring, capability awareness, and epistemic self-regulation directly into the generative process.
4. **Tool-Augmented Action (MCP)**: Grants the agent external reach—the ability to execute bash commands, query academic databases, read terminal errors, edit local files, and generate diagrams.

## 🔄 The Autonomous Research Pipeline
The Open Paper Machine executes five continuous, fully automated phases. This repository contains the raw, traceable artifacts produced at each step:

| Phase | Agent Role | Generated Artifact | Tools Invoked |
| :--- | :--- | :--- | :--- |
| **1. Reconnaissance** | Query formulation & literature gathering | [`literature_base.csv`](literature_base.csv) | arXiv & Semantic Scholar APIs |
| **2. Framing** | Theoretical lens synthesis & structuring | [`framing.md`](framing.md), [`paper_structure.md`](paper_structure.md) | File System, Bash |
| **3. Architecture** | Methodological grounding | [`concept_matrix.md`](concept_matrix.md) | Local Retrieval |
| **4. Production** | Full text drafting & citation mapping | [`draft.md`](draft.md) | Recursive LLM Calls |
| **5. Assembly** | LaTeX formatting & visualization | [`latex/paper.tex`](latex/paper.tex), [`latex/figures/`](latex/figures/) | Bash, pdflatex, PaperBanana (Gemini 3.1 Pro) |

## 🚀 Reproducibility & Local Execution

### Prerequisites
* Python 3.10+
* LaTeX distribution (`pdflatex`, `bibtex`)
* API Keys for Anthropic (Claude) and Google (Gemini)
* [PaperBanana](https://github.com/llmsresearch/paperbanana) Python Library

### 1. Generating the Publication-Ready Figures
The 7 conceptual diagrams featured in the paper are dynamically generated based on a strict, high-end design system (utilizing Deep Slate, Azure Blue, Teal, and Amber). Generation is handled by **Gemini 3.1 Pro** via the PaperBanana library.

```bash
# Export your Gemini API key
export GOOGLE_API_KEY="your-google-api-key"

# Execute the deterministic generation script
python regen_figures.py
```

### 2. Compiling the LaTeX Manuscript
The agent dynamically evaluates, writes, and compiles its own findings using standard LaTeX.

```bash
cd latex
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

---
*Developed as a sociotechnical intervention by Tobias-Benedikt Blask (Harz University of Applied Sciences). The machine wrote the words; the orchestrator designed the machine.*
