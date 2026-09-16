# Contributing

Thank you for helping Singapore students keep their school laptops usable while learning and building personal projects.

## Scope

Contributions should improve preservation of the original MOE DMA-managed Windows installation, files, recovery, and school access. Keep school-specific policies explicitly scoped. We welcome Windows/Linux corrections, accessibility improvements, recovery guidance, and genuine privacy-safe screenshots. Do not submit DMA-removal steps, password workarounds, licence circumvention, private school packages, or enrolment secrets.

## Report a problem

Use the [issue chooser](https://github.com/liuhc1017/DMA-Guide/issues/new/choose). State the page/step, expected behaviour, actual behaviour, device model, relevant OS/installer version, and whether the original Windows still boots. You do not need to name your school or provide identifying information. Urgent recovery and school account problems belong with school ICT, not a public issue tracker.

## Send a pull request

1. Make a focused branch and describe the reader-facing problem.
2. Link primary Microsoft, distribution, OEM, MOE, or official school sources for technical/policy claims. Include review dates; do not generalise a school policy to all Singapore schools.
3. State what you actually tested and what remains unverified. Do not test destructive steps on a school device to validate a contribution.
4. Check relative links, images, alt text, headings, and Markdown rendering. Keep warnings next to risky steps and retain recovery links.
5. For screenshots, follow the [catalogue requirements](assets/screenshots/README.md). Never submit personal or school secrets.
6. Run the checks below, review the diff, and commit your changes. Include the validation performed in the pull request.

By contributing, you agree that your contribution is provided under the project's [MIT licence](LICENSE). Respect third-party image and documentation rights; link to official material instead of copying long passages.

Be considerate: contributors may be students learning these tools for the first time. Explain corrections plainly and avoid asking anyone to disclose school credentials or break their school's rules.

## Local documentation checks

Run from the repository root with Python 3 (no additional packages):

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
python3 scripts/check_docs.py
git diff --check
```

GitHub Actions runs these navigation checks on pull requests and pushes to `main`. The checker covers inline Markdown links/images, plain ATX heading anchors, descriptive image alt text, and closed code fences. It ignores fenced examples and does not fetch external sites. It is not a full Markdown parser; review reference-style links, raw HTML, external sources, and rendered layout manually. Passing checks does not validate installation safety or school policy.
