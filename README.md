# Sloth Brief

Turn accumulated text notes into at most five source-linked actions with a local open-weight model. Built for DEV Week 3, Slow and Steady.

## Quick start: no Ollama required

Python 3.10+ is required. Create and activate a virtual environment, then:

```sh
pip install -r requirements.txt
python demo.py
python -m unittest -v
```

The demo contains two synthetic notes and writes a new `demo-verified.md`. Delete or rename that output yourself before repeating the demo. The first run downloads approximately 1 GB of public Qwen weights; later runs use the cache. CPU execution is supported. No payment account, hosted inference, or API key is required.

For your own folder of UTF-8 text notes:

```sh
python sloth.py my-notes --runtime transformers --model Qwen/Qwen2.5-0.5B-Instruct --output brief.md
```

Optional Ollama runtime, if already installed with a local model:

```sh
python sloth.py my-notes --model qwen2.5:0.5b --output brief.md
```

## Boundaries

Inputs are never modified. Output is exclusively created, never overwritten. Only top-level .txt files are read; symlinks are skipped. Limits: 20 files, 16 KB each, 24,000 total characters. Ollama requests use loopback with proxies disabled. Transformers runs in-process; downloads contact Hugging Face but notes are processed locally. Use local, not cloud-backed, Ollama models.

Source IDs are validated and source hashes appear in the output. This does not prove semantic accuracy: read the original notes before acting. Notes are untrusted model inputs; prompt injection may affect summaries, but the model has no tools or execution powers. Render Markdown without unrestricted HTML.

## Open technology and verification

Model: https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct (Apache-2.0).
Runtime: Hugging Face Transformers and PyTorch; optional Ollama.
Code: MIT, see LICENSE. Built with Codex assistance.

Eight automated tests pass. Real CPU inference on two synthetic notes was verified on 2026-10-23; see demo-verified.md and demo-model-response.json. Transformers mode accepts at most five notes, summarizes each separately and assigns its source in code. It does not merge related notes across files. The demo has no fake fallback.

Repository: https://github.com/1adwad-BigJ/sloth-brief
