# Planner routing ruling

Root inspected skill_entry_points.py discover/produce and slice_size.py CHANGE_LIMIT=10. Keep every generated path visible in <=10-file slices. Use the existing produce API to write the named batch, then required whole --write at completion; do not change generator or size policy to avoid the limit. This is mechanical generation; no wrapper text is manually authored. Each batch can be compared against produce(discover(ROOT)); interim overall wrapper-suite failures are expected until all batches land and must be explicitly named. Final whole generation must be a no-op or only the final named batch. Record cost: temporary incompleteness and extra sequential reviews, no product interface redesign.

If your plan finds a cleaner solution already permitted by current code and policies, use it and document evidence. This ruling does not request a new design.

## Future-file size accounting

Approved: name future predecessor outputs as explicit prerequisites, with their paths and consuming slices. Do not fabricate stub files or omit them from the execution brief. Initial size report measures currently existing required reads; before each dependent dispatch root adds the produced files to that slice Read and reruns size check. The resulting current size report must fit before dispatch. Document this limitation in plan and report, without claiming initial report measures unknown text. All Change paths remain explicit. Cost: one mechanical plan update/rerun as predecessor files appear; alternative fake files makes the measured input misleading. Actual inventory is 14 existing skills, 28 wrappers, then 15/30, correcting earlier estimate.
