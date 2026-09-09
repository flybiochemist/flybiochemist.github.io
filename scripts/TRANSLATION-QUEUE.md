# English translation queue

Progress on translating blog posts into English. Run translations with
`scripts/make_en_posts.py` — see its docstring for the calling convention.

## Scope

Translate **research and science posts only**. Skip lab-life, career and
personal entries (paper acceptances, getting scooped, blog recommendations,
diary posts) — they carry less for an international scientific audience and
the Korean originals stay available either way.

Untranslated posts need no placeholder: the listings filter on `lang`, so a
Korean-only post simply does not appear in `/year-archive/` or `/all-posts/`.

## Done

65 posts. Order worked so far: most recent science posts, then Parkinson's
(all science-tagged Parkinson's posts are now translated), then all twelve
posts from the 2026-09-09 Threads export, then twenty Alzheimer's/
molecular-biology posts across two batches:

Batch 1: brain organoids and assembloids, protein tagging methods, Down
syndrome and levetiracetam, the 40Hz monkey experiment, APOE4's lipid-
transport mechanism, the Selkoe-Small amyloid debate, dementia-driven
accelerated aging in the body, SETDB1/ERV/microglia in autism, the KAIST
40Hz reproducibility post, and the lithium-Alzheimer's sequestration
discovery.

Batch 2: five journal club paper picks, the cerebellum's role in sociality
(the fuller of two near-duplicate drafts — 2026-05-17-cerebellum-social-
behavior-autism.md is the same post, shorter, left untranslated), a rare
epilepsy ASO treatment and its rodent-model compromise, a conference
recap covering two-photon imaging/nanotubes/SVZ migration, why papers
should flag sex-chromosome genes, the 61-year Japanese dark-fly
experiment, an EBV paper salvaged from discarded sequencing data,
cell-free DNA for both prenatal testing and cancer screening, sickle
cell disease's hemoglobin fiber mechanism and treatments, and debunking
the "intelligence comes from the mother" myth.

## Next up — Alzheimer's and molecular biology (69 candidates remain)

Remaining candidates lean more toward personal/lab-life than earlier
batches did — screen for real science content before translating, per
the scope rule above. To list them:

```python
import io, os, yaml
SCI = {"alzheimers", "molecular-biology", "genetics", "neuroscience",
       "immunology", "stem-cells", "drosophila"}
for n in sorted(os.listdir("_posts")):
    fm = yaml.safe_load(io.open("_posts/"+n, encoding="utf-8").read().split("---")[1])
    if fm.get("lang") == "en" or fm.get("translation"):
        continue
    if set(fm.get("tags") or []) & SCI:
        print(fm.get("date"), n, fm.get("title"))
```

## Voice

Keep the original's tone — a scientist thinking out loud to a colleague, not
a formal abstract. Jokes and metaphors carry over rather than getting
flattened. Korean-reader-specific references (Korea Yakult, 백두산 as a unit
of altitude) get enough context to land in English, or a light equivalent.
