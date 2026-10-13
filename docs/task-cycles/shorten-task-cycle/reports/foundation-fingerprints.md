# Direct final fingerprint comparison

Computed from the exact final binding paragraphs using relation-model/fingerprint.py.

| Entry | Fingerprint |
|---|---|
| WAY-11 | e882a9df |
| WAY-136 | e9ca5dac |
| WAY-148 | 2a5f9057 |
| WAY-149 | 6c02ef48 |

## Every affected reference in the whole foundation

| File:line | Reference | Expected | Result |
|---|---|---|---|
| foundations/decisions.md:3661 | WAY-11@e882a9df | e882a9df | match |
| foundations/invariants.md:222 | WAY-11@e882a9df | e882a9df | match |

WAY-136, WAY-148 and WAY-149 have no fingerprint-bearing dependants in the final foundation.

## New decisions and all retained relation targets

| Dependant | Target reference | Expected | Result |
|---|---|---|---|
| WAY-11 | WAY-01@60960941 | 60960941 | match |
| WAY-136 | WAY-13@e6c830b7 | e6c830b7 | match |
| WAY-148 | WAY-125@441e3a6a | 441e3a6a | match |
| WAY-148 | WAY-10@db68de1c | db68de1c | match |
| WAY-149 | WAY-10@db68de1c | db68de1c | match |
| WAY-149 | WAY-08@2343e09f | 2343e09f | match |
| WAY-149 | WAY-69@7051f884 | 7051f884 | match |
| WAY-126 | WAY-01@60960941 | 60960941 | match |
| WAY-126 | WAY-11@e882a9df | e882a9df | match |
| WAY-126 | WAY-114@04b4f599 | 04b4f599 | match |
| WAY-126 | WAY-118@5af868b3 | 5af868b3 | match |
| WAY-126 | WAY-106@63eddf70 | 63eddf70 | match |

return-step-record/1 is identical to the base entry except its Derives from fingerprint.
WAY-126/1 was read whole; its projected-entry duty remains valid under WAY-11's new criterion.
No fingerprint-value claim relies on a --merge-onto none guard.
