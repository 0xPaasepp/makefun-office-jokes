# Office Jokes entry: one deterministic one-liner, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
import os

JOKE = "My out-of-office reply just says \"per my last email\" \u2014 even my vacation is passive-aggressive now."

OUTPUT_PATH = "/output/entry.txt"

os.makedirs("/output", exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
    handle.write(JOKE)
