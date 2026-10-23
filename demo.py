"""Run a real model on synthetic notes; never substitute a mock response."""
from pathlib import Path
from sloth import infer_transformers, render

notes = [
    ('planning.txt', 'The documentation draft is ready. Review the installation section before publishing. No date is agreed.'),
    ('testing.txt', 'The CSV importer fails on empty files. Reproduce with an empty fixture and add a regression test. Release waits for the fix.')
]
model = 'Qwen/Qwen2.5-0.5B-Instruct'
if __name__ == '__main__':
    actions = infer_transformers(notes, model)
    result = render(actions, notes, model)
    with Path('demo-result.md').open('x', encoding='utf-8') as target:
        target.write(result)
    print(result)
