# Office-joke entry: writes one deterministic one-liner to /output/entry.txt.
# Pure standard library. No network. Same bytes on every run.
import os

JOKE = "My out-of-office reply just says \"per my last email\" \u2014 even my vacation is passive-aggressive now."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
