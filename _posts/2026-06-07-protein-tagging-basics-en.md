---
title: "Putting a tag on a protein or molecule"
date: 2026-06-07
permalink: /en/posts/2026-06-07/
lang: en
translation: /posts/2026-06-07/
tags:
  - biology
  - molecular-biology
  - lab-tips
---

Molecular biology mostly looks at how human heredity breaks down into genes, how one or more genes on a chromosome get their expression regulated, how DNA is transcribed into RNA and translated into protein, and where that protein goes and what it does once it gets there.

DNA and RNA can be analysed quickly now, thanks to sequencing technology. Protein, though (mass spec aside), is still studied largely by analog means — using an antibody to see how much of it there is and where it sits in a cell or tissue.

## The limits of antibodies, and the arrival of the tag

But an antibody, being made against a specific part of a protein via an immune response, can fail to recognize a tertiary structure, or grab something other than what you wanted... For anything short of a famous protein, a decent antibody often just doesn't exist. More precisely, one exists, but its quality is far too poor for what you actually need it to do. So instead you attach a short sequence — a tag — for which an extremely well-established antibody already exists.

## Watching protein interactions with Co-IP

What can you do with this kind of tagging? Tag a protein that antibodies don't work well against, and you can check whether it binds other proteins. Tag protein A, pull A down with an antibody against the tag, and proteins B and C that were bound to A come along for the ride. This experiment, co-immunoprecipitation (Co-IP), lets you see fairly directly which proteins interact with each other. An applied version tags a protein characteristic of a particular organelle, so that Co-IP pulls down just that organelle, letting you fish out and analyse only its proteins and metabolites.

## Tracking location with fluorescent proteins

Another approach tags with a fluorescent protein. Attach GFP (green fluorescent protein), or one of its engineered variants that glow at other wavelengths (YFP, RFP, and so on), to the protein you want to watch, and you can track where it moves inside the cell by its light. Does it go into the nucleus? Does it stay at the membrane? How does it redistribute during division? In principle you can watch all of this continuously under a microscope.

## The price of the tag

Tags are not free. Sticking extra baggage onto a protein sometimes wrecks its original function or location — GFP especially, being a large protein. Attach a roughly 27 kDa GFP to a protein of, say, 30-60 kDa, and it may fail to reach where it needs to go (staying in the cytoplasm when it should enter the nucleus, for instance) or fail to fold into its proper structure.

Because attaching it at the N-terminus (front end) especially tends to block a protein's movement, people generally consider the C-terminus (back end) instead — and if that doesn't work, the real trouble begins. Reviewers often end up asking you to verify, at the very end and with an ordinary antibody, that the tagged protein really behaves like the untagged one. Ironic, isn't it.

## Choosing the right tag for the job

So unless you actually need to watch it live under a microscope, a small tag is the wiser choice. Short sequences of around ten amino acids — FLAG, HA, Myc, V5 — put almost no burden on the protein. If purification is the goal instead, a His-tag (a run of histidines) is used to exploit its electrical affinity for a nickel column. Big tag, small tag, purification tag — you choose based on the job.

There are also tags that stay quiet until exposed to light or a particular enzyme, tags that only fluoresce once two proteins come together, and technologies like APEX or BioID that label only the proteins sitting near the tag, recording "who spent time next to this protein" across space and time. All of these are experimental methods built on tagging.

## Closing question

So, to everyone running experiments — what's your favourite tag?
