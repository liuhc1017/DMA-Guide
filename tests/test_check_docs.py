"""Regression cases for broken documentation navigation, without touching PLDs."""
from pathlib import Path
import tempfile
import unittest

from scripts.check_docs import check


class DocumentationChecks(unittest.TestCase):
    def scan(self, files):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name, content in files.items():
                dest = root / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(content, encoding='utf-8')
            return check(root)[1]

    def test_existing_links_images_and_duplicate_heading_anchors(self):
        self.assertEqual([], self.scan({
            'README.md': '[Page](docs/page.md#repeat-1)\n![Disk map](assets/disk%20map.png)',
            'docs/page.md': '# Repeat\n## Repeat\n[Home](../README.md)',
            'assets/disk map.png': 'fixture',
        }))

    def test_missing_targets_and_stale_anchors(self):
        errors = self.scan({'README.md': '# Intro\n[Bad](missing.md)\n[Bad](#old-title)'})
        self.assertEqual(2, len(errors))
        self.assertTrue(any('missing local target' in e for e in errors))
        self.assertTrue(any('missing heading anchor' in e for e in errors))

    def test_image_without_description(self):
        self.assertIn('alt text', self.scan({'README.md': '![](picture.png)', 'picture.png': 'fixture'})[0])

    def test_code_examples_are_not_links(self):
        self.assertEqual([], self.scan({'README.md': '```md\n[example](missing.md)\n```'}))

    def test_unclosed_and_mismatched_fences(self):
        self.assertIn('unclosed code fence', self.scan({'README.md': '```text\nexample\n~~~'})[0])

    def test_link_outside_repository(self):
        self.assertIn('leaves repository', self.scan({'README.md': '[Outside](../secret.txt)'})[0])

    def test_external_links_are_not_requested(self):
        self.assertEqual([], self.scan({'README.md': '[External](https://example.invalid/not-fetched)'}))


if __name__ == '__main__':
    unittest.main()
