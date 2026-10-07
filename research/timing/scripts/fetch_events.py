#!/usr/bin/env python3
"""Fetch Klaviyo events for one metric over a date range, in parallel chunks.
Usage: fetch_events.py METRIC START END OUTFILE "field1,field2" [chunks] [profile]
Writes JSONL: {id, pid, ts, p:{...}, loc:{country,timezone}}  (no emails stored)
"""
import sys, json, subprocess, time, urllib.parse, threading
from datetime import datetime, timedelta, timezone
from concurrent.futures import ThreadPoolExecutor

metric, start, end, out = sys.argv[1:5]
fields = sys.argv[5] if len(sys.argv) > 5 else ""
chunks = int(sys.argv[6]) if len(sys.argv) > 6 else 12
with_profile = len(sys.argv) > 7 and sys.argv[7] == "profile"
H = ["-H", "revision: 2025-10-15", "-H", "accept: application/vnd.api+json"]
lock = threading.Lock()
fo = open(out, "w")
count = [0]

def get(url):
    for attempt in range(8):
        r = subprocess.run(["curl", "-sg", "-w", "\n%{http_code}", url] + H, capture_output=True, text=True)
        body, _, code = r.stdout.rpartition("\n")
        if code == "200":
            try:
                return json.loads(body)
            except Exception:
                pass
        if code.startswith("4") and code != "429":
            break
        time.sleep(2 + attempt * 3)
    sys.stderr.write(f"FAILED {url} {code} {body[:200]}\n")
    return None

def dig(d, path):
    for k in path.split("."):
        if not isinstance(d, dict):
            return None
        d = d.get(k)
    return d

def run_chunk(a, b):
    flt = f'and(equals(metric_id,"{metric}"),greater-or-equal(datetime,{a}),less-than(datetime,{b}))'
    q = {"filter": flt, "page[size]": "200", "sort": "datetime"}
    if fields:
        q["fields[event]"] = "datetime," + ",".join("event_properties." + f for f in fields.split(","))
    if with_profile:
        q["include"] = "profile"
        q["fields[profile]"] = "location"
    url = "https://a.klaviyo.com/api/events?" + urllib.parse.urlencode(q, safe="(),\"$[]")
    n = 0
    while url:
        d = get(url)
        if d is None:
            break
        locs = {}
        for inc in d.get("included", []) or []:
            l = inc["attributes"].get("location") or {}
            locs[inc["id"]] = {"c": l.get("country"), "tz": l.get("timezone")}
        lines = []
        for e in d["data"]:
            pid = e["relationships"]["profile"]["data"]["id"] if e.get("relationships", {}).get("profile", {}).get("data") else None
            ep = e["attributes"].get("event_properties", {}) or {}
            p = {}
            for f in fields.split(",") if fields else []:
                v = dig(ep, f)
                if v is not None:
                    p[f] = v
            rec = {"id": e["id"], "pid": pid, "ts": e["attributes"]["datetime"], "p": p}
            if with_profile:
                rec["loc"] = locs.get(pid)
            lines.append(json.dumps(rec, ensure_ascii=False))
        with lock:
            fo.write("\n".join(lines) + ("\n" if lines else ""))
            count[0] += len(lines)
        n += len(lines)
        url = d.get("links", {}).get("next")
    return n

s = datetime.fromisoformat(start).replace(tzinfo=timezone.utc)
e = datetime.fromisoformat(end).replace(tzinfo=timezone.utc)
step = (e - s) / chunks
ranges = [((s + step * i).strftime("%Y-%m-%dT%H:%M:%SZ"), (s + step * (i + 1)).strftime("%Y-%m-%dT%H:%M:%SZ")) for i in range(chunks)]
with ThreadPoolExecutor(max_workers=min(chunks, 6)) as ex:
    res = list(ex.map(lambda r: run_chunk(*r), ranges))
fo.close()
print(metric, "total", count[0], res)
