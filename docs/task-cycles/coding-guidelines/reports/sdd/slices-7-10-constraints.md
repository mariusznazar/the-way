Global constraints for Slices 7-10:
- Each named entry point equals the output of produce(discover(ROOT)) of agent-instructions/skill_entry_points.py at the slice head, byte for byte; the .claude and .agents copies identical; no other file changed; never hand-written (WAY-127, skill-entry-points/1).
- After the slice the generator prints exactly the would-change lines of the later batches; after Slice 10 it prints `entry points are current` and the gate and agent-instructions suites pass.
- No invariant code covered; no deliberate break.
