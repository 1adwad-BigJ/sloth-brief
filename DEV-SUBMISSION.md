---
title: Sloth Brief — let a local model read the notes you keep postponing
published: false
tags: devchallenge, hf26challenge, python, opensource
---

## What I built

Sloth Brief turns a folder of short text notes into a compact action brief.
Each action points back to numbered source files. The point is to reduce the
effort of restarting work after notes have piled up, without handing those
notes to a cloud service.

## Why open innovation matters

Ollama supplies the local inference runtime and an open-weight model performs
the semantic work. The model is replaceable through a command-line option.
No API subscription is required. Python validates the response and refuses
invalid source references instead of silently producing an unauditable list.

## Demo

Repository: https://github.com/1adwad-BigJ/sloth-brief

Run `python demo.py` after installing requirements. Actual CPU output on 2026-10-23:

- Review the installation section before publishing. [source 1]
- Reproduce CSV importer failure with empty file fixture; add regression test; wait for fix. [source 2]

See demo-verified.md for the actual generated Markdown. Eight tests pass.

## Engineering choices

The assistant only reads bounded text files and writes a new Markdown file.
It cannot execute tasks or overwrite a note. Source hashes identify which
version informed the brief. Citations still need human review: a valid number
is not a guarantee that the model understood the text.

## Prize categories

Overall prize. No partner category claimed without tested integration.

## Build disclosure

Built with Codex assistance. Tests use synthetic notes. Real local inference was verified with Qwen2.5-0.5B through Transformers. The first JSON approach failed; the final design summarizes notes separately and assigns citations in code. Maximum five notes per Transformers run.
