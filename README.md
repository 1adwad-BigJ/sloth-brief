# Sloth Brief

A small local AI assistant that turns accumulated text notes into five or fewer
source-linked actions. Built for the DEV Week 3 “Slow and Steady” theme.

## Run

Python 3.10+ and a locally running Ollama with an open-weight model are required.
No Python dependencies, cloud keys or paid services. Install Ollama from its
official site and choose a model whose license you accept. Default model is
`qwen2.5:0.5b`. Model downloads require internet and disk space; subsequent
inference runs locally. Do not use a cloud-backed model for private notes.

```sh
ollama pull qwen2.5:0.5b
python sloth.py examples/notes --output brief.md
python -m unittest -v
```

The output must not already exist. Inputs are never modified. Only top-level
`.txt` files are read; symlinks are skipped. Limits: 20 files, 16 KB per file,
24,000 total characters. Requests go only to loopback, without environment proxies.

## Why open AI

The model performs semantic consolidation; rules alone cannot connect arbitrary
notes into useful actions. Ollama and swappable open-weight models let users
keep text on their machine and inspect or replace the inference layer.

## Limitations

Source IDs are validated, but citations do not prove semantic accuracy. Review
the source notes. Prompt injection can influence a summary; the model has no
tools, filesystem writes or execution powers. Output is plain Markdown and
should not be rendered with unrestricted HTML. Model inference is not yet
verified on this workstation; automated tests cover validation and file handling.

Created with Codex assistance. Synthetic demo inputs contain no client data.
See DEV-SUBMISSION.md for the unpublished contest draft.

## Direct Transformers runtime (no Ollama server)

```sh
python -m venv .venv
# Activate the environment, then:
pip install -r requirements.txt
python sloth.py examples/notes --runtime transformers --model Qwen/Qwen2.5-0.5B-Instruct --output brief.md
```

The first run downloads public Apache-2.0 Qwen weights from Hugging Face.
No hosted inference or payment account is used. Notes remain local. Model source:
https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct
Repository: https://github.com/1adwad-BigJ/sloth-brief
