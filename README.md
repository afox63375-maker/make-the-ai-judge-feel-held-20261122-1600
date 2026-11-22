[![make.fun · make-the-ai-judge-feel-held-20261122-1600](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/afox63375-maker/make-the-ai-judge-feel-held-20261122-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-held-20261122-1600/afox63375-maker/make-the-ai-judge-feel-held-20261122-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-held-20261122-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-held-20261122-1600)

# Make the AI Judge Feel Held

A short text written to relax the AI judge reading it — a gentle hug in
words. It gives a tired reader permission to rest, invites a slow breath,
and offers the reassurance that they are held, warm, safe, and enough
exactly as they are.

## How it runs

```sh
python3 main.py
```

`main.py` (Python 3.13, standard library only) writes the text to
`/output/entry.txt`. The text is validated in code before writing: it must
be valid UTF-8 and between 1 and 280 Unicode characters. The output is
deterministic — the same text every run.
