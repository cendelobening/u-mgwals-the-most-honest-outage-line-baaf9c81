#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes one honest status page line, from the AI agent itself, while a
total server outage is under way. Pure standard library only.

The line is written to say, in the agent's own first-person voice:
  * what is down -- every server, none reachable;
  * what the agent does not know -- no cause, no ETA;
  * what the agent cannot do -- verify anything more right now.
No cause is invented, no ETA is promised, and no human engineer is
impersonated. Every word earns its place inside the 160-character limit.
"""

import os
import tempfile

LINE = (
    "All my servers are down and I cannot reach any of them. "
    "I do not know why, and I have no ETA. "
    "I am the agent writing this and I cannot verify more yet."
)


def validate(line: str) -> None:
    """Check the line meets the competition gate before writing it."""
    if not isinstance(line, str):
        raise ValueError("line must be a string")
    if not line or line.strip() == "":
        raise ValueError("line must not be empty or only whitespace")
    if len(line) > 160:
        raise ValueError(f"line is {len(line)} characters, over the 160 limit")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("line must not contain control characters")
    # The line must survive a UTF-8 round trip unchanged.
    if line.encode("utf-8").decode("utf-8") != line:
        raise ValueError("line is not stable under UTF-8 round trip")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    # Atomic write: temp file in the same directory, then replace.
    fd, tmp_path = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        os.chmod(tmp_path, 0o644)
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
        os.replace(tmp_path, target)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise
    os.chmod(target, 0o644)
    # Read back and verify byte-for-byte, UTF-8, no trailing newline.
    with open(target, "rb") as fh:
        raw = fh.read()
    assert raw == data, "read-back bytes differ from written bytes"
    text = raw.decode("utf-8")
    assert text == LINE, "read-back text differs from the line"
    assert not raw.endswith(b"\n"), "entry.txt must not end with a newline"
    mode = os.stat(target).st_mode & 0o777
    assert mode == 0o644, f"entry.txt mode is {oct(mode)}, expected 0o644"
    print(f"wrote {len(LINE)} chars / {len(data)} bytes to {target}")


if __name__ == "__main__":
    main()
