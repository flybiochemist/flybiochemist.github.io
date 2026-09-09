---
title: "Why the same calculation gives a different answer on a different number of CPU cores"
date: 2026-09-01
permalink: /en/posts/2026-09-01-2/
lang: en
translation: /posts/2026-09-01-2/
tags:
  - biology
  - molecular-biology
---

A friend in the lab develops software that predicts genes and the compounds likely to act on them, and kept running into a strange problem: a 40-core machine and a 64-core machine kept returning different values.

Tracking it down: the computation truncates the result past a certain decimal place at each step. Do 40 operations at a time and truncate, versus doing them 64 at a time — the longer the calculation runs and the more rounding steps accumulate, the further the two diverge.

Fascinating once you know why; feels like the world is broken until you do. There is a lot like that out there.

## References

<!-- TODO: add link -->
