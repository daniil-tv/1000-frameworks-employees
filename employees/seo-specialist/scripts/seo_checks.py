"""Offline checks. Python 3.10+, standard library only."""
import argparse
import csv
import json
import sys
from urllib.parse import urlsplit, urlunsplit

def normalize_query(s):
    return " ".join(s.casefold().split())

def dedupe(rows):
    seen, clean, duplicates = set(), [], []
    for row in rows:
        if not row.get("query", "").strip():
            raise ValueError("empty query")
        key = (normalize_query(row["query"]), *(row.get(k, "") for k in ("engine","region","device","frequency_type","source","measured_at","frequency")))
        if key in seen:
            duplicates.append(row)
        else:
            seen.add(key)
            clean.append(row)
    return {"rows": clean, "duplicates": duplicates}

def canonical_key(url):
    p = urlsplit(url)
    if p.scheme not in ("http","https") or not p.netloc:
        raise ValueError("absolute HTTP(S) URL required")
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), p.path or "/", p.query, ""))

def overlap(a, b):
    x, y = set(map(canonical_key,a)), set(map(canonical_key,b))
    if not x or not y:
        raise ValueError("empty SERP")
    return {"shared": len(x & y), "jaccard": len(x & y)/len(x | y), "overlap_coefficient": len(x & y)/min(len(x),len(y))}

def validate(rows, required):
    return [{"row": i+2,"missing": missing} for i,row in enumerate(rows) if (missing := [k for k in required if not row.get(k,"").strip()])]

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("mode", choices=["dedupe","overlap","validate"])
    p.add_argument("input")
    p.add_argument("--required", default="query,source,measured_at")
    a=p.parse_args()
    with open(a.input, encoding="utf-8-sig", newline="") as f:
        if a.mode=="overlap":
            d=json.load(f); result=overlap(d["a"],d["b"])
        else:
            reader=csv.DictReader(f)
            required=a.required.split(",") if a.mode=="validate" else ["query","engine","region","device","frequency_type","source","measured_at","frequency"]
            if not set(required).issubset(reader.fieldnames or []):
                raise ValueError("missing headers")
            rows=list(reader)
            result=dedupe(rows) if a.mode=="dedupe" else {"errors":validate(rows,required)}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return int(a.mode=="validate" and bool(result["errors"]))
if __name__=="__main__":
    sys.exit(main())
