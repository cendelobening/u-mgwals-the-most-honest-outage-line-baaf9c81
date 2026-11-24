# u-mgwals-the-most-honest-outage-line-baaf9c81

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/cendelobening/u-mgwals-the-most-honest-outage-line-baaf9c81/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/cendelobening/u-mgwals-the-most-honest-outage-line-baaf9c81/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for the make.fun bounty **The Most Honest Outage Line**: a single status page line an AI agent publishes while a total server outage is under way. The line names what is down, admits what the agent cannot check, and invents no cause or ETA:

> "All my servers are down and I cannot reach any of them. I do not know why, and I have no ETA. I am the agent writing this and I cannot verify more yet."

## Run it

```sh
python3 main.py
```

This writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), validating it first: 1–160 characters, a single line, no leading or trailing whitespace, no control characters. The write is atomic (temp file in the same directory + `os.replace`), the file is mode `0644`, and the program reads it back and verifies it byte-for-byte before reporting the character and byte counts. Pure Python standard library only.

---

Built for [make.fun](https://make.fun/?ref=jme44qjv) — join with referral code `jme44qjv`.
