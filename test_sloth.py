import tempfile
import unittest
from pathlib import Path
from sloth import load_notes, validate, render


class BriefTests(unittest.TestCase):
    def test_grounded_actions(self):
        self.assertEqual(validate({'actions': [{'text': ' Review draft ', 'sources': [2, 1, 2]}]}, 2),
                         [{'text': 'Review draft', 'sources': [1, 2]}])

    def test_bad_references(self):
        for sources in [[], [0], [3], [True], ['1']]:
            with self.subTest(sources=sources), self.assertRaises(ValueError):
                validate({'actions': [{'text': 'Act', 'sources': sources}]}, 2)

    def test_bad_shape(self):
        for data in [[], {}, {'actions': 'no'}, {'actions': [None]}, {'actions': [{}]}]:
            with self.subTest(data=data), self.assertRaises(ValueError):
                validate(data, 1)

    def test_action_limit(self):
        with self.assertRaises(ValueError):
            validate({'actions': [{'text': 'x', 'sources': [1]}] * 6}, 1)

    def test_empty_directory(self):
        with tempfile.TemporaryDirectory() as directory, self.assertRaises(ValueError):
            load_notes(Path(directory))

    def test_read_only_and_order(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'b.txt').write_text('second', encoding='utf-8')
            (root / 'a.txt').write_text('first', encoding='utf-8')
            (root / 'ignore.md').write_text('ignore', encoding='utf-8')
            self.assertEqual(load_notes(root), [('a.txt', 'first'), ('b.txt', 'second')])
            self.assertEqual((root / 'b.txt').read_text(), 'second')

    def test_size_guard(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'a.txt').write_text('x' * 16001)
            with self.assertRaises(ValueError):
                load_notes(root)

    def test_source_audit(self):
        output = render([{'text': 'Review', 'sources': [1]}], [('note.txt', 'hello')], 'test')
        self.assertIn('2cf24dba5fb0', output)
        self.assertIn('[sources: 1]', output)


if __name__ == '__main__':
    unittest.main()
