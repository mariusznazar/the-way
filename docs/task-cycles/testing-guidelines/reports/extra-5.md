- This slice touches the trust boundary `installation/install.py`: a fresh reviewer reviews it on
  its own, checking crafted input at that boundary (a foreign file, a directory or a non-UTF-8 file
  at the new entry-point path, and the `AGENTS.md` block and sibling entry points it rewrites).
- C9: the existing crafted non-UTF-8 case stops on an uncaught `UnicodeDecodeError`; the new test
  copies that assertion and this slice does not change the installer's decoding. Name it in your
  report.
