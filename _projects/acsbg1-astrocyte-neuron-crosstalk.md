---
title: "ACSBG1-mediated astrocyte–neuron crosstalk in synucleinopathy"
collection: projects
permalink: /projects/acsbg1-astrocyte-neuron-crosstalk
lang: en
translation: /ko/projects/acsbg1-astrocyte-neuron-crosstalk
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

<figure class="project__figure">
<svg viewBox="0 0 720 286" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="acsbg1-fig-title acsbg1-fig-desc">
  <title id="acsbg1-fig-title">How astrocytic ACSBG1 drives neuronal alpha-synuclein phosphorylation</title>
  <desc id="acsbg1-fig-desc">Two parallel paths. In wild-type astrocytes, TNF-alpha and IL-1alpha drive a reactive state in which ACSBG1 is active; the astrocytes secrete IL-6, RANTES and MIP-3 alpha together with long-chain sphingosine C20:1 and C22:1, and neurons respond with increased phosphorylated alpha-synuclein at serine 129. In Acsbg1 knockout astrocytes the same stimulus produces reduced cytokine release and sphingosine returned to baseline, and neuronal phosphorylated alpha-synuclein does not increase.</desc>

  <defs>
    <marker id="ac-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--global-text-color)"/>
    </marker>
  </defs>

  <text x="6" y="20" font-size="12" font-weight="bold" fill="var(--global-base-color)">Wild-type astrocytes &#8212; pathology transfers</text>
  <g stroke="var(--global-text-color)" stroke-width="1" fill="none">
    <rect x="6" y="34" width="76" height="64" rx="4"/>
    <rect x="110" y="34" width="140" height="64" rx="4"/>
    <rect x="278" y="34" width="210" height="64" rx="4" stroke="var(--global-base-color)" fill="var(--global-base-color)" fill-opacity="0.08"/>
    <rect x="516" y="34" width="88" height="64" rx="4"/>
  </g>
  <g font-size="12" fill="var(--global-text-color)" text-anchor="middle">
    <text x="44" y="62">TNF-&#945;</text>
    <text x="44" y="78">IL-1&#945;</text>
    <text x="180" y="62">Reactive astrocyte</text>
    <text x="180" y="80" font-weight="bold">ACSBG1 active</text>
    <text x="383" y="56">IL-6 &#183; RANTES &#183; MIP-3&#945;</text>
    <text x="383" y="74">sphingosine</text>
    <text x="383" y="90" font-weight="bold">C20:1 / C22:1</text>
    <text x="560" y="72">Neuron</text>
    <text x="662" y="64" font-weight="bold" fill="var(--global-base-color)">&#8593; pS129-</text>
    <text x="662" y="80" font-weight="bold" fill="var(--global-base-color)">&#945;-Syn</text>
  </g>
  <g stroke="var(--global-text-color)" stroke-width="1.5" marker-end="url(#ac-arrow)">
    <line x1="84" y1="66" x2="106" y2="66"/>
    <line x1="252" y1="66" x2="274" y2="66"/>
    <line x1="490" y1="66" x2="512" y2="66"/>
    <line x1="606" y1="66" x2="624" y2="66"/>
  </g>

  <text x="6" y="162" font-size="12" font-weight="bold" fill="var(--global-text-color)">Acsbg1 knockout &#8212; the link is broken</text>
  <g stroke="var(--global-text-color)" stroke-width="1" fill="none" stroke-opacity="0.55">
    <rect x="6" y="176" width="76" height="64" rx="4"/>
    <rect x="110" y="176" width="140" height="64" rx="4"/>
    <rect x="278" y="176" width="210" height="64" rx="4" stroke-dasharray="4 3"/>
    <rect x="516" y="176" width="88" height="64" rx="4"/>
  </g>
  <g font-size="12" fill="var(--global-text-color)" text-anchor="middle">
    <text x="44" y="204">TNF-&#945;</text>
    <text x="44" y="220">IL-1&#945;</text>
    <text x="180" y="204">Reactive astrocyte</text>
    <text x="180" y="222" font-weight="bold">Acsbg1 knockout</text>
    <text x="383" y="198">cytokine release reduced</text>
    <text x="383" y="216">sphingosine back</text>
    <text x="383" y="232">to baseline</text>
    <text x="560" y="214">Neuron</text>
    <text x="662" y="214" font-weight="bold">no increase</text>
  </g>
  <g stroke="var(--global-text-color)" stroke-width="1.5" stroke-opacity="0.55" marker-end="url(#ac-arrow)">
    <line x1="84" y1="208" x2="106" y2="208"/>
    <line x1="252" y1="208" x2="274" y2="208"/>
    <line x1="490" y1="208" x2="512" y2="208"/>
  </g>

  <text x="6" y="276" font-size="11" fill="var(--global-text-color)" fill-opacity="0.75">Each cytokine alone, and C20:1 or C22:1 sphingosine alone, is sufficient to raise neuronal pS129-&#945;-Syn.</text>
</svg>
<figcaption>ACSBG1 couples astrocytic lipid processing to the inflammatory secretome. Removing it leaves the astrocyte reactive but strips the mediators that reach the neuron.</figcaption>
</figure>

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
