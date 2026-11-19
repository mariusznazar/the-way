import re, subprocess, sys, unittest, json
from pathlib import Path
directory = Path(sys.argv[1]).resolve()
out = Path(sys.argv[2])
sys.path.insert(0, str(directory))
real = subprocess.run
records = []
def wrapper(args, *a, **k):
    result = real(args, *a, **k)
    if isinstance(args, list) and any(str(x).endswith("plan_state.py") for x in args):
        norm = lambda t: re.sub(r"plan state \w+", "plan state X", (t.decode("utf-8","replace") if isinstance(t, bytes) else t).replace("\\", "/"))
        records.append([result.returncode, norm(result.stdout), norm(result.stderr)])
    return result
subprocess.run = wrapper
import test_plan_state
suite = unittest.defaultTestLoader.loadTestsFromModule(test_plan_state)
res = unittest.TextTestRunner(verbosity=0).run(suite)
out.write_text(json.dumps(records, indent=1), encoding="utf-8")
print(len(records), res.wasSuccessful())
