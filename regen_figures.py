"""
Regenerate all 16 figures for:
  "Open Paper Machine: How an LLM Agent Wrote This Paper"
using PaperBanana Python API + Gemini backend.
"""

import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv

# ── Load API key ──────────────────────────────────────────────────────────────
# Try several known locations for the .env
for env_path in [
    Path(__file__).parent / ".env",
    Path("/Users/tobias-benediktblask/PaperBanana/.env"),
    Path("/Users/tobias-benediktblask/2026_Open_Research_Machine/academic-research-plugin/paper/latex/.env"),
]:
    if env_path.exists():
        load_dotenv(env_path)
        break

# Fallback: raise error if not found in any .env
if not os.environ.get("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY environment variable not set. Please set it or add it to a .env file.")

from paperbanana import PaperBananaPipeline, GenerationInput, DiagramType
from paperbanana.core.config import Settings

OUTPUT_DIR = Path(__file__).parent / "figures"
OUTPUT_DIR.mkdir(exist_ok=True)

# ── Shared design system ──────────────────────────────────────────────────────
DS = """
GLOBAL DESIGN RULES (apply to every element):
- Canvas: Wide landscape (16:9). Background: Pale, ultra-clean off-white background (#F8FAFC) for a modern aesthetic.
- Font: Inter, Roboto, or Helvetica Neue. Typography must be crisp and highly readable.
- Palette: Primary text is Deep Slate (#0F172A). Accent colors should feel like a premium scientific journal (e.g., Azure Blue #2563EB, Teal #0D9488, and warm Amber #D97706 for alerts).
- Nodes and Containers: Use subtle soft, diffuse drop shadows on nodes to give depth. Backgrounds of nodes can be #FFFFFF or have a slight premium pastel tint depending on category. 
- Borders: Crisp, thin borders (#CBD5E1 or #94A3B8) at 1px or 1.5px width. Elegant rounded corners (e.g. 8px) on boxes.
- Arrows: Smooth curving or perfectly orthogonal with neat, sharp arrowheads. Use #475569 or translucent primary colors for flows.
- Aesthetics: High-end publication ready. Visually stunning, clear hierarchy, avoid clutter. Perfect alignment.
- Labels: Ensure all text is fully visible, not truncated, with ample whitespace inside boxes.
"""

FIGURES = [

    # ── fig13: Hero overview ─────────────────────────────────────────────────
    {
        "filename": "fig13_open_paper_machine_overview.png",
        "caption": "The Open Paper Machine — autonomous LLM research agent overview.",
        "context": DS + """
DIAGRAM TYPE: Hero architecture overview — 3 horizontal zones separated by dividers.

TOP ZONE — "Orchestrator" (light blue background):
  One box: "Human Orchestrator (Blask)" — role labels below: "Task Design · Output Approval · Accountability"
  Arrow pointing DOWN labeled "Research Brief"

MIDDLE ZONE — "Open Paper Machine Agent" (Deep Blue filled, white text):
  Label: "Open Paper Machine · Claude Sonnet 4.6 + MCP"
  Inside: 5 horizontally connected phase boxes (white fill, blue border):
    [① Reconnaissance] → [② Framing] → [③ Architecture] → [④ Production] → [⑤ Assembly]
  Between each phase: small diamond labeled "✓ Checkpoint"
  Arrow pointing DOWN labeled "Tool Calls"

BOTTOM ZONE — "Infrastructure" (light grey background), split into two rows:
  Row A (APIs): 4 equal boxes: "Semantic Scholar" | "OpenAlex" | "CrossRef" | "arXiv"
  Row B (Tools): 3 boxes: "File I/O (read/write/grep)" | "Bash Execution" | "PaperBanana (figures)"

CRITICAL: Middle zone must be visually dominant. All 5 phase boxes clearly connected left-to-right.
""",
    },

    # ── fig7: Transformer attention ──────────────────────────────────────────
    {
        "filename": "fig7_transformer_attention.png",
        "caption": "Transformer self-attention: every token attends to every other token in parallel.",
        "context": DS + """
DIAGRAM TYPE: Two-panel technical diagram.

PANEL LEFT — "Self-Attention Mechanism":
  3 input token boxes at bottom, labeled "Token₁", "Token₂", "Token₃".
  From each token, arrows fan up to a central "Attention Matrix" grid (3×3, showing weights like 0.7, 0.2, 0.1).
  From the matrix, 3 output vectors emerge upward, labeled "Contextual Repr₁", "Repr₂", "Repr₃".
  Key insight label (italic): "All tokens processed in parallel — no recurrence"

PANEL RIGHT — "Scale → Emergence":
  A vertical bar chart with 3 bars (x-axis: model size in parameters):
    "1B params": short grey bar, label "Basic completion"
    "13B params": medium grey bar, label "Few-shot learning"
    "175B+ params": tall Deep Blue bar, label "Emergent research agency"
  Annotation arrow on tallest bar: "GPT-3 / Claude scale"
  X-axis: "Model Scale (parameters)" Y-axis: "Emergent Capability Level"

CRITICAL: The attention matrix must look like a real grid with visible numerical weights.
""",
    },

    # ── fig12: RLHF pipeline ─────────────────────────────────────────────────
    {
        "filename": "fig12_rlhf_pipeline.png",
        "caption": "RLHF pipeline: SFT → reward model → PPO policy optimisation producing the HHH triad.",
        "context": DS + """
DIAGRAM TYPE: Horizontal 3-stage pipeline with output.

STAGE 1 (leftmost box, Deep Blue border):
  Title: "Stage 1: Supervised Fine-Tuning (SFT)"
  Content: "Human demonstrations → fine-tune base model"
  Small icon: person writing

STAGE 2 (middle box, Deep Blue border):
  Title: "Stage 2: Reward Model Training"
  Content: "Human pairwise comparisons → reward signal"
  Small icon: two responses with ▲ / ▼

STAGE 3 (rightmost box, Deep Blue border):
  Title: "Stage 3: PPO Policy Optimisation"
  Content: "RL loop: maximise reward signal"
  Small icon: circular arrows (loop)

Horizontal Deep Blue arrows connecting Stage 1 → 2 → 3.

OUTPUT (far right, separated by dashed line):
  Three stacked boxes (green border), labeled:
    "✓ Helpfulness"
    "✓ Honesty"
    "✓ Harmlessness"
  Group label above: "HHH Triad"

Research implication note (italic, bottom): "Honesty disposition → critical constraint against hallucination"

CRITICAL: The three HHH output boxes must be visually grouped and clearly distinct from the pipeline stages.
""",
    },

    # ── fig5: Constitutional AI ──────────────────────────────────────────────
    {
        "filename": "fig5_constitutional_ai.png",
        "caption": "Constitutional AI training loop: generate → self-critique → revise → RLAIF.",
        "context": DS + """
DIAGRAM TYPE: Circular process diagram with 4 labelled steps + centre label.

CENTRE CIRCLE (Deep Blue fill, white text): "Constitutional AI\nTraining Loop"

4 process steps arranged clockwise around the centre (each is a rounded rectangle):
  TOP: "① Generate\nInitial response"
  RIGHT: "② Self-Critique\nagainst Constitution principles"
  BOTTOM: "③ Revise\nImproved response"
  LEFT: "④ RLAIF Training\nTrain on revised outputs"

Clockwise arrows between all 4 steps (Deep Blue).

CONSTITUTION BOX (top-right, separate, dashed border):
  Title: "The Constitution (examples)"
  Bullet list:
    "• Be honest about uncertainty"
    "• Avoid fabricating citations"
    "• Acknowledge knowledge limits"
    "• Flag claims needing verification"

Arrow from CONSTITUTION BOX pointing to Step ② "Self-Critique".

OUTCOME label (bottom-right, italic): "Result: Self-monitoring epistemic behaviours"

CRITICAL: The circular flow must be clearly clockwise. The constitution box must look like a separate document.
""",
    },

    # ── fig4: Distributed cognition ──────────────────────────────────────────
    {
        "filename": "fig4_distributed_cognition.png",
        "caption": "Distributed cognition: research cognition spans LLM agent, human, databases, file system, and institutions.",
        "context": DS + """
DIAGRAM TYPE: Hub-and-spoke cognitive system diagram.

CENTRE HUB (large Deep Blue circle, white text):
  "Open Paper Machine\n(Cognitive Artifact)"

5 SPOKES radiating outward (Deep Blue lines), each ending in a box:
  TOP: "Human Orchestrator\n(Direction · Judgment · Accountability)"
  TOP-RIGHT: "Academic Databases\n(Semantic Scholar · OpenAlex · CrossRef · arXiv)"
  RIGHT: "File System\n(Persistent artifacts across phases)"
  BOTTOM-RIGHT: "Institutional Context\n(Peer review · Publication norms · Citation standards)"
  LEFT: "LLM Parameters\n(Implicit knowledge · Emergent capabilities)"

DISTRIBUTED COGNITION label (bold, at top): "Cognition is distributed — not confined to any single component"

Dashed oval boundary enclosing all components, labeled: "Extended Cognitive System"

CRITICAL: The hub must be clearly central. All 5 spoke-end boxes must be readable.
""",
    },

    # ── fig2: Pipeline phases ────────────────────────────────────────────────
    {
        "filename": "fig2_pipeline_phases.png",
        "caption": "Five-phase Open Paper Machine pipeline: Reconnaissance → Framing → Architecture → Production → Assembly.",
        "context": DS + """
DIAGRAM TYPE: Horizontal 5-phase pipeline with artifact row below.

TOP ROW (5 equal phase boxes, Deep Blue border, connected left-to-right with thick arrows):
  [① Reconnaissance] → [② Framing] → [③ Architecture] → [④ Production] → [⑤ Assembly]
  Between each phase: small diamond (Deep Blue fill, white text) labeled "Checkpoint ✓"

BOTTOM ROW (5 artifact boxes, each directly below its phase, connected by short downward Slate arrows):
  Below ①: "literature_base.csv\nreferences.bib\n35 papers"
  Below ②: "framing.md\n(Theory + RQs)"
  Below ③: "concept_matrix.md\npaper_structure.md"
  Below ④: "draft.md\n(~8,600 words)"
  Below ⑤: "paper.pdf\n+ status_report.md"

Artifact box style: light grey fill, dashed border, document icon top-left.

CRITICAL: Checkpoint diamonds sit between phase boxes on the same horizontal line, not above or below.
""",
    },

    # ── fig11: Concept matrix ────────────────────────────────────────────────
    {
        "filename": "fig11_concept_matrix.png",
        "caption": "Concept matrix (Webster & Watson): 34 papers × 8 thematic dimensions.",
        "context": DS + """
DIAGRAM TYPE: Grid / matrix table (Webster & Watson style).

STRUCTURE: 6-row × 9-column matrix table (5 data rows + header).

COLUMN HEADERS (Deep Blue fill, white text, bold):
  "Paper" | "LLM Agency" | "Multi-Agent" | "HITL" | "Tool Use" | "Alignment" | "Research WF" | "Architecture" | "Sociotech."

DATA ROWS (alternating white and very-light-grey fill):
  Row 1: "Vaswani et al. (2017)" | ● | ○ | ○ | ○ | ○ | ○ | ● | ○
  Row 2: "Ouyang et al. (2022)" | ● | ○ | ● | ○ | ● | ○ | ○ | ○
  Row 3: "Bai et al. (2022)" | ● | ○ | ● | ○ | ● | ○ | ○ | ○
  Row 4: "Wang et al. (2024)" | ● | ● | ● | ● | ○ | ● | ● | ○
  Row 5: "Yamada et al. (2025)" | ● | ○ | ○ | ● | ○ | ● | ● | ●

LEGEND (below table): "● = Addressed · ○ = Not addressed"
FOOTER ROW (bold, Deep Blue border): "Column Totals:" | "5" | "1" | "3" | "2" | "2" | "2" | "3" | "1"

TITLE ABOVE TABLE: "Concept Matrix — 34 Papers × 8 Dimensions (Representative Excerpt)"

CRITICAL: ● = solid Deep Blue filled circle. ○ = hollow grey circle. Column headers must be readable.
""",
    },

    # ── fig1: Architecture layers ────────────────────────────────────────────
    {
        "filename": "fig1_architecture_layers.png",
        "caption": "Four-layer architecture: transformer substrate → RLHF → Constitutional AI → MCP tool stack.",
        "context": DS + """
DIAGRAM TYPE: Vertical 4-layer stack diagram with emergence arrow.

LAYER 1 — BOTTOM (foundation): "Transformer Substrate"
  Box: light grey fill, label bold "Layer 1: Transformer Substrate"
  Sub-labels: "200K token context · Autoregressive coherence · Implicit knowledge"

LAYER 2: "RLHF Alignment"
  Box: slightly darker grey fill, label bold "Layer 2: RLHF Alignment"
  Sub-labels: "Helpfulness · Honesty · Harmlessness (HHH triad)"

LAYER 3: "Constitutional AI"
  Box: light blue fill, label bold "Layer 3: Constitutional AI (CAI)"
  Sub-labels: "Self-critique · Epistemic self-monitoring · [TODO] / [CITE] markers"

LAYER 4 — TOP: "MCP Tool Stack"
  Box: Deep Blue fill, white text, label bold "Layer 4: MCP Tool Stack"
  Sub-labels: "Academic APIs · File I/O · Bash · PaperBanana · Web fetch"

Upward arrow on RIGHT SIDE spanning all 4 layers, labeled:
  "Research Agency EMERGES from interaction of all four layers"

CRITICAL: Layers must be clearly stacked bottom-to-top, with the MCP layer dominant at top.
""",
    },

    # ── fig3: ReAct loop ─────────────────────────────────────────────────────
    {
        "filename": "fig3_react_loop.png",
        "caption": "ReAct agent loop: Reason–Act–Observe cycles for adaptive goal-directed behaviour.",
        "context": DS + """
DIAGRAM TYPE: Circular 3-step loop with example annotation panel.

MAIN LOOP (centre) — 3 nodes connected clockwise by Deep Blue arrows:
  LEFT NODE (rounded rectangle, Deep Blue fill, white text): "REASON\nAnalyse state, plan next action"
  TOP NODE (rounded rectangle, Deep Blue fill, white text): "ACT\nExecute tool call (API / file / bash)"
  RIGHT NODE (rounded rectangle, Deep Blue fill, white text): "OBSERVE\nProcess result, update context"

Clockwise arrows between all 3 nodes labeled:
  Reason→Act: "tool call"
  Act→Observe: "result"
  Observe→Reason: "updated context"

TERMINATION CONDITION (exit arrow from REASON, pointing RIGHT):
  Dashed arrow labeled "Goal achieved?" → box "EXIT: Deliver output"

EXAMPLE PANEL (right side, dashed border, light background):
  Title: "Phase 1 Example (~12 cycles)"
  Bullet list:
    "• Reason: 'Query Semantic Scholar for LLM agents'"
    "• Act: search_papers(query=..., db='semantic_scholar')"
    "• Observe: 0 results — API failure"
    "• Reason: 'Try OpenAlex instead'"
    "• Act: search_papers(query=..., db='openalex')"
    "• Observe: 12 papers returned"

CRITICAL: The 3-node circular loop must be clearly visible. Arrows must show directionality.
""",
    },

    # ── fig6: Capability matrix ──────────────────────────────────────────────
    {
        "filename": "fig6_capability_matrix.png",
        "caption": "Capability matrix: demonstrated capabilities, partial capabilities, and fundamental limitations.",
        "context": DS + """
DIAGRAM TYPE: 3-column + header table (capability assessment matrix).

HEADER ROW (Deep Blue fill, white text, bold):
  "Research Task" | "✓ Demonstrated" | "⚠ Limited" | "✗ Fundamental Limit"

DATA ROWS (5 rows, alternating white/light-grey):
  Row 1: "Literature Reconnaissance"
         | "6-DB parallel search, 35 papers, DOI dedup"
         | "No methodological quality scoring"
         | "Paywalled content inaccessible"

  Row 2: "Theoretical Framing"
         | "Theory selection, gap formulation, RQ derivation"
         | "Cannot invent new theoretical vocabulary"
         | "Bounded by training-data theory space"

  Row 3: "Academic Writing"
         | "8,600 words, 7 sections, APA conventions"
         | "Defaults to safe/hedged formulations"
         | "No autobiographical grounding"

  Row 4: "Citation Integration"
         | "Cites retrieved literature accurately"
         | "Accuracy depends on retrieved base"
         | "Parametric citations carry hallucination risk"

  Row 5: "Empirical Research"
         | "Archival synthesis of existing work"
         | "Can synthesise researcher-provided data"
         | "Cannot conduct experiments or interviews"

COLUMN STYLE: ✓ column = light green background. ⚠ column = light yellow. ✗ column = light red.
CRITICAL: The three shaded columns must be clearly readable and colour-coded.
""",
    },

    # ── fig9: System comparison ──────────────────────────────────────────────
    {
        "filename": "fig9_system_comparison.png",
        "caption": "AI research system comparison: Coscientist, AI Scientist-v2, SciAgents, Open Paper Machine.",
        "context": DS + """
DIAGRAM TYPE: Comparison matrix table (4 systems × 5 dimensions).

HEADER ROW (Deep Blue fill, white text, bold):
  "System" | "Pipeline Scope" | "Empirical Exec." | "Self-Analysis" | "IS Grounding" | "Domain"

DATA ROWS:
  Row 1: "Coscientist\n(Boiko et al., 2023)"
         | "Narrow (reactions)"
         | "✓ Yes (experiments)"
         | "✗ No"
         | "✗ No"
         | "Chemistry"

  Row 2: "AI Scientist-v2\n(Yamada et al., 2025)"
         | "Full paper"
         | "✓ Yes (ML exp.)"
         | "✗ No"
         | "✗ No"
         | "ML only"

  Row 3: "SciAgents\n(Ghafarollahi et al., 2024)"
         | "Hypothesis gen."
         | "✗ No"
         | "✗ No"
         | "✗ No"
         | "Materials sci."

  Row 4 (highlight with Deep Blue left border): "Open Paper Machine\n(This work)"
         | "Full paper"
         | "✗ No (archival)"
         | "✓ Yes (reflexive)"
         | "✓ Yes"
         | "General / IS"

CAPTION BELOW: "Open Paper Machine's distinctive contribution: full-pipeline generality + reflexive self-analysis + IS theoretical grounding"

CRITICAL: Row 4 (Open Paper Machine) must be visually highlighted to show it's the subject of this paper.
""",
    },

    # ── fig14: Epistemic boundaries ──────────────────────────────────────────
    {
        "filename": "fig14_epistemic_boundaries.png",
        "caption": "Four fundamental epistemic boundaries of the Open Paper Machine.",
        "context": DS + """
DIAGRAM TYPE: 2×2 grid of limit cards (equal quadrants).

GRID TITLE (top, bold): "Fundamental Epistemic Boundaries"

TOP-LEFT QUADRANT (light red background):
  Title (bold, red): "⚠ Training Cutoff"
  Body: "Parametric knowledge frozen at training time.\nPost-cutoff developments invisible to base model.\nPartially compensated by live API retrieval."

TOP-RIGHT QUADRANT (light orange background):
  Title (bold, orange): "⚠ Hallucination Risk"
  Body: "LLMs generate plausible but false content.\nFabricated citations with realistic metadata.\nAll citations require human verification."

BOTTOM-LEFT QUADRANT (light yellow background):
  Title (bold, gold): "⚠ Overconfident Synthesis"
  Body: "May elide contradictions & null results.\nConfidence calibration imperfect.\nAggregated claims may misrepresent sources."

BOTTOM-RIGHT QUADRANT (light purple background):
  Title (bold, purple): "⚠ No Primary Data"
  Body: "Cannot conduct experiments, surveys, or interviews.\nCannot access proprietary or paywalled data.\nResearch is fundamentally archival & synthetic."

CRITICAL: All 4 quadrants must be equal size. Titles must be clearly readable with colour coded headers.
""",
    },

    # ── fig8: Sociotechnical redesign ────────────────────────────────────────
    {
        "filename": "fig8_sociotechnical_redesign.png",
        "caption": "Sociotechnical redesign: AI agents reconfigure roles, norms, and accountability structures.",
        "context": DS + """
DIAGRAM TYPE: Before/After comparison with transition arrow.

LEFT PANEL — "Traditional Research Workflow":
  Sequential vertical flow of boxes (grey, connected by downward arrows):
    "Literature Review\n(2–4 weeks)"
    "Theoretical Framing\n(1–2 weeks)"
    "Research Design\n(1–2 weeks)"
    "Data Collection\n(months–years)"
    "Writing\n(2–3 months)"
  TOTAL LABEL below: "~3–6 months per paper"

CENTRE: Large horizontal arrow labeled "Sociotechnical\nIntervention\n(AI Research Agent)"
  Below arrow: "Not just 'faster' — structurally different"

RIGHT PANEL — "AI-Augmented Research Workflow":
  Two zones separated by a horizontal dashed line:
  ZONE A (AI executes, light blue background):
    Horizontal flow: [Reconnaissance ~3min] → [Framing ~1.5min] → [Architecture ~2min] → [Draft ~20min]
    Label: "AI-Executed: 40 minutes total"
  ZONE B (Human-led, white background):
    "[Checkpoint Review × 5]" → "[Data Collection]" → "[Validation & Editing]"
    Label: "Human-Led: Judgment & Accountability"

OUTCOME BOX (bottom right, Deep Blue border): "Skill shift: from synthesis mechanics → critical evaluation"

CRITICAL: The before/after contrast must be visually clear. The timeline compression must be legible.
""",
    },

    # ── fig10: Orchestrator model ────────────────────────────────────────────
    {
        "filename": "fig10_orchestrator_model.png",
        "caption": "Orchestrator model of AI-assisted authorship: human accountability, AI as disclosed generator.",
        "context": DS + """
DIAGRAM TYPE: Role-responsibility diagram with accountability flow.

TWO MAIN ACTORS (left-right layout):

LEFT BOX — "Human Orchestrator" (Deep Blue border, prominent):
  Title: "Human Orchestrator\n(Tobias-Benedikt Blask)"
  Responsibilities (bullet list):
    "• Formulates research task"
    "• Approves/redirects at checkpoints"
    "• Accepts full accountability"
    "• Signs the paper"
  Label below: "= AUTHOR (accountable)"

RIGHT BOX — "AI System" (grey border, secondary):
  Title: "Claude Sonnet 4.6\n(Anthropic PBC)"
  Responsibilities (bullet list):
    "• Executes all 5 pipeline phases"
    "• Generates all prose and citations"
    "• Self-monitors via CAI"
    "• Cannot accept accountability"
  Label below: "= GENERATOR (disclosed)"

CENTRE ACCOUNTABILITY FLOW (between the two boxes):
  "Research Brief" arrow → (Human to AI)
  "Draft output" arrow ← (AI to Human)
  "Review & approve" arrow → (Human evaluates)

ANALOGY NOTE (bottom): "Analogy: Research assistant who drafts; PI who signs — contribution ≠ authorship"

CRITICAL: The distinction between AUTHOR and GENERATOR must be visually unmistakable.
""",
    },

    # ── fig15: Skill shift ───────────────────────────────────────────────────
    {
        "filename": "fig15_skill_shift.png",
        "caption": "Skill shift: declining mechanical competencies, rising evaluative and directive competencies.",
        "context": DS + """
DIAGRAM TYPE: Two-column skills comparison with value direction arrows.

HEADER (bold, centred): "The AI-Driven Skill Shift in Academic Research"

LEFT COLUMN — "Declining Value" (light red background, ↓ arrow top):
  Title: "↓ Mechanical Competencies"
  List (grey text, strikethrough style):
    "Boolean search string construction"
    "Manual abstract screening (200+ papers)"
    "Literature review drafting from scratch"
    "Citation formatting & management"
    "LaTeX compilation and layout"

RIGHT COLUMN — "Rising Value" (light green background, ↑ arrow top):
  Title: "↑ Critical & Directive Competencies"
  List (Deep Blue text, bold):
    "Formulating precise research briefs"
    "Evaluating AI synthesis critically"
    "Identifying gaps the AI missed"
    "Domain judgment & theory selection"
    "Ethical oversight & accountability"

VERTICAL DIVIDER between columns.

BOTTOM IMPLICATION BOX (Deep Blue border):
  "Doctoral training must adapt: less manual synthesis, more critical evaluation of AI outputs"

CRITICAL: The two columns must be clearly colour-coded. Arrows must show direction of change.
""",
    },

    # ── fig16: Reflexive structure ───────────────────────────────────────────
    {
        "filename": "fig16_reflexive_structure.png",
        "caption": "Reflexive paradox: the system's self-assessment is shaped by the same training that produced its capabilities.",
        "context": DS + """
DIAGRAM TYPE: Self-referential loop diagram with paradox annotation.

MAIN LOOP (circular, centre of canvas):
  NODE A (top, Deep Blue fill, white text): "Constitutional AI Training\n(Normative principles embedded)"
  NODE B (right): "Epistemic Self-Monitoring\n(Flags uncertainty, cites sources)"
  NODE C (bottom): "Self-Assessment Output\n('I acknowledge my limitations')"
  NODE D (left): "Same Training Process\n(Shapes the self-assessment itself)"

Clockwise arrows A→B→C→D→A (Deep Blue).

PARADOX ANNOTATION (red dashed box outside the loop):
  "The Reflexive Paradox:
   The system cannot step outside itself.
   Its acknowledgment of limitations
   is ITSELF a product of CAI training —
   and may be systematically incomplete
   in ways the model cannot detect."

HUMAN COUNTERPOINT (bottom, italic, grey):
  "But: human researchers also write from within their frameworks.
   The model's reflexive limits are more systematic — not categorically different."

CRITICAL: The circular self-reference must be visually obvious. The paradox box must contrast with the main loop.
""",
    },

    # ── fig17: Artifact flow ─────────────────────────────────────────────────
    {
        "filename": "fig17_artifact_flow.png",
        "caption": "Artifact flow: detailed data lineage from raw database searches to final assembled LaTeX manuscript.",
        "context": DS + """
DIAGRAM TYPE: Horizontal data flow lineage diagram.

LEFT ZONE (Raw Inputs):
  Stacked database icons/boxes: "Semantic Scholar", "arXiv", "OpenAlex", "CrossRef".

MIDDLE ZONE (Intermediate State):
  3 sequential artifact nodes (blue/teal gradients):
  1: "literature_base.csv & references.bib" -> Arrow to 2
  2: "framing.md & concept_matrix.md" -> Arrow to 3
  3: "draft.md (Markdown Full Text)"

RIGHT ZONE (Final Outputs):
  2 parallel final artifacts:
  Top: "paper.tex (LaTeX Source)"
  Bottom: "Compiled paper.pdf"

ARROWS: 
  Sleek data flow tubes or styled arrows connecting the zones left-to-right. 
  Label the arrows with processes: "MCP Fetch & Deduplicate", "LLM Reasoning", "Bash Compilation".

CRITICAL: Emphasize the transformation from raw unstructured data on the left to structured, publication-ready formats on the right.
""",
    },

    # ── fig18: Peer review loop ──────────────────────────────────────────────
    {
        "filename": "fig18_peer_review_loop.png",
        "caption": "AI-augmented peer review system tracking hallucination risks and claim evidence.",
        "context": DS + """
DIAGRAM TYPE: Auditing workflow / system diagram.

MAIN SUBJECT:
  Center element: "Submitted Manuscript (AI-Generated)" with attached "Artifact Chain (CSV, BibTeX)".

LEFT ACTOR (Human Reviewer):
  Box: "Human Peer Reviewer"
  Role: "Evaluates theory, novelty, and overarching arguments."
  Arrow to Center: "Qualitative Critique"

RIGHT ACTOR (AI Audit Agent):
  Box: "AI Review Assistant"
  Role: "Verifies live citations, flags hallucination risks, checks claims against base evidence."
  Arrow to Center: "Automated Evidence Audit"

BOTTOM FEEDBACK:
  A warning/alert box (amber/red accents): "Audit Engine Output"
  Text inside: "⚠ Flag: Claim 3 unverified in cited source" | "✓ Citation 41 matched perfectly"

CRITICAL: Clearly divide the qualitative human review from the quantitative/factual AI audit process. Use high-end visuals and crisp icons.
""",
    },

]


async def regenerate_all():
    settings = Settings(
        vlm_provider="gemini",
        vlm_model="gemini-2.0-flash",
        image_provider="google_imagen",
        image_model="gemini-3-pro-image-preview",
        refinement_iterations=1,
        optimize_inputs=True,
        auto_refine=False,
    )

    pipeline = PaperBananaPipeline(settings=settings)
    total = len(FIGURES)
    print(f"\n🚀 Generating {total} figures for 'Open Paper Machine' paper...\n")

    for i, fig in enumerate(FIGURES, 1):
        print(f"[{i:02d}/{total}] {fig['filename']}...")
        try:
            result = await pipeline.generate(
                GenerationInput(
                    source_context=fig["context"],
                    communicative_intent=fig["caption"],
                    diagram_type=DiagramType.METHODOLOGY,
                )
            )
            src = Path(result.image_path)
            dst = OUTPUT_DIR / fig["filename"]
            dst.write_bytes(src.read_bytes())
            print(f"  ✅ Saved → {dst.name}\n")
        except Exception as e:
            print(f"  ❌ Error: {e}\n")

    print("🎉 Done! All figures generated.")


if __name__ == "__main__":
    asyncio.run(regenerate_all())
