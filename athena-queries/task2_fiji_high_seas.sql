-- Task 2: High Seas Catch Analysis for Fiji
-- Environment: AWS Academy (Athena)
-- Description:
-- Calculates total landed value of Fiji's high seas fishing activity
-- after the year 2000 by aggregating landed_value where area_name IS NULL.

SELECT
    year,
    fishing_entity AS Country,
    CAST(CAST(SUM(landed_value) AS DOUBLE) AS DECIMAL(38,2)) AS ValueAllHighSeasCatch
FROM fishdb.data_source_22601
WHERE area_name IS NULL
  AND fishing_entity = 'Fiji'
  AND year > 2000
GROUP BY year, fishing_entity
ORDER BY year;