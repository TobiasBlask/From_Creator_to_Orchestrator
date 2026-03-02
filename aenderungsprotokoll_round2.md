# Änderungsprotokoll — Burkhardt Round 2 (16 Kommentare)

Baseline: Zustand nach Round 1 (78 Kommentare bereits eingearbeitet)

---

## Phase 1: Textuelle Korrekturen

| # | Stelle | Änderung |
|---|--------|----------|
| 1 | Autorenzeile | `\thanks{Equal contribution.}` und `\footnotemark[1]` entfernt |
| 2 | §1.1, Zeile 93 | „and corrected errors" → „and changed the wording of the final document" |
| 3 | §1.1, Zeile 99 | „First, no prior study positions an LLM…" → „First, we are not aware of a prior study that positions an LLM…" |
| 13 | §8.2 (alt §7.2) | Satz „These challenges will manifest differently across disciplines…" gelöscht |
| 14 | §8.2 (alt §7.2) | Satz „Our argument applies most directly to desk-research-intensive disciplines…" gelöscht |

---

## Phase 2: Strukturelle Änderung — §2-Split

| # | Stelle | Änderung |
|---|--------|----------|
| 4+5 | §2 | **§2 „Theoretical Foundations" aufgeteilt in zwei Sektionen:** |
| | | **Neue §2 „Technical Foundations"** (Label `sec:tech`): §2.1 Transformers, §2.2 Alignment, §2.3 Tool-Augmented Agency, §2.4 Hallucination (zusammengelegt), §2.5 Related Systems |
| | | **Neue §3 „Theoretical Lenses"** (Label `sec:lenses`): §3.1 Distributed Cognition, §3.2 Sociotechnical Systems/MLP, §3.3 Task Formulation/Creator-to-Orchestrator |
| | | Folgend: §4 Methodology, §5 Technology Stack, §6 Capabilities, §7 From Creator to Orchestrator, §8 Conclusion |
| 6 | §2 Intro | Satz „Before developing these frameworks, we address the technical preconditions…" gelöscht |
| 7 | §2.4 | Hallucination-Vorabhinweis (Zeile 131) + §2.7 Hallucination Mitigation zu einem Unterabschnitt „Hallucination and Its Mitigation" zusammengeführt |

---

## Phase 3: Tabellen, Abbildungen, Konsistenz

| # | Stelle | Änderung |
|---|--------|----------|
| 8 | §2.5 Related Systems | **Nachholen aus Round 1:** Die in Round 1 geforderte Entschärfung der Vergleichs- und Einzigartigkeitsargumentation war nicht vollständig umgesetzt worden. Jetzt korrigiert: „only system"-Claim entfernt; Passage umformuliert zu „The Open Paper Machine differs from these systems not in capability but in intent"; Vergleichssprache („compared against") durchgängig durch Landschafts-Framing ersetzt |
| 9 | §4 Methodology | Overselling-Passage entfernt (überhöhte Methodenbeschreibung gestrichen) |
| 10 | Table 1 | Caption geändert: „Comparison of autonomous AI research systems" → „Autonomous AI research systems relevant to this paper"; Einleitungstext von Vergleichs- auf Landschafts-Framing umgestellt; Label `tab:comparison` → `tab:systems` |
| 11 | Figure 1 | **Nachholen aus Round 1:** Die in Round 1 geforderte Umbenennung von „Architecture" → „Structure" war im Fließtext und in Table 2 umgesetzt worden, aber die Abbildung selbst wurde nicht neu generiert. Jetzt korrigiert: Pipeline-Abbildung (`fig2_pipeline_phases.png`) via PaperBanana neu generiert — zeigt jetzt „Structure" statt „Architecture" |
| 12 | Durchgängig | **Nachholen aus Round 1:** Die in Round 1 geforderte konsistente Phasen-Terminologie war nicht durchgängig umgesetzt worden (insb. in der Abbildung). Jetzt vollständig vereinheitlicht: Reconnaissance, Framing, **Structure**, Production, Assembly, Self-Review — in Abbildung, Tabelle 2, und Fließtext |

**Zusätzliche Konsistenz-Fixes (aus #8 abgeleitet):**

| Stelle | Änderung |
|--------|----------|
| §1.1, Contribution #2 | „compared against six existing autonomous research systems" → „situated within the landscape of autonomous research systems" |
| §4 Methodology | „compared against six autonomous research systems" → „situated within the landscape of autonomous research systems" |

---

## Phase 4: Literaturverzeichnis

| # | Stelle | Änderung |
|---|--------|----------|
| 15 | references.bib | 5 arXiv-Einträge standardisiert: arXiv-IDs im Journal-Feld ergänzt (`bai2022constitutional`, `greshake2023prompt`, `henneking2025inverse`, `si2024llms`, `yamada2025scientist`); DOI für `bai2022constitutional` hinzugefügt |
| 16 | references.bib | `guan2024amor`: Fehlende Metadaten ergänzt (volume=38, number=16, pages=17777–17785, DOI) |

---

## Zusammenfassung

- **16 Kommentare** vollständig eingearbeitet
- **Größte Änderung:** §2-Split in „Technical Foundations" + „Theoretical Lenses"
- **Kompilierung:** 0 Fehler, 18 Seiten, alle Querverweise aufgelöst
- **Commit:** `00af92b`
