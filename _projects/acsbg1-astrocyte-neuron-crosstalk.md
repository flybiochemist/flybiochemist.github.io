---
title: "ACSBG1-mediated astrocyte–neuron crosstalk in synucleinopathy"
collection: projects
permalink: /projects/acsbg1-astrocyte-neuron-crosstalk
order: 2
status: "Preprint, BioRxiv (2026)"
summary: "How a lipid enzyme expressed only in astrocytes changes α-Synuclein inside neurons — and why switching it off rescues a Parkinson's mouse."
---

## The question

α-Synuclein (α-Syn) pathology is a neuronal problem, but neurons do not sit alone. Astrocytes supply their metabolic support and handle much of the brain's lipid processing, and in disease they shift from protective to reactive states.

Our earlier genome-wide screens identified **ACSBG1** — Acyl-CoA Synthetase Bubblegum Family Member 1 — as a robust in vivo regulator of α-Syn levels. ACSBG1 converts long- and very-long-chain fatty acids into fatty acyl-CoAs, and in the brain it is expressed almost exclusively in astrocytes.

That left an obvious puzzle: **how does a lipid enzyme, in a cell that is not the neuron, change what happens to α-Syn inside the neuron?**

## Approach

The core experiment is a conditioned-medium transfer. Primary astrocytes from wild-type or *Acsbg1* knockout mice were driven into a reactive state with TNF-α and IL-1α, and their medium was transferred onto primary neurons. Around that, we profiled what the astrocytes were doing and what they were releasing:

- RNA-seq of the astrocytes themselves
- A cytokine antibody array and untargeted lipidomics on the secreted medium
- Add-back of individual candidate cytokines and of synthetic sphingosines of defined chain length
- A catalytically impaired ACSBG1 (K701A) to separate enzyme activity from mere presence
- *Acsbg1* knockout crossed onto the Thy1-α-Syn (Line 61) transgenic model for the in vivo test

## What we found

**The medium carries the pathology.** Conditioned medium from reactive wild-type astrocytes raised both total and pS129-α-Syn in neurons. Medium from reactive *Acsbg1* knockout astrocytes did not.

**Two mediators, not one.** Losing *Acsbg1* blunted the astrocytes' TNF-signaling transcriptional response and cut the release of inflammatory mediators. Three stood out — **IL-6, RANTES, and MIP-3α** — and adding any one of them back to normal medium was sufficient on its own to raise neuronal α-Syn and, more strikingly, pS129-α-Syn.

The lipid arm ran in parallel. Cytokine activation raised sphingosine, LBPA, and hexosylceramide in wild-type medium; *Acsbg1* deletion returned them to baseline. Supplementing knockout medium with synthetic sphingosines showed sharp chain-length selectivity: **C20:1 and C22:1 restored neuronal pS129-α-Syn, while C16:1 and C18:1 did nothing.**

**It depends on catalysis, not presence.** The pan-ACS inhibitor Triacsin C reproduced the knockout effect. Re-expressing wild-type ACSBG1 in knockout astrocytes restored their ability to drive neuronal pathology; the catalytically dead K701A mutant did not.

**It holds in vivo.** In Thy1-α-Syn mice, deleting *Acsbg1* normalized stereotypic and rearing behavior, improved parallel rod and pole test performance, reduced total and pS129-α-Syn in cortex and midbrain, resolved GFAP astrogliosis, and preserved PSD95 — meaning synapses were protected, not just markers moved.

## Why ACSBG1 is a promising target

Its expression is unusually restricted: astrocytes in the brain, and little outside the testis and ovary. *Acsbg1* knockout mice have no overt baseline phenotype, so the brain tolerates its loss under healthy conditions. Together that suggests a wide therapeutic index — an enzyme that can be inhibited to blunt disease-associated astrocyte reactivity without much collateral cost.

## What's next

Thy1-α-Syn is an overexpression model, and its deficits are severe from five weeks — early enough that rotarod and grip strength are already floored and cannot resolve improvement. The natural next step is to test *Acsbg1* deletion in the [*Snca*<sup>G51D/G51D</sup> knock-in model](/projects/g51d-knock-in-mice), where pathology unfolds at endogenous expression levels and a prodromal window exists before motor symptoms appear. That combination should show whether targeting astrocytic ACSBG1 can slow synucleinopathy as it develops, rather than blunting an already-saturated phenotype.

## Reference

Kim Y\*, Vaidya B\*, Kim J, Bitar S, Shajan FJ, Verma AK, Yalamanchili HK, Singh S, Zoghbi HY. Astrocytic ACSBG1 depletion improves lipid-cytokine signaling and attenuates α-Synuclein pathology in a Parkinson's disease mouse model. *BioRxiv* May 2026. [doi:10.64898/2026.05.20.726454](https://doi.org/10.64898/2026.05.20.726454)

\* equal contribution
