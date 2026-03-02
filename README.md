<div align="center">
  <h1>From Creator to Orchestrator</h1>
  <p><b>From Creator to Orchestrator? How an LLM Agent Wrote This Paper and What That Means for Science</b></p>

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![arXiv](https://img.shields.io/badge/arXiv-2603.XXXXX-b31b1b.svg)](https://arxiv.org/)
  [![Orchestrator](https://img.shields.io/badge/Orchestrator-T.B.%20Blask%20%26%20B.%20Funk-purple)](https://github.com/TobiasBlask)
  [![Agent](https://img.shields.io/badge/Agent-Claude_Opus_4.6-blue)](https://anthropic.com)
  [![Figures](https://img.shields.io/badge/Figures-PaperBanana_+_Gemini-orange)](https://github.com/llmsresearch/paperbanana)
  [![Template](https://img.shields.io/badge/Template-arxiv--style-lightgrey)](https://github.com/kourgeorge/arxiv-style)

  <i>A reference implementation of an observable, modifiable, and replicable AI research infrastructure.</i>
</div>

<br>

> *This paper was produced by the system it describes. Claude Opus 4.6 searched four academic databases, selected theoretical lenses, built a concept matrix, drafted every section, and generated figures. The human orchestrators designed the research, evaluated outputs, and accepted accountability.*

---

## The Artifact

The flagship output of this repository is the complete academic manuscript (18 pages, 46 citations, 2 figures) typeset in the [arxiv-style](https://github.com/kourgeorge/arxiv-style) template. All citations have been [verified against source content](verification_report.md).

**[Read the Machine-Generated Paper (PDF)](latex/paper.pdf)**

## The Orchestrator Paradigm

This project demonstrates the **creator-to-orchestrator transition**: when generative AI assumes execution-level tasks in knowledge work, the human role shifts from producing output to directing, evaluating, and taking accountability for AI-generated output. The human orchestrator retains judgment, domain expertise, and institutional responsibility. The AI system is disclosed as the generator.

We propose **accountability-based authorship**: the human who formulates the research, evaluates outputs, verifies claims, and accepts responsibility is the author. The AI is disclosed as the generative engine. The distinction is one of *accountability*, not *contribution*.

## Paper Structure

| Section | Title | Content |
| :--- | :--- | :--- |
| 1 | Introduction | Research gaps, two RQs, contributions |
| 2 | Technical Foundations | Transformers, alignment, MCP, hallucination, related systems |
| 3 | Theoretical Lenses | Distributed cognition, sociotechnical systems/MLP, task formulation |
| 4 | Methodology | Design science with reflexive twist, pipeline as data |
| 5 | The Technology Stack | Four-layer architecture, MCP tool stack |
| 6 | Capabilities and Failure Modes | What worked, what failed, evaluation |
| 7 | From Creator to Orchestrator | Task redistribution, authorship, peer review, evolving role |
| 8 | Conclusion | Summary, CRediT guidelines, the hard problem |

## Architecture

Agentic research behavior emerges from the interaction of four layers:

| Layer | Component | Function |
| :--- | :--- | :--- |
| 1 | **Transformer Base** | 200K+ token context, autoregressive coherence, implicit academic knowledge |
| 2 | **RLHF Alignment** | Helpfulness, honesty, harmlessness (HHH triad) |
| 3 | **Constitutional AI** | Self-critique, epistemic self-monitoring, uncertainty flagging |
| 4 | **MCP Tool Stack** | Academic APIs, file I/O, bash, web, PaperBanana figure generation |

## The Six-Phase Pipeline

The Open Paper Machine executes six autonomous phases. All intermediate artifacts are archived:

| Phase | Activities | Artifacts | Tools |
| :--- | :--- | :--- | :--- |
| **1. Reconnaissance** | Parallel DB searches, deduplication, ranking | [`literature_base.csv`](literature_base.csv), [`references.bib`](references.bib) | OpenAlex, CrossRef, arXiv, Semantic Scholar |
| **2. Framing** | Theory selection, gap formulation, RQ derivation | [`framing.md`](framing.md) | LLM reasoning |
| **3. Structure** | Concept matrix, section design | [`concept_matrix.md`](concept_matrix.md), [`paper_structure.md`](paper_structure.md) | LLM + file I/O |
| **4. Production** | Full-text drafting, section by section | [`draft.md`](draft.md) | LLM generation + file I/O |
| **5. Assembly** | Figure generation, LaTeX compilation | [`figures/`](figures/), [`latex/paper.tex`](latex/paper.tex) | Bash + PaperBanana + LaTeX |
| **6. Self-Review** | Simulated peer review, critique generation | `review.md` | LLM reasoning |

The self-review in Phase 6 generates a structured peer review that the orchestrator uses to identify revision targets. This paper underwent this process: the self-review identified the circularity problem, under-theorization of emergent tasks, and asymmetries in the comparative analysis --- all subsequently addressed.

## Citation Verification

All citations were systematically verified using the plugin's [verification-engine](https://github.com/TobiasBlask/open-paper-machine). The engine fetched source abstracts via academic APIs (OpenAlex, CrossRef, Semantic Scholar) and full text for open-access papers (arXiv), then compared each attributed claim against actual source content.

| Classification | Count | % |
| :--- | :--- | :--- |
| VERIFIED | 25 | 52% |
| PLAUSIBLE | 17 | 35% |
| MISMATCH | 1 | 2% |
| UNVERIFIABLE | 5 | 10% |
| NOT FOUND | 0 | 0% |

**0 fabricated references.** The single mismatch (Lincoln & Guba quality criteria terminology) was corrected. 5 sources are unverifiable (books/paywalled content). Full results: [`verification_report.md`](verification_report.md).

## Figures

All publication figures are generated by [PaperBanana](https://github.com/llmsresearch/paperbanana) (Gemini backend) with iterative critic refinement:

| Figure | Description | File |
| :--- | :--- | :--- |
| Fig. 1 | Six-phase pipeline with human quality gates | [`fig2_pipeline_phases.png`](latex/figures/fig2_pipeline_phases.png) |
| Fig. 2 | Creator-to-orchestrator transition model | [`fig_creator_to_orchestrator.png`](latex/figures/fig_creator_to_orchestrator.png) |

## Setup & Reproducibility

### Prerequisites

* Python 3.10+
* LaTeX distribution (`pdflatex`, `bibtex`)
* A Google Gemini API key (free tier available)
* [Claude Code](https://claude.ai/claude-code) with the Open Academic Paper Machine plugin (for the full pipeline)

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/TobiasBlask/From_Creator_to_Orchestrator.git
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

### 3. Compile the Manuscript

The paper uses the [arxiv-style](https://github.com/kourgeorge/arxiv-style) template (`arxiv.sty` is included in `latex/`).

```bash
cd latex
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

### 4. Run the Full Pipeline (via Claude Code)

To reproduce the entire paper from scratch using the autonomous agent, install the [Open Academic Paper Machine](https://github.com/TobiasBlask/open-paper-machine) plugin:

```bash
claude
# Inside Claude Code:
/write-paper "From Creator to Orchestrator"
```

## Repository Structure

```
.
├── latex/
│   ├── paper.tex              # Complete LaTeX manuscript (18 pages)
│   ├── appendix.tex           # Plugin architecture & orchestration dialogue
│   ├── references.bib         # Bibliography (46 entries)
│   ├── arxiv.sty              # arxiv-style template
│   ├── paper.pdf              # Compiled PDF
│   └── figures/               # 2 PaperBanana-generated figures
├── figures/                    # Figure sources
├── references.bib              # BibTeX entries (verified)
├── verification_report.md      # Citation verification results
├── draft.md                    # Markdown source draft
├── framing.md                  # Theory selection & research questions
├── concept_matrix.md           # Webster & Watson concept matrix
├── paper_structure.md          # Section architecture
├── literature_base.csv         # Retrieved literature database
└── .env                        # API keys (not committed)
```

## Citation

```bibtex
@article{blask2026creator,
  title={From Creator to Orchestrator? How an LLM Agent Wrote This Paper
         and What That Means for Science},
  author={Blask, Tobias-Benedikt and Funk, Burkhardt},
  journal={arXiv preprint},
  year={2026},
  note={Paper generated by Claude Opus 4.6 (Anthropic PBC) under
        human orchestration. Repository:
        \url{https://github.com/TobiasBlask/From_Creator_to_Orchestrator}}
}
```

---
*Developed as a sociotechnical intervention by Tobias-Benedikt Blask (Harz University of Applied Sciences) and Burkhardt Funk (Leuphana University of L&uuml;neburg). The machine wrote the words; the orchestrators designed the machine.*
