-- EEZ Analysis Queries
-- Environment: AWS Academy (Athena)
-- Description:
-- Analyzes fishing activity within Exclusive Economic Zones (EEZs)
-- to compare national waters against high seas fishing.

SELECT
    year,
    fishing_entity AS Country,
    SUM(landed_value) AS EEZTotalValue
FROM fishdb.data_source_22601
WHERE area_name IS NOT NULL
GROUP BY year, fishing_entity
ORDER BY year;