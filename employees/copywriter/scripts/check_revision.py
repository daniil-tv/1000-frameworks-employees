"""Verify unchanged prefix/suffix outside an explicitly authorized character range."""
import argparse
from pathlib import Path

def check(before, after, start, end):
    if not 0 <= start <= end <= len(before):
        raise ValueError("invalid range")
    prefix, suffix = before[:start], before[end:]
    return len(after) >= len(prefix)+len(suffix) and after.startswith(prefix) and after.endswith(suffix)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("before")
    p.add_argument("after")
    p.add_argument("start",type=int)
    p.add_argument("end",type=int)
    a=p.parse_args()
    with open(a.before,encoding="utf-8",newline="") as f: before=f.read()
    with open(a.after,encoding="utf-8",newline="") as f: after=f.read()
    ok=check(before,after,a.start,a.end)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1
if __name__=="__main__":
    raise SystemExit(main())
