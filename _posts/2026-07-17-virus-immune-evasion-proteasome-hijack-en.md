---
title: "How viruses evade immunity — hijacking the proteasome"
date: 2026-07-17
permalink: /en/posts/2026-07-17-2/
lang: en
translation: /posts/2026-07-17-2/
tags:
  - biology
  - immunology
  - molecular-biology
---

There is already a great deal of work on how viruses evade the immune system. The well-known routes: mutating just enough that existing antibodies no longer recognise the antigen, mimicking the host species' own proteins, and — once inside — coating themselves in material taken from the host so that immune cells stop noticing them.

But those are all somewhat indirect. There are also mechanisms that block the immune response from being generated in the first place. One of them is interference with antigen presentation. Antigen-presenting cells (APCs) digest a virus into protein fragments and hand some of those to T cells, and the T cells that receive them go hunting. Block the presentation step and the T cells are never activated.

## 500 viruses, 8,000 genes, one screen

Stephen J. Elledge's group published two papers this month, one in Cell and one in Science. The Cell paper builds a library of 13,000 ORFs covering 8,000 genes from 500 viral species, and screens it. Some of the viral proteins turned out to act on cell division, on interferon signalling, and on MHC class I — the route by which antigen reaches T cells. If inhibitors of these viral proteins can eventually be developed, they could help boost antiviral immunity.

The Science paper takes up part of the antigen presentation process itself: how the ubiquitin-proteasome degradation system (UPS) is manipulated by viral proteins.

## Viruses that forge the ubiquitin tag

A protein clump digested by an APC first gets tagged with ubiquitin, which marks it as something to be broken down. That tag is extended step by step through a chain of three enzymes (E1, E2, E3), and a protein carrying the resulting long tag is fed into the proteasome — a barrel-shaped disposal unit — and chopped into small pieces. Those pieces are what gets handed to the T cell.

So the team screened the Cell paper's library for viral proteins that inhibit the UPS. To work out how the effective ones operate, they then knocked down UPS-related proteins with CRISPR-Cas9 and looked for cases where the inhibition was cancelled out.

The result: some viral proteins exploit structural similarity to bind CUL5-ELOB/C, an E3 — the third enzyme in the ubiquitin chain — and obstruct it. Others act as counterfeit ubiquitin ligases, hijacking the proteins that were meant to act next in the degradation sequence. Either way they effectively sabotage the order to rapidly degrade proteins coming from antiviral signalling. T cell activation slows, and the virus gets to multiply more comfortably.

What struck me personally: in neurodegeneration, the idea that viral infection worsens disease was treated as heresy for a long time. This makes me think that alongside inflammation, direct inhibition of protein degradation may be part of that picture too. An enjoyable read for that reason.

Sadly, Eric Fujimura — first author on the Cell paper and a co-author on the Science one — has since passed away.

## References

- https://www.science.org/doi/10.1126/science.aec6299
- https://www.cell.com/cell/fulltext/S0092-8674(26)00583-0
