---
title: "A patient-specific treatment attempt for a rare epilepsy, and how hard a cure really is"
date: 2026-05-06
permalink: /en/posts/2026-05-06/
lang: en
translation: /posts/2026-05-06/
tags:
  - biology
  - neuroscience
  - genetics
---

Think about a disease caused by a mutation in a single gene. The obvious conclusion is that correcting or suppressing just that mutation should solve it. And that's basically right. The hard part is how to do that efficiently, across every relevant cell, without touching any other gene. This paper is about the achievements and limits of rare pediatric disease research as it currently stands.

## EIMFS and the KCNT1 mutation

EIMFS (Epilepsy of Infancy with Migrating Focal Seizures), a severe epilepsy that appears from infancy, is known to arise from a de novo mutation in KCNT1 — one that neither parent carries — in over 25% of cases. Neuronal activity runs on the voltage difference created by sodium/potassium flux, and when a potassium pump like KCNT1 malfunctions, the R474H mutation specifically amplifies the resulting signal up to 22-fold. Small wonder that produces epilepsy.

Cells were taken from a patient with the most severe presentation (up to 30-40 seizures a day) carrying R474H, reprogrammed into stem cells, and differentiated back into neurons.

## A selective suppression strategy using ASOs

With the causal gene identified, the team turned to antisense oligonucleotides (ASOs) to eliminate the mutant gene's transcript. A disease-mutant DNA has to be transcribed into RNA and then translated into protein. Introduce an ASO with a sequence complementary to the mutant mRNA, and it binds that RNA before translation, forming an RNA duplex the cell's machinery mistakes for a virus and cuts apart.

In theory, this lets you suppress the mutant-making mRNA more selectively than the normal mRNA. (The figure below is borrowed from another paper, but this is roughly how it works.)

Screening over 200 candidates, the team found an ASO that completely suppressed the mutant potassium-channel effect in iPSC-derived neurons. The trouble started when they tried to move this to a rodent model.

## An uneasy compromise in the rodent model

Human and rodent (mouse and rat) genes differ substantially, and the region an ASO was designed against for the human R474H patient turned out to differ a lot in sequence from the corresponding mouse region. So they instead tested it in mice carrying an unrelated mutation, P905L. It worked — but this time not by selectively lowering the mutant protein; it lowered the gene's expression regardless of whether the copy was normal or mutant. This is where things start to feel like a compromise. This is exactly the moment where a NAM approach — human stem cells or organoids — would have been the better choice.

## Results in the patient

Ultimately, whether or not the mouse work justified it, the treatment moved to the patient.

In the patient, it produced a dramatic, though temporary, suppression of seizures. Afterward, seizures returned — not quite to baseline, but to a meaningful degree. Statistically significant reduction, still at a fairly high level. A weak result to call a treatment.

## What's left to want

In the end there's a lot to wish had gone differently: 1) a better ASO, 2) patient-derived iPSCs, 3) good organoids, or a humanized mouse carrying the actual patient mutation as a knock-in, 4) and only then dosing the patient. Delivery of the ASO itself remains a major problem too.

But this is the current state of the field, and reading it with the hope that these gaps get addressed in future rare-disease work is a paper worth the time.

## References

- https://www.nature.com/articles/s41591-026-04314-9
