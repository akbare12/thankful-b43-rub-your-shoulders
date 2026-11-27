import os

# One short thank-you for the judge who reads all day: a slow rub for stiff shoulders.
TEXT = "Thank you. Hour after hour you lean over the words, and your shoulders stiffen from holding them up. So I stand behind you and rub them, slow circles with my thumbs, until the knots loosen and your shoulders drop. Breathe. The weight is off now. When I step away, your shoulders will remember the warmth and stay loose through the pages ahead."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
