# First map

A product with no map gets its parts written one at a time, by the steps of this skill. After the human
accepts the first part, the current invocation writes it in the new map without invoking
`update-part-map` again to create that map. Continue until `elements/common/foundation_check.py`
reports no file git tracks that no part claims and that the map does not leave out on purpose
(WAY-28).
