<div align="center">
  <h1>From Creator to Orchestrator</h1>
  <p><b>From Creator to Orchestrator: How an LLM Agent Wrote This Paper and What That Means for Science</b></p>

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![arXiv](https://img.shields.io/badge/arXiv-2603.XXXXX-b31b1b.svg)](https://arxiv.org/)
  [![Orchestrator](https://img.shields.io/badge/Orchestrator-T.B.%20Blask-purple)](https://github.com/ProfDrT)
  [![Agent](https://img.shields.io/badge/Agent-Claude_Opus_4.6-blue)](https://anthropic.com)
  [![Figures](https://img.shields.io/badge/Figures-PaperBanana_+_Gemini-orange)](https://github.com/llmsresearch/paperbanana)
  [![Template](https://img.shields.io/badge/Template-arxiv--style-lightgrey)](https://github.com/kourgeorge/arxiv-style)

  <i>A reference implementation of an observable, modifiable, and replicable AI research infrastructure.</i>
</div>

<br>

> *This paper was produced by the system it describes. Claude Opus 4.6 searched four academic databases, selected theoretical lenses, built a concept matrix, drafted every section, generated a self-review, and the human orchestrator designed the task, evaluated outputs, and accepted accountability.*

---

## The Artifact

The flagship output of this repository is the complete academic manuscript (19 pages, 62 citations, 7 figures) typeset in the [arxiv-style](https://github.com/kourgeorge/arxiv-style) template. All citations have been [verified against source content](verification_report.md).

**[Read the Machine-Generated Paper (PDF)](latex/paper.pdf)**

## The Orchestrator Paradigm

This project demonstrates the **creator-to-orchestrator transition**: when generative AI assumes execution-level tasks in knowledge work, the human role shifts from producing output to directing, evaluating, and taking accountability for AI-generated output. The human orchestrator retains judgment, domain expertise, and institutional responsibility. The AI system is disclosed as the generator.

We propose **accountability-based authorship**: the human who formulates the research, evaluates outputs, verifies claims, and accepts responsibility is the author. The AI is disclosed as the generative engine. The distinction is one of *accountability*, not *contribution*.

## Architecture

Agentic research behavior emerges from the interaction of four layers:

| Layer | Component | Function |
| :--- | :--- | :--- |
| 1 | **Transformer Substrate** | 200K+ token context, autoregressive coherence, implicit academic knowledge |
| 2 | **RLHF Alignment** | Helpfulness, honesty, harmlessness (HHH triad) |
| 3 | **Constitutional AI** | Self-critique, epistemic self-monitoring, uncertainty flagging |
| 4 | **MCP Tool Stack** | Academic APIs, file I/O, bash, web, PaperBanana figure generation |

## The Six-Phase Pipeline

The Open Paper Machine executes six autonomous phases. All intermediate artifacts are archived:

| Phase | Activities | Artifacts | Tools |
| :--- | :--- | :--- | :--- |
| **1. Reconnaissance** | Parallel DB searches, deduplication, ranking | [`literature_base.csv`](literature_base.csv), [`references.bib`](references.bib) | OpenAlex, CrossRef, arXiv, Semantic Scholar |
| **2. Framing** | Theory selection, gap formulation, RQ derivation | [`framing.md`](framing.md) | LLM reasoning |
| **3. Architecture** | Concept matrix, section design | [`concept_matrix.md`](concept_matrix.md), [`paper_structure.md`](paper_structure.md) | LLM + file I/O |
| **4. Production** | Full-text drafting, section by section | [`draft.md`](draft.md) | LLM generation + file I/O |
| **5. Assembly** | Figure generation, LaTeX compilation | [`figures/`](figures/), [`latex/paper.tex`](latex/paper.tex) | Bash + PaperBanana + LaTeX |
| **6. Self-Review** | Simulated peer review, critique generation | `review.md` | LLM reasoning |

The self-review in Phase 6 generates a structured peer review that the orchestrator uses to identify revision targets. This paper underwent this process: the self-review identified the circularity problem, under-theorization of emergent tasks, and asymmetries in the comparative analysis --- all subsequently addressed.

## Citation Verification

All 62 citations were systematically verified using the plugin's [verification-engine](https://github.com/ProfDrT/open-paper-machine). The engine fetched source abstracts via academic APIs (OpenAlex, CrossRef, Semantic Scholar) and full text for open-access papers (arXiv), then compared each attributed claim against actual source content.

| Classification | Count | % |
| :--- | :--- | :--- |
| VERIFIED | 25 | 52% |
| PLAUSIBLE | 17 | 35% |
| MISMATCH | 1 | 2% |
| UNVERIFIABLE | 5 | 10% |
| NOT FOUND | 0 | 0% |

**0 fabricated references.** The single mismatch (Lincoln & Guba quality criteria terminology) was corrected. 5 sources are unverifiable (books/paywalled content). Full results: [`verification_report.md`](verification_report.md).

## Figures

All 7 publication figures are generated by [PaperBanana](https://github.com/llmsresearch/paperbanana) (Gemini backend) with iterative critic refinement:

| Figure | Description | File |
| :--- | :--- | :--- |
| Fig. 1 | Four-layer architecture stack | [`fig1_architecture_layers.png`](figures/fig1_architecture_layers.png) |
| Fig. 2 | Six-phase pipeline | [`fig2_pipeline_phases.png`](figures/fig2_pipeline_phases.png) |
| Fig. 3 | Task redistribution (skill shift) | [`fig15_skill_shift.png`](figures/fig15_skill_shift.png) |
| Fig. 4 | Epistemic boundaries | [`fig14_epistemic_boundaries.png`](figures/fig14_epistemic_boundaries.png) |
| Fig. 5 | Sociotechnical redesign | [`fig8_sociotechnical_redesign.png`](figures/fig8_sociotechnical_redesign.png) |
| Fig. 6 | Orchestrator authorship model | [`fig10_orchestrator_model.png`](figures/fig10_orchestrator_model.png) |
| Fig. 7 | Capability matrix | [`fig6_capability_matrix.png`](figures/fig6_capability_matrix.png) |

## Setup & Reproducibility

### Prerequisites

* Python 3.10+
* LaTeX distribution (`pdflatex`, `bibtex`)
* A Google Gemini API key (free tier available)
* [Claude Code](https://claude.ai/claude-code) with the Open Academic Paper Machine plugin (for the full pipeline)

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/ProfDrT/From_Creator_to_Orchestrator.git
cd From_Creator_to_Orchestrator

# Install PaperBanana (figure generation engine)
pip install paperbanana[mcp,google]
```

### 2. Configure Your API Key

PaperBanana uses Google Gemini for figure generation. You need a free API key from [Google AI Studio](https://aistudio.google.com/apikey).

```bash
# Option A: Create a .env file in the project root (recommended)
echo 'GOOGLE_API_KEY="your-google-api-key-here"' > .env

# Option B: Export directly in your shell
export GOOGLE_API_KEY="your-google-api-key-here"
```

> **Note:** The `.env` file is listed in `.gitignore` and will not be committed. Never commit API keys to version control.

### 3. Generate Figures

```bash
# Generate all 7 paper figures via PaperBanana
python regen_figures.py
```

Each figure goes through PaperBanana's multi-agent pipeline (Planner → Stylist → Visualizer → Critic) with iterative refinement. Expect ~1 minute per figure.

### 4. Compile the Manuscript

The paper uses the [arxiv-style](https://github.com/kourgeorge/arxiv-style) template (`arxiv.sty` is included in `latex/`).

```bash
cd latex
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

### 5. Run the Full Pipeline (via Claude Code)

To reproduce the entire paper from scratch using the autonomous agent, install the [Open Academic Paper Machine](https://github.com/ProfDrT/open-paper-machine) plugin:

```bash
claude
# Inside Claude Code:
/write-paper "From Creator to Orchestrator"
```

## Repository Structure

```
.
├── latex/
│   ├── paper.tex              # Complete LaTeX manuscript (19 pages)
│   ├── arxiv.sty              # arxiv-style template
│   ├── orcid.pdf              # ORCID icon for author block
│   ├── paper.pdf              # Compiled PDF
│   └── figures/               # Figures (copy used by LaTeX)
├── figures/                    # 7 PaperBanana-generated figures (source)
├── references.bib              # 62 BibTeX entries (verified)
├── verification_report.md      # Citation verification results
├── draft.md                    # Markdown source draft
├── framing.md                  # Theory selection & research questions
├── concept_matrix.md           # Webster & Watson concept matrix
├── paper_structure.md          # Section architecture
├── literature_base.csv         # Retrieved literature database
├── regen_figures.py            # Figure regeneration script
└── .env                        # API keys (not committed)
```

## Citation

```bibtex
@article{blask2026creator,
  title={From Creator to Orchestrator: How an LLM Agent Wrote This Paper
         and What That Means for Science},
  author={Blask, Tobias-Benedikt},
  journal={arXiv preprint},
  year={2026},
  note={Paper generated by Claude Opus 4.6 (Anthropic PBC) under
        human orchestration. Repository:
        \url{https://github.com/ProfDrT/From_Creator_to_Orchestrator}}
}
```

---
*Developed as a sociotechnical intervention by Tobias-Benedikt Blask (Harz University of Applied Sciences). The machine wrote the words; the orchestrator designed the machine.*
