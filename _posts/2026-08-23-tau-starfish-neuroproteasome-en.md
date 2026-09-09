---
title: "A new technique reveals where tau protein is made and degraded"
date: 2026-08-23
permalink: /en/posts/2026-08-23/
lang: en
translation: /posts/2026-08-23/
tags:
  - biology
  - alzheimers
  - molecular-biology
---

Alzheimer's researchers spend most of their time on Abeta and tau (ApoE is getting more attention too these days). There are three reasons: first, in the Alzheimer's brain, Abeta aggregates outside neurons while tau aggregates inside them; second, introducing the right mutations alone is enough to reproduce several disease symptoms in animal models; and third, simply clearing out Abeta or tau can weaken symptoms in those same models. (Plenty of people dispute all three points, and I'm aware of that.)

But how these proteins are actually made, put to work, and broken down is understood far less than you'd expect. So whenever a new technique or a newly discovered neuron-specific mechanism shows up, someone builds a paper marrying that tool to the old questions. Today's paper looks at the life cycle of tau using a tool called STARFISH and a concept called the neuroproteasome.

## What is STARFISH?

STARFISH, built by the paper's authors, combines single-molecule fluorescence in situ hybridization with a proximity ligation assay. Let's take it apart piece by piece.

DNA is the blueprint. When a protein is needed, it's transcribed into an intermediate, mRNA; the ribosome reads that mRNA three letters at a time, and tRNA delivers the amino acid each triplet specifies, which get strung together into a protein.

To find out where a given mRNA is sitting, you synthesize a probe complementary to it and tag it with a fluorophore. The single-stranded mRNA binds the probe on contact, forming a double strand — wherever you see the fluorescence, that's where your mRNA is. That's fluorescence in situ hybridization. The shorter the complementary sequence, the closer you get to true single-molecule resolution.

A proximity ligation assay is the newest way to measure whether two proteins are sitting close together. The older tools were things like splitting a fluorescent protein in two so the halves reassemble and glow when the proteins come close (BiFC), or tagging one protein with something that emits blue light under UV and the other with something that turns blue light into yellow, then watching for yellow (FRET).

The trouble is that GFP is a bulky protein, and things often don't behave the way you'd hope. So these days, instead of tagging the proteins themselves, people attach a single strand of DNA — not double-stranded — to the antibodies against them. When the two proteins are close enough, the strands recognize complementary sequences, anneal into a small stable circle, and DNA polymerase amplifies that circle like crazy. The resulting blob of DNA tells you the two proteins were bound.

To pin down exactly where transcription is happening, the method uses two probes at once: one targeting the transcript of interest, the other targeting the ribosome's 18S rRNA. Each carries a "clickable handle" (azide on the mRNA probe, tetrazine on the rRNA probe), connected through a deliberately short, semi-flexible 14-nucleotide linker. Add the PLA oligo, and the structure only closes into a ring — and gets amplified — when the two handles are close enough to touch. (Honestly, the fine mechanics of this are still a bit much for me too.) The upshot: a much cleaner, faster readout of transcriptional change than older methods.

## Where is tau made?

With this method, the authors watched where tau protein is produced and degraded inside a neuron.

Tau stabilizes the microtubule scaffold of the axon — that long extension of the neuron — the same "railway" that kinesin and dynein use to haul cargo back and forth. Given that, most people assumed tau was made in the cell body (the soma) and shipped out to the axon, or made locally right there near the axon. Older methods backed that up.

But when checked with this new method, tau turns out to be made in the dendrite instead — neither the axon nor the soma. That's strange, because the usual flow of a neural signal runs from the soma, down the axon, across the synapse, and into the next cell's dendrite, back toward that cell's soma. Tau is being mass-produced at the point furthest from where it's actually used.

Interestingly, one of the earliest signs of Alzheimer's is tau aggregation in the soma and dendrites. The old story was that axonal tau detaches, loses its mooring, and drifts back into the cell body. This result raises another possibility: maybe it's the tau made in the dendrites — and never put to use — that's aggregating.

## The neuroproteasome handles degradation

That brings in the second concept: a neuron-specific proteasome called the neuroproteasome.

Proteins get broken down by a barrel-shaped complex called the proteasome. The corresponding author, Kapil V. Ramachandran, first described the neuroproteasome as first author back in 2017 — it sits near the cell membrane, has a stripped-down structure, and degrades proteins fast.

Here, the authors show that tau made in the dendrites gets degraded by the neuroproteasome, and that blocking the neuroproteasome alone is enough to make tau phosphorylate and aggregate.

This same group published a paper last month, also in Nature Neuroscience, connecting ApoE, aging, and the neuroproteasome. Their signature move is taking the long-overlooked question of how neurodegenerative disease proteins are regulated at a fine-grained, subcellular level, and pairing it with tools like smFISH and PLA — each already in use separately — bundled into one method, STARFISH. That combination alone makes me look forward to whatever this lab puts out next. I genuinely enjoyed reading this one.
