# A missing element file

- Where the product has no file of the element's entries, ask whether it starts that file here; if
  not, stop
  (`TODO — decision pending: which decision sets that a product starts an element's file only on
  the human's word`). If so, the same change gives the new file to a part of the map through
  `update-part-map` (WAY-44). Where the missing file is the part map itself, the current
  `update-part-map` invocation writes the first map directly, using its "The first map of a
  product" section. Where another element's file is missing and the product has no part map,
  `update-part-map` writes the map first (WAY-28, for a product the process enters;
  `TODO — decision pending: which decision sets that the part map is written before another
  element's first file`).
