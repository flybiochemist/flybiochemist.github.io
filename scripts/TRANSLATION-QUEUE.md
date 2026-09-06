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

23 posts. Order worked so far: most recent science posts, then Parkinson's.

## Next up — Parkinson's, science-focused

- [ ] 2026-04-25 알츠하이머와 파킨슨에서 떠오르는 지질대사체 연구
- [ ] 2026-04-05 암을 따라가는 알츠하이머, 알츠하이머를 따라가는 파킨슨
- [ ] 2025-09-16 파킨슨 유병률의 환경적 요인
- [ ] 2025-09-15 헤모글로빈이 적혈구 아닌데도 있다구요?
- [ ] 2025-05-10 교과서 속 미토콘드리아는 지하철 노선도 같은 것
- [ ] 2025-03-16 쥐 모델의 검증과 검증과 검증
- [ ] 2025-01-16 생존자 편향과 파킨슨 쥐 모델
- [ ] 2024-06-13 Autism과 지적장애에서 파킨슨병 확률이 3배?
- [ ] 2024-05-16 파킨슨 병의 역사에 대한 재밌는 이야기들
- [ ] 2024-02-07 퇴행성뇌질환 쥐 모델의 변비를 재는 법

## After that

Alzheimer's and molecular biology posts. To list remaining candidates:

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
