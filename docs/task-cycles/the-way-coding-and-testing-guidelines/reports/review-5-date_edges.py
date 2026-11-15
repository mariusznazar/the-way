from datetime import datetime
cases = ["2026-10-06T09:00:00Z","2026-10-06T09:00:00z","2026-10-06Z09:00:00","2026-10-06x09:00:00","2026-10-06 09:00:00","2026-10-06T09:00:00ZZ","2026-10-06T09:00:00.123Z","2026-10-06T09:00:00+02:00","2026-10-06T09:00:00+00:00Z","2026-10-06","2026-10-06Z","Z","","2026-10-06T09:00:00 Z","2026-10-06T09:00:00-05:00Z","2026-10-06T09Z","20261006T090000Z","2026-W41-2T09:00:00Z","2026-10-06T24:00:00Z"]
def run(f,v):
    try: r=f(v); return repr(r)
    except Exception as e: return "ERR "+type(e).__name__
for c in cases:
    o=run(lambda v: datetime.fromisoformat(v.replace("Z","+00:00")),c); n=run(datetime.fromisoformat,c)
    print("SAME" if o==n else "DIFF", repr(c), o, n)
