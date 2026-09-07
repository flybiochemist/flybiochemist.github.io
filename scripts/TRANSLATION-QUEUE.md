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

33 posts. Order worked so far: most recent science posts, then Parkinson's
(all science-tagged Parkinson's posts are now translated).

## Next up — Alzheimer's and molecular biology

To list remaining candidates:

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
