---
title: "G51D knock-in mice"
collection: projects
permalink: /projects/g51d-knock-in-mice
order: 1
status: "Published in PNAS (2024)"
summary: "A knock-in mouse carrying a Parkinson's-causing SNCA mutation at its own locus, which reproduces the order in which human symptoms appear: smell and gut first, movement much later."
---

## The problem with existing models

Parkinson's disease (PD) is usually sporadic and late-onset, which makes it hard to model in a mouse. Most α-Synuclein (α-Syn) models overexpress the protein under a heterologous promoter such as *Thy1* or *prion*, or introduce it by injecting preformed fibrils or virus into the substantia nigra.

These models proved that excess α-Syn is toxic, but they distort the question I care about: **where the disease starts and how it travels**. Overexpression puts α-Syn into brain regions that human PD never touches, and injection models bypass peripheral tissue altogether — precisely where the earliest human pathology is thought to appear.

## Approach

I used CRISPR-Cas9 to edit the endogenous mouse *Snca* locus, installing human PD-causing point mutations so that mutant α-Syn is expressed under its own promoter, at its own levels, in its own spatiotemporal pattern.

Of the four mutations attempted (A30P, E46K, H50Q, G51D), three lines were established; H50Q could not be recovered. *Snca* mRNA and α-Syn protein remained comparable to wild-type in all three, confirming the lines report on mutation rather than on dosage. Homozygotes were studied, since a short mouse lifespan often hides heterozygous phenotypes.

Among the three, homozygous *Snca*<sup>G51D/G51D</sup> proved the informative line. G51D causes the earliest onset of any known *SNCA* mutation in humans, sometimes in the first decade.

## What the mice show

The phenotypes emerge in a fixed order, and that order is the point.

<figure class="project__figure">
<svg viewBox="0 0 720 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="g51d-fig-title g51d-fig-desc">
  <title id="g51d-fig-title">Order of pathology and symptoms in Snca G51D/G51D mice</title>
  <desc id="g51d-fig-desc">A timeline from 3 to 18 months of age. Phosphorylated alpha-synuclein appears in the olfactory bulb, enteric nerves and vagal nucleus at 3 months, before any symptom. Impaired smell and slowed gut transit follow at 6 months. Motor incoordination begins at 9 months; altered gait with astrogliosis and pathology reaching the substantia nigra at 12 months; loss of dopaminergic neurons and reduced dopamine at 18 months. The interval from 3 to 9 months is a prodromal window corresponding to Braak stages one and two.</desc>

  <rect x="34" y="36" width="310" height="228" rx="4" fill="var(--global-base-color)" fill-opacity="0.08"/>
  <text x="189" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--global-base-color)">Prodromal &#8212; Braak I&#8211;II</text>
  <text x="522" y="26" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--global-text-color)">Motor phase &#8212; Braak III&#8211;IV</text>

  <g font-size="12" fill="var(--global-text-color)" text-anchor="middle">
    <text x="104" y="66">pS129-&#945;-Syn in</text>
    <text x="104" y="82">olfactory bulb, enteric</text>
    <text x="104" y="98">nerves, vagal nucleus</text>
    <text x="454" y="66">pS129-&#945;-Syn reaches</text>
    <text x="454" y="82">substantia nigra;</text>
    <text x="454" y="98">astro- and microgliosis</text>
  </g>
  <g stroke="var(--global-text-color)" stroke-opacity="0.35" stroke-width="1">
    <line x1="104" y1="108" x2="104" y2="152"/>
    <line x1="454" y1="108" x2="454" y2="152"/>
    <line x1="224" y1="188" x2="224" y2="206"/>
    <line x1="344" y1="188" x2="344" y2="206"/>
    <line x1="624" y1="188" x2="624" y2="206"/>
  </g>

  <line x1="44" y1="160" x2="684" y2="160" stroke="var(--global-text-color)" stroke-width="1.5"/>
  <g fill="var(--global-bg-color)" stroke="var(--global-text-color)" stroke-width="1.5">
    <circle cx="104" cy="160" r="5"/>
    <circle cx="224" cy="160" r="5"/>
    <circle cx="454" cy="160" r="5"/>
    <circle cx="624" cy="160" r="5"/>
  </g>
  <circle cx="344" cy="160" r="6" fill="var(--global-base-color)" stroke="var(--global-base-color)"/>

  <g font-size="11" font-weight="bold" fill="var(--global-text-color)" text-anchor="middle">
    <text x="104" y="180">3 mo</text>
    <text x="224" y="180">6 mo</text>
    <text x="344" y="180">9 mo</text>
    <text x="454" y="180">12 mo</text>
    <text x="624" y="180">18 mo</text>
  </g>

  <g font-size="12" fill="var(--global-text-color)" text-anchor="middle">
    <text x="224" y="220">impaired smell,</text>
    <text x="224" y="236">slowed gut transit</text>
    <text x="344" y="220" font-weight="bold">motor incoordination</text>
    <text x="344" y="236">(rotarod, footslips)</text>
    <text x="454" y="220">altered gait</text>
    <text x="624" y="220">dopaminergic loss,</text>
    <text x="624" y="236">reduced dopamine</text>
  </g>

  <text x="44" y="288" font-size="11" fill="var(--global-text-color)" fill-opacity="0.75">Molecular pathology above the axis, behavioural signs below.</text>
</svg>
<figcaption>Pathology is detectable six months before the first motor sign. The shaded interval is the window in which a therapy can be tested before irreversible loss.</figcaption>
</figure>

Non-motor signs precede motor signs by three months, mirroring the two-decade prodrome in patients.

**Three pathological species of α-Syn** form in these mice: S129-phosphorylated α-Syn, soluble oligomers running from 60 kDa to above 250 kDa on blue native PAGE, and Triton X-100–insoluble aggregates.

**Cortical pathology is layer-restricted.** Signal appears in layers II and IV at 3 months and extends to layer V by 12 months — the same layers that carry Lewy bodies in postmortem tissue from patients with *SNCA* mutations. *Thy1*-α-Syn overexpressing mice, by contrast, show signal across every cortical layer.

**The pathology is neuronal.** pS129-α-Syn colocalizes with NeuN, is absent from astrocytes, and appears in fewer than 5% of oligodendrocytes. This matters because G51D patients can present with features resembling multiple system atrophy, an oligodendrocyte-driven synucleinopathy. These mice resemble PD, not MSA.

**Motor deficits arrive before dopamine loss** — 9 months versus 18. Dopaminergic dysfunction, rather than outright neuronal death, appears to drive the early motor phenotype, with neuroinflammation tracking dysfunction more closely than cell loss.

## Why it matters

The progression maps onto Braak staging: olfactory and vagal involvement at stages I–II (3–6 months), reaching the nigra at stages III–IV (9–12 months). Because pathology is detectable at 3 months but motor symptoms do not arrive until 9, the model opens a **prodromal window** — a period in which a candidate therapy can be tested well before irreversible neuron loss.

This is the model I now use to ask whether interventions can change the course of the disease rather than treat its endpoint, including the astrocytic work described in [ACSBG1-mediated astrocyte–neuron crosstalk](/projects/acsbg1-astrocyte-neuron-crosstalk).

## Reference

Kim Y, McInnes J, Kim J, Liang YW, Veeraragavan S, Garza AR, Belfort DW, Arenkiel B, Samaco R, Zoghbi HY. Olfactory deficit and gastrointestinal dysfunction precede motor abnormalities in alpha-synuclein G51D knock-in mice. *Proc. Natl. Acad. Sci. U.S.A.* 2024, 121(39) e2406479121. [doi:10.1073/pnas.2406479121](https://doi.org/10.1073/pnas.2406479121)
