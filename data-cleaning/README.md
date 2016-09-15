# Data Cleaning

Below are known issues in the data. Please add an 'x' next to the item if you've resolved it in your script. At an upcoming session we can consolidate the data cleaning!

## Prioritization for data cleaning

- We should focus on cleaning up the metrics first and do some feature engineering on these to make sure they are in a state that's valuable to FuF
  - Sidewalk damage: HARDSCAPE
  - Size of trees: DBH
  - Density of trees: Lat/Long - create additional metric
  - Neighborhood: PROPERTY
  - Health of tree: CONDITION - definitely needs cleaning, could simplify categories
  - Types of tree: (Genus and Species): BOTANICAL - may be useful to seperate out genus and species here; Common name: COMMON

## Known issues / areas to work on

- ON_ADR/ONSTREET and PROP_ADR/PROPSTREET are the same except for in some cases, we think it may be because of street corners?
- ON_ADR/ONSTREET and PROP_ADR/PROPSTREET need to be merged to produce addresses
- BOTANICAL needs to be split apart into GENUS and Species
- Many categorical variables, especially the metrics, have redundant/messy categorical values that need to be cleaned up.
- We can create binary indicators from many of these categorical variables and aggregate them to create proportions at the neighborhood level, which would be much easier to visualize on the map, and could also then be exported for decision-making purposes.
