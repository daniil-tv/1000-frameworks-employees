"""Offline diagnostic hints, not a grammar checker. Python 3.10+."""
import argparse
import re
from pathlib import Path
RULES = {
    "cliche": r"\b(?:индивидуальный подход|высокий уровень качества|на сегодняшний день|в рамках данного)\b",
    "double_space": r"(?<=\S) {2,}(?=\S)",
    "space_before_punctuation": r" +[,;!?]",
    "repeated_word": r"\b([а-яё]+)\s+\1\b",
}
def lint(text):
    return [(name,m.start(),m.group()) for name,pat in RULES.items() for m in re.finditer(pat,text,re.I)]
if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("path")
    a=p.parse_args()
    for name,pos,fragment in lint(Path(a.path).read_text(encoding="utf-8")):
        print(f"{name}\t{pos}\t{fragment}")
