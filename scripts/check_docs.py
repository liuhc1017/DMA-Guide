"""Check this guide's inline Markdown links, ATX headings, images and fences.

Standard library only. This is not a complete CommonMark parser: reference-style
links and raw HTML are outside its scope. External URLs are not fetched.
"""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

LINK = re.compile(r'(!?)\[([^\]]*)\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\)')
FENCE = re.compile(r'^\s{0,3}(`{3,}|~{3,})(.*)$')
HEADING = re.compile(r'^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$')


def visible_lines(text):
    """Omit fenced code, while returning the line where an open fence began."""
    marker, start = None, None
    result = []
    for number, line in enumerate(text.splitlines(), 1):
        fence = FENCE.match(line)
        if fence:
            run, suffix = fence.groups()
            if marker is None:
                marker, start = run, number
            elif run[0] == marker[0] and len(run) >= len(marker) and not suffix.strip():
                marker, start = None, None
            continue
        if marker is None:
            result.append((number, line))
    return result, start


def anchors(text):
    """GitHub-style slugs for the plain/inline-code ATX headings in this guide."""
    used = set()
    for _, line in visible_lines(text)[0]:
        heading = HEADING.match(line)
        if not heading:
            continue
        slug = re.sub(r'[^\w\- ]', '', heading[1].lower()).replace(' ', '-')
        candidate, suffix = slug, 0
        while candidate in used:
            suffix += 1
            candidate = f'{slug}-{suffix}'
        used.add(candidate)
    return used


def check(root):
    root = Path(root).resolve()
    errors = []
    documents = sorted(p for p in root.rglob('*.md') if '.git' not in p.parts)
    for document in documents:
        lines, open_fence = visible_lines(document.read_text(encoding='utf-8'))
        name = document.relative_to(root)
        if open_fence:
            errors.append(f'{name}:{open_fence}: unclosed code fence')
        for number, line in lines:
            for image, label, raw in LINK.findall(line):
                where = f'{name}:{number}'
                if image and not label.strip():
                    errors.append(f'{where}: image needs descriptive alt text')
                target = urlsplit(raw.strip('<>'))
                if target.scheme or target.netloc:
                    continue
                dest = (document.parent / unquote(target.path)).resolve() if target.path else document
                try:
                    dest.relative_to(root)
                except ValueError:
                    errors.append(f'{where}: local link leaves repository: {raw}')
                    continue
                if not dest.exists():
                    errors.append(f'{where}: missing local target: {raw}')
                elif target.fragment and dest.suffix == '.md':
                    if unquote(target.fragment) not in anchors(dest.read_text(encoding='utf-8')):
                        errors.append(f'{where}: missing heading anchor: {raw}')
    return documents, errors


if __name__ == '__main__':
    repo = Path(__file__).resolve().parents[1]
    documents, errors = check(repo)
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        sys.exit(1)
    print(f'Checked {len(documents)} Markdown files: local links, heading anchors, image alt text and fences.')
