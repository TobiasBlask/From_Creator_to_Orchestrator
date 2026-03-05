# Änderungsprotokoll — Burkhardt Round 3 (7 Kommentare)

Baseline: Zustand nach Round 2 (16 Kommentare, Commit `df5e261`)

---

## Phase 1: Terminologie

| # | Stelle | Änderung |
|---|--------|----------|
| 1+3 | §1.3, Contribution #2 | "autonomous research systems" → "autonomous research agents" |
| 1+3 | §2.5, Subsection title | `\subsection{Related Systems}` → `\subsection{Related Agents}` |
| 1+3 | §2.5, Intro text | "autonomous AI research systems that informed" → "autonomous AI research agents that informed" |
| 1+3 | Table 1 caption | "Autonomous AI research systems." → "Autonomous AI research agents." |
| 1+3 | §4.1, Eval paragraph | "autonomous research systems (Table~...)" → "autonomous research agents (Table~...)" |
| — | §3.1 (line 218) | "within the research system" — bewusst NICHT geändert (Singular, anderer Kontext: OPM als kognitives System, nicht Tabelle 1) |

---

## Phase 2: Strukturelle Änderung — §4.2 Restrukturierung

| # | Stelle | Änderung |
|---|--------|----------|
| 5 | §4.2 | **§4.2 "The Pipeline as Data" restrukturiert:** Neuer Absatz mit Kurzbeschreibung aller 6 Phasen eingefügt (was der Agent in jeder Phase tut). Folgt direkt nach dem Einleitungsabsatz, vor Table 2. |
| 4 | §4.2 → §8.1 | **"Scope and applicability"-Absatz aus §4.2 nach §8.1 (Summary) verschoben.** Burkhardt: "not part of the method section, but discussion/conclusion." |

---

## Phase 3: Textuelle Korrekturen

| # | Stelle | Änderung |
|---|--------|----------|
| 6 | §4.2, Orchestrator trace | "included:" → "included, for instance:" |
| 7 | §7.3 | `Section~6.1` → `Section~\ref{sec:task_redistribution}` (Querverweis-Fehler korrigiert: §6.1 = "What Worked", richtig ist §7.1 = "The Task Redistribution") |
| 7 | §7.1 | `\label{sec:task_redistribution}` hinzugefügt |

---

## Phase 4: Abbildung

| # | Stelle | Änderung |
|---|--------|----------|
| 2 | Figure 1 | Pipeline-Abbildung (`fig2_pipeline_phases.png`) neu generiert — "Human Orchestrator evaluates"-Zone erstreckt sich jetzt bis einschließlich `paper.pdf` (vorher endete sie bei Self-Review) |

---

## Zusammenfassung

- **7 Kommentare** vollständig eingearbeitet
- **Größte Änderung:** §4.2-Restrukturierung mit Phasenbeschreibungen + Scope-Verschiebung nach §8
- **Terminologie:** "research systems" → "research agents" durchgängig (5 Stellen)
- **Kompilierung:** 0 Fehler, 19 Seiten, alle Querverweise aufgelöst
