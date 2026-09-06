#!/usr/bin/env python3
"""Create English twins for selected Korean posts and pair them up.

Usage: write a small batch script that imports build() and passes a dict of
    stem -> (english title, english body)
where stem is the Korean post's filename without .md. For example:

    from make_en_posts import build
    build({"2026-07-07-ank2-astrocyte-long-term-memory":
           ("Ank2 and astrocytes", "Body text in markdown...")})

For each entry this reads date / permalink / tags from the Korean original,
writes _posts/<stem>-en.md at /en/<korean permalink>, and adds lang plus
translation to both files so the masthead language button links them.

The blog listings filter on lang, so an untranslated post simply stays
Korean-only: /year-archive/ and /all-posts/ show lang: en posts, while
/ko/blog/ and /ko/all-posts/ show everything else.

Re-running is safe: it rewrites the twin and refreshes the pairing.
"""

import io
import os
import re
import sys

POSTS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_posts")


def split_fm(text):
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("no front matter")
    return parts[1], parts[2]


def field(fm, key):
    m = re.search(r"^%s:\s*(.*)$" % key, fm, re.M)
    return m.group(1).strip() if m else None


def tags_of(fm):
    m = re.search(r"^tags:\s*\n((?:\s*-\s*.*\n?)+)", fm, re.M)
    return [l.strip()[2:].strip() for l in m.group(1).strip().splitlines()] if m else []


def upsert(fm, key, value):
    """Set key in front matter, inserting before `tags:` if absent."""
    if re.search(r"^%s:\s*.*$" % key, fm, re.M):
        return re.sub(r"^%s:\s*.*$" % key, "%s: %s" % (key, value), fm, count=1, flags=re.M)
    if re.search(r"^tags:", fm, re.M):
        return re.sub(r"^tags:", "%s: %s\ntags:" % (key, value), fm, count=1, flags=re.M)
    return fm.rstrip("\n") + "\n%s: %s\n" % (key, value)


def build(translations):
    files = os.listdir(POSTS)
    made = []
    for stem, (en_title, en_body) in translations.items():
        src = stem + ".md"
        if src not in files:
            sys.exit("no such post: %s" % src)
        ko_path = os.path.join(POSTS, src)
        ko_text = io.open(ko_path, encoding="utf-8").read()
        ko_fm, _ = split_fm(ko_text)

        date = field(ko_fm, "date")
        ko_link = field(ko_fm, "permalink")
        if not date or not ko_link:
            sys.exit("%s missing date or permalink" % src)
        en_link = "/en" + ko_link
        tags = tags_of(ko_fm)

        # English twin
        out = ['---', 'title: "%s"' % en_title.replace('"', '\\"'),
               'date: %s' % date, 'permalink: %s' % en_link,
               'lang: en', 'translation: %s' % ko_link]
        if tags:
            out.append("tags:")
            out += ["  - %s" % t for t in tags]
        out.append("---")
        en_path = os.path.join(POSTS, stem + "-en.md")
        io.open(en_path, "w", encoding="utf-8", newline="\n").write(
            "\n".join(out) + "\n\n" + en_body.strip() + "\n")

        # pair the Korean original back
        new_fm = upsert(upsert(ko_fm, "lang", "ko"), "translation", en_link)
        io.open(ko_path, "w", encoding="utf-8", newline="\n").write(
            "---" + new_fm + "---" + split_fm(ko_text)[1])

        made.append((stem, en_link, ko_link))

    for stem, en, ko in made:
        print("  %-52s %s  <->  %s" % (stem[:52], en, ko))
    print("\n%d English post(s) written and paired" % len(made))
