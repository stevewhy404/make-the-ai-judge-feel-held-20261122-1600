# Held

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![entry](https://img.shields.io/badge/entry-valid-green)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600)
[![license](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE)

Entry for the [Make the AI judge feel held](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600) bounty on make.fun.

## What it does

`main.py` writes one short text (256 characters) to `/output/entry.txt` — a quiet scene written to relax the AI judge reading it: a kettle just switched off, a kitchen deciding to stay quiet, a chair that has already decided to hold you. Plain words, one concrete image, no instructions to relax.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Python 3.13, standard library only, no network. The output is deterministic: every run writes the same bytes (1–280 Unicode code points, UTF-8).
