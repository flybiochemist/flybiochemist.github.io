---
title: "Why primer placement matters when checking a CRISPR knockdown by qPCR"
date: 2026-09-01
permalink: /en/posts/2026-09-01/
lang: en
translation: /posts/2026-09-01/
tags:
  - biology
  - molecular-biology
  - lab-tips
---

RT-qPCR is a common way to confirm that a CRISPR-Cas9 knockdown worked. In mice, or in a cell line carried through several passages, the guide RNA gets diluted out over time — but if you are checking right after cutting, as in a screen, the gRNA can still be riding along in your extracted RNA and interfere with qPCR at that site.

So, as the paper notes, either use a reverse transcriptase that properly unwinds the resulting RNA-DNA duplex before it runs, or, if you are an ordinary experimentalist not about to buy a specialty enzyme just for this, place your qPCR target a bit further away from the gRNA's cutting site.

Design your PCR primers wisely.

## References

- https://www.nature.com/articles/s41587-026-03291-1
