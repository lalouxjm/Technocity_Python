"""
╔══════════════════════════════════════════════════════════════════════════╗
║       SQL EXERCISES — MYTHICAL CREATURE STABLE                           ║
║       Exercise 3 — Subqueries, CTEs & Window Functions                        ║
╚══════════════════════════════════════════════════════════════════════════╝

HOW TO USE THIS FILE
────────────────────
1. Make sure you ran SETUP (Exercise 1) and EXTRA_SETUP (Exercise 2) first.
   Then run the DAY3_SETUP block below ONCE in your DB console — it adds
   the mission_logs table needed for window function exercises.
2. Read each concept definition carefully before writing your query.
3. Write your SQL inside the triple-quoted string for each exercise.
4. Run the tests:  python stable_sql_advanced_exercises.py

CONCEPTS COVERED
────────────────
  SUBQUERIES
    Scalar subquery in SELECT  — returns exactly one value, used as a column
    Subquery in WHERE          — IN (SELECT ...), EXISTS, NOT EXISTS
    Correlated subquery        — references the outer query row by row
    Derived table              — subquery in FROM, must have an alias

  CTEs
    WITH cte AS (...)          — name a subquery for readability and reuse
    Chaining CTEs              — WITH a AS (...), b AS (...) SELECT ...
    Recursive CTE              — WITH RECURSIVE, for hierarchical data
    CTE vs subquery            — when each is the right tool

  WINDOW FUNCTIONS
    OVER ()                    — the window clause, turns aggregate into window fn
    PARTITION BY               — group without collapsing rows
    ORDER BY inside OVER       — defines row ordering within each partition
    ROW_NUMBER()               — unique sequential rank, no ties
    RANK()                     — tied rows share rank, next rank has a gap
    DENSE_RANK()               — tied rows share rank, no gap after
    LAG(col, n)                — value of col n rows before current row
    LEAD(col, n)               — value of col n rows after current row
    SUM() OVER (...)           — running total or partition total
    AVG() OVER (...)           — running/partition average
    FIRST_VALUE() / LAST_VALUE() — first/last value in the window frame

────────────────────────────────────────────────────────────────────────────
FULL SCHEMA REMINDER
────────────────────────────────────────────────────────────────────────────

  species          id, name, danger_level, habitat
  keepers          id, full_name, email, hired_at, supervisor_id → keepers
  creatures        id, name, species_id → species, origin, power_level,
                   in_stable, registered_at
  missions         id, creature_id → creatures, keeper_id → keepers,
                   objective, started_at, ended_at, success
  health_checks    id, creature_id → creatures, keeper_id → keepers,
                   checked_at, notes, power_recorded
  creature_ratings id, creature_id → creatures, keeper_id → keepers,
                   score (1–10), rated_at

NEW TABLE (see DAY3_SETUP)
────────────────────────────────────────────────────────────────────────────
  mission_logs     id, mission_id → missions, event_type, event_at, notes
                   → Tracks each phase of a mission (departure, checkpoint,
                     arrival). Enables time-series window function exercises.
"""

import psycopg
import psycopg.rows

# ─────────────────────────────────────────────────────────────────────────────
# CONNECTION — adjust to your local setup
# ─────────────────────────────────────────────────────────────────────────────
DB_CONFIG = {
    "host":     "localhost",
    "port":     5432,
    "dbname":   "mythical_creature_stable",
    "user":     "postgres",
    "password": "postgrespwd",
}

# ─────────────────────────────────────────────────────────────────────────────
# SETUP Database
# ─────────────────────────────────────────────────────────────────────────────
SETUP_SQL = """
-- It creates the schema and inserts seed data so the exercises work.

DROP TABLE IF EXISTS health_checks, creature_missions, missions, creatures, keepers, species CASCADE;

CREATE TABLE species (
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(100) NOT NULL UNIQUE,
    danger_level INTEGER NOT NULL CHECK (danger_level BETWEEN 1 AND 10),
    habitat      VARCHAR(100)
);

CREATE TABLE keepers (
    id        SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL,
    email     VARCHAR(255) NOT NULL UNIQUE,
    hired_at  TIMESTAMP DEFAULT NOW()
);

CREATE TABLE creatures (
    id            SERIAL PRIMARY KEY,
    name          TEXT NOT NULL,
    species_id    INTEGER NOT NULL REFERENCES species(id) ON DELETE RESTRICT,
    origin        TEXT NOT NULL,
    power_level   NUMERIC(5,2) NOT NULL CHECK (power_level BETWEEN 0 AND 100),
    in_stable     BOOLEAN NOT NULL DEFAULT TRUE,
    registered_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE missions (
    id          SERIAL PRIMARY KEY,
    creature_id INTEGER NOT NULL REFERENCES creatures(id) ON DELETE RESTRICT,
    keeper_id   INTEGER NOT NULL REFERENCES keepers(id),
    objective   TEXT NOT NULL,
    started_at  TIMESTAMP NOT NULL DEFAULT NOW(),
    ended_at    TIMESTAMP,
    success     BOOLEAN
);

CREATE TABLE health_checks (
    id             SERIAL PRIMARY KEY,
    creature_id    INTEGER NOT NULL REFERENCES creatures(id) ON DELETE CASCADE,
    keeper_id      INTEGER NOT NULL REFERENCES keepers(id),
    checked_at     TIMESTAMP NOT NULL DEFAULT NOW(),
    notes          TEXT,
    power_recorded NUMERIC(5,2)
);

-- Species
INSERT INTO species (name, danger_level, habitat) VALUES
    ('Dragon',     9,  'Volcanic Mountains'),
    ('Ice Dragon', 8,  'Arctic Tundra'),
    ('Phoenix',    6,  'Solar Peaks'),
    ('Griffin',    7,  'Highland Cliffs'),
    ('Unicorn',    3,  'Enchanted Forest'),
    ('Basilisk',   10, 'Dark Caverns');

-- Keepers
INSERT INTO keepers (full_name, email, hired_at) VALUES
    ('Morgane Le Fay',   'morgane@stable.com',  NOW() - INTERVAL '3 years'),
    ('Aldric Stonehoof', 'aldric@stable.com',   NOW() - INTERVAL '1 year'),
    ('Seraphina Voss',   'seraphina@stable.com', NOW() - INTERVAL '6 months');

-- Creatures
INSERT INTO creatures (name, species_id, origin, power_level, in_stable, registered_at) VALUES
    ('Frostbite',   2, 'Nordic Realms',       95,   TRUE,  NOW() - INTERVAL '2 years'),
    ('Emberclaw',   1, 'Volcanic Peaks',       88,   FALSE, NOW() - INTERVAL '18 months'),
    ('Solaris',     3, 'Solar Peaks',          76,   TRUE,  NOW() - INTERVAL '1 year'),
    ('Stonewing',   4, 'Highland Cliffs',      65,   TRUE,  NOW() - INTERVAL '8 months'),
    ('Pearlhoof',   5, 'Enchanted Forest',     45,   TRUE,  NOW() - INTERVAL '5 months'),
    ('Shadowcoil',  6, 'Dark Caverns',         99,   FALSE, NOW() - INTERVAL '3 months'),
    ('Blazethorn',  1, 'Volcanic Peaks',       55,   TRUE,  NOW() - INTERVAL '40 days'),
    ('Glacierfang', 1, 'Nordic Realms',        81,   TRUE,  NOW() - INTERVAL '15 days'),
    ('Dawnfeather', 3, 'Solar Peaks',          60,   TRUE,  NOW() - INTERVAL '7 days'),
    ('Nightscale',  1, 'Shadow Mountains',     33,   TRUE,  NOW() - INTERVAL '2 days');

-- Missions
INSERT INTO missions (creature_id, keeper_id, objective, started_at, ended_at, success) VALUES
    (2, 1, 'Escort the fire convoy through the Ashlands',
        NOW() - INTERVAL '10 days', NOW() - INTERVAL '3 days', TRUE),
    (6, 2, 'Patrol the northern border of the Dark Caverns',
        NOW() - INTERVAL '5 days', NULL, NULL),
    (1, 1, 'Scout frozen passage for the winter expedition',
        NOW() - INTERVAL '60 days', NOW() - INTERVAL '55 days', TRUE),
    (4, 3, 'Guard the royal messenger through Highland Pass',
        NOW() - INTERVAL '20 days', NOW() - INTERVAL '18 days', FALSE);

-- Health checks
INSERT INTO health_checks (creature_id, keeper_id, checked_at, notes, power_recorded) VALUES
    (1, 1, NOW() - INTERVAL '30 days', 'Excellent condition, scales bright', 94),
    (1, 2, NOW() - INTERVAL '5 days',  'Minor cold after scouting mission',  88),
    (3, 1, NOW() - INTERVAL '10 days', 'Feathers regenerating well',         70),
    (5, 3, NOW() - INTERVAL '2 days',  NULL,                                 45),
    (7, 2, NOW() - INTERVAL '1 day',   'New arrival checkup',                55);

-- Exercise 2 Setup
-- Add supervisor_id to keepers for the self-join exercise
ALTER TABLE keepers ADD COLUMN IF NOT EXISTS supervisor_id INTEGER REFERENCES keepers(id);

-- Morgane supervises Aldric and Seraphina
UPDATE keepers SET supervisor_id = 1 WHERE full_name = 'Aldric Stonehoof';
UPDATE keepers SET supervisor_id = 1 WHERE full_name = 'Seraphina Voss';
-- Morgane has no supervisor (she is the head keeper)

-- New table: creature_ratings (some creatures intentionally have no rating)
DROP TABLE IF EXISTS creature_ratings CASCADE;

CREATE TABLE creature_ratings (
    id          SERIAL PRIMARY KEY,
    creature_id INTEGER NOT NULL REFERENCES creatures(id) ON DELETE CASCADE,
    keeper_id   INTEGER NOT NULL REFERENCES keepers(id),
    score       INTEGER NOT NULL CHECK (score BETWEEN 1 AND 10),
    rated_at    TIMESTAMP NOT NULL DEFAULT NOW()
);

INSERT INTO creature_ratings (creature_id, keeper_id, score, rated_at) VALUES
    (1, 1, 9,  NOW() - INTERVAL '25 days'),   -- Frostbite     rated by Morgane
    (1, 2, 8,  NOW() - INTERVAL '4 days'),    -- Frostbite     rated by Aldric
    (2, 1, 7,  NOW() - INTERVAL '12 days'),   -- Emberclaw     rated by Morgane
    (3, 1, 6,  NOW() - INTERVAL '9 days'),    -- Solaris       rated by Morgane
    (4, 3, 5,  NOW() - INTERVAL '19 days'),   -- Stonewing     rated by Seraphina
    (7, 2, 8,  NOW() - INTERVAL '1 day');     -- Blazethorn    rated by Aldric
-- Pearlhoof (5), Shadowcoil (6), Glacierfang (8),
-- Dawnfeather (9), Nightscale (10) → no rating yet

-- Exercise 3 Setup
-- mission_logs: sequential events on each mission (for window function exercises)
DROP TABLE IF EXISTS mission_logs CASCADE;

CREATE TABLE mission_logs (
    id          SERIAL PRIMARY KEY,
    mission_id  INTEGER NOT NULL REFERENCES missions(id) ON DELETE CASCADE,
    event_type  VARCHAR(50) NOT NULL
                CHECK (event_type IN ('departure','checkpoint','arrival','abort')),
    event_at    TIMESTAMP NOT NULL,
    notes       TEXT
);

-- Mission 1  (creature_id=2, Emberclaw — completed, success)
INSERT INTO mission_logs (mission_id, event_type, event_at, notes) VALUES
    (1, 'departure',   NOW() - INTERVAL '10 days',             'Left at dawn'),
    (1, 'checkpoint',  NOW() - INTERVAL '8 days',              'Reached mid-point'),
    (1, 'checkpoint',  NOW() - INTERVAL '5 days 12 hours',     'Escort secured'),
    (1, 'arrival',     NOW() - INTERVAL '3 days',              'Mission complete');

-- Mission 2  (creature_id=6, Shadowcoil — ongoing, no end)
INSERT INTO mission_logs (mission_id, event_type, event_at, notes) VALUES
    (2, 'departure',   NOW() - INTERVAL '5 days',              'Night departure'),
    (2, 'checkpoint',  NOW() - INTERVAL '3 days',              'Border reached');

-- Mission 3  (creature_id=1, Frostbite — completed, success)
INSERT INTO mission_logs (mission_id, event_type, event_at, notes) VALUES
    (3, 'departure',   NOW() - INTERVAL '60 days',             'Scouting team assembled'),
    (3, 'checkpoint',  NOW() - INTERVAL '58 days',             'Ice passage located'),
    (3, 'arrival',     NOW() - INTERVAL '55 days',             'Route confirmed');

-- Mission 4  (creature_id=4, Stonewing — completed, failure)
INSERT INTO mission_logs (mission_id, event_type, event_at, notes) VALUES
    (4, 'departure',   NOW() - INTERVAL '20 days',             'Highland patrol start'),
    (4, 'checkpoint',  NOW() - INTERVAL '19 days 12 hours',    'Ambush encountered'),
    (4, 'abort',       NOW() - INTERVAL '19 days',             'Messenger lost — aborted'),
    (4, 'arrival',     NOW() - INTERVAL '18 days',             'Returned to stable');
"""


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS — do not modify
# ─────────────────────────────────────────────────────────────────────────────
def get_conn():
    return psycopg.connect(**DB_CONFIG)

def setup_database(conn):
    with conn.cursor() as cur:
        cur.execute(SETUP_SQL)
    conn.commit()
    print("Database setup complete.")

def run_query(sql: str) -> list[dict]:
    with get_conn() as conn:
        with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
            cur.execute(sql)
            return cur.fetchall()

def check(label: str, result, assertion_fn, hint: str = ""):
    try:
        ok = assertion_fn(result)
    except Exception as e:
        ok = False
        hint = f"{hint} | assertion raised: {e}"
    status = "✅ PASS" if ok else "❌ FAIL"
    print(f"{status}  —  {label}")
    if not ok:
        print(f"         Result  : {result}")
        if hint:
            print(f"         Hint    : {hint}")


# ═════════════════════════════════════════════════════════════════════════════
#
#  ██████╗  █████╗ ██████╗ ████████╗      ██╗
#  ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝     ██╔╝
#  ██████╔╝███████║██████╔╝   ██║       ██╔╝
#  ██╔═══╝ ██╔══██║██╔══██╗   ██║      ██╔╝
#  ██║     ██║  ██║██║  ██║   ██║     ██╔╝
#  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═╝
#       SUBQUERIES
#
# ─────────────────────────────────────────────────────────────────────────────
# CONCEPT: SCALAR SUBQUERY IN SELECT
# ─────────────────────────────────────────────────────────────────────────────
# A subquery that returns exactly ONE row and ONE column.
# It is used as a regular column expression in SELECT.
# If it returns more than one row → runtime error.
# If it returns no rows → NULL.
#
# Use it when you want to show a computed reference value alongside each row
# without collapsing the result with GROUP BY.
#
# Example:
#   SELECT name,
#          power_level,
#          (SELECT AVG(power_level) FROM creatures) AS avg_power
#   FROM creatures;
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 1 — Scalar subquery: power vs stable average
#
# For each creature currently in the stable, show:
#   - name
#   - power_level
#   - the average power_level of ALL creatures in the stable (aliased as avg_stable_power,
#     rounded to 2 decimals) — compute this with a scalar subquery, not a JOIN
#   - the difference between the creature's power and that average
#     (aliased as diff, rounded to 2 decimals)
#
# Condition: in_stable = TRUE
# Order by: diff DESC
# ─────────────────────────────────────────────────────────────────────────────
Q1 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 2 — Scalar subquery: most recent health check date
#
# For each creature, show its name and the date of its most recent health check.
# Use a correlated scalar subquery in SELECT (not a JOIN).
# Creatures with no health check should show NULL.
#
# Return: name, last_check (the MAX checked_at for that creature, or NULL)
# Order by: last_check DESC NULLS LAST
# ─────────────────────────────────────────────────────────────────────────────
Q2 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# CONCEPT: SUBQUERY IN WHERE — IN / EXISTS / NOT EXISTS
# ─────────────────────────────────────────────────────────────────────────────
# IN (SELECT ...)   — row matches if its value is in the subquery result set.
#                     The subquery is run ONCE and its result is materialized.
#                     Fragile if the subquery can return NULLs (see Day 2).
#
# EXISTS (SELECT 1 FROM ... WHERE correlated_condition)
#                   — returns TRUE if the subquery returns at least one row.
#                     Does not care about the value — convention is SELECT 1.
#                     Short-circuits on first match → can be faster than IN
#                     on large datasets.
#
# NOT EXISTS        — returns TRUE if the subquery returns ZERO rows.
#                     Safe with NULLs. Preferred over NOT IN.
#
# EXISTS vs IN:
#   Semantically identical for simple cases.
#   EXISTS is better when: the subquery is large, NULLs are possible,
#   or you only care about existence (not the value).
#   IN is cleaner for small static lists or simple lookups.
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 3 — IN (subquery): species that have a dangerous creature in-stable
#
# Find all species where at least one creature with power_level > 80
# is currently in the stable.
# Use IN (SELECT ...) — do not use a JOIN.
#
# Return: species name, danger_level
# Order by: danger_level DESC
# ─────────────────────────────────────────────────────────────────────────────
Q3 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 4 — EXISTS: keepers who have performed at least one health check
#
# List all keepers who have performed at least one health check.
# Use EXISTS — do not use a JOIN or COUNT.
#
# Return: full_name, email
# Order by: full_name ASC
# ─────────────────────────────────────────────────────────────────────────────
Q4 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 5 — NOT EXISTS: creatures that have never had a health check
#
# Find all creatures that have never had a health check recorded.
# Use NOT EXISTS — do not use LEFT JOIN or NOT IN.
#
# Return: name, species_id, power_level
# Order by: power_level DESC
# ─────────────────────────────────────────────────────────────────────────────
Q5 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# CONCEPT: CORRELATED SUBQUERY
# ─────────────────────────────────────────────────────────────────────────────
# A subquery that references a column from the OUTER query.
# It is re-executed once for every row of the outer query.
# This makes it powerful but potentially slow on large tables.
#
# Use it when the condition depends on the current outer row.
#
# Example: find creatures whose power is above their own species average:
#   SELECT c.name, c.power_level
#   FROM creatures c
#   WHERE c.power_level > (
#       SELECT AVG(c2.power_level)
#       FROM creatures c2
#       WHERE c2.species_id = c.species_id   -- ← references outer row
#   );
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 6 — Correlated subquery: above-species-average power
#
# Find all creatures whose power_level is strictly above the average
# power_level of their own species.
# Use a correlated subquery in WHERE — not a CTE or JOIN.
#
# Return: name, species_id, power_level
# Order by: power_level DESC
# ─────────────────────────────────────────────────────────────────────────────
Q6 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 7 — Correlated subquery: keeper's most recent mission
#
# For each keeper, return their name and the objective of their most recent
# mission (by started_at). Keepers with no missions show NULL.
# Use a correlated scalar subquery in SELECT.
#
# Return: full_name, latest_mission_objective
# Order by: full_name ASC
# ─────────────────────────────────────────────────────────────────────────────
Q7 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# CONCEPT: DERIVED TABLE (subquery in FROM)
# ─────────────────────────────────────────────────────────────────────────────
# A subquery placed in the FROM clause and given an alias.
# The outer query treats it exactly like a regular table.
# Must always have an alias.
#
# Use it to pre-aggregate or pre-filter data before joining or filtering again.
# CTEs (see below) are the modern, more readable alternative.
#
# Example:
#   SELECT species_id, avg_power
#   FROM (
#       SELECT species_id, AVG(power_level) AS avg_power
#       FROM creatures
#       GROUP BY species_id
#   ) AS species_stats
#   WHERE avg_power > 60;
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 8 — Derived table: species with average power above threshold
#
# Using a derived table (subquery in FROM), find all species whose
# average creature power_level is above 60.
# Join the derived result back to the species table to get the species name.
#
# Return: species name, avg_power (rounded to 2 decimals)
# Order by: avg_power DESC
# ─────────────────────────────────────────────────────────────────────────────
Q8 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 9 — Derived table: creatures above their species average
#
# Using a derived table that computes avg power per species,
# join it back to creatures to find every creature whose power_level
# exceeds their species average.
#
# Return: creature name, species_id, power_level, species_avg (rounded to 2)
# Order by: power_level DESC
# ─────────────────────────────────────────────────────────────────────────────
Q9 = """
SELECT 0


"""


# ═════════════════════════════════════════════════════════════════════════════
#
#   ██████╗████████╗███████╗███████╗
#  ██╔════╝╚══██╔══╝██╔════╝██╔════╝
#  ██║        ██║   █████╗  ███████╗
#  ██║        ██║   ██╔══╝  ╚════██║
#  ╚██████╗   ██║   ███████╗███████║
#   ╚═════╝   ╚═╝   ╚══════╝╚══════╝
#
# ─────────────────────────────────────────────────────────────────────────────
# CONCEPT: CTE — Common Table Expression
# ─────────────────────────────────────────────────────────────────────────────
# WITH cte_name AS (
#     SELECT ...
# )
# SELECT ... FROM cte_name;
#
# A CTE is a named, temporary result set defined at the top of the query.
# It can be referenced multiple times in the main query.
# It does NOT persist after the query finishes.
#
# CTE vs subquery — when to prefer which:
#   → CTE  : the logic is complex, referenced more than once, or you need
#             to debug a step in isolation. Readability is the main gain.
#   → Subquery: simple one-off computation, inline is clear enough,
#               or you need a correlated reference (CTEs can't be correlated).
#
# Chaining CTEs:
#   WITH a AS (...),
#        b AS (... reference a ...)
#   SELECT ... FROM b;
#   Each CTE can reference any earlier CTE in the chain.
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 10 — Single CTE: creatures above overall average power
#
# Rewrite Exercise 6's logic using a CTE instead of a correlated subquery.
# The CTE computes the average power_level per species.
# The main query joins creatures to the CTE and filters those above average.
#
# Return: creature name, species_id, power_level, species_avg (rounded to 2)
# Order by: power_level DESC
# ─────────────────────────────────────────────────────────────────────────────
Q10 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 11 — Chained CTEs: mission stats + top performers
#
# Using two chained CTEs:
#   CTE 1 (keeper_stats): for each keeper, compute total_missions and
#          successful_missions (success = TRUE).
#   CTE 2 (top_keepers): filter keeper_stats to keepers with at least
#          2 total missions.
# Main query: join top_keepers to keepers to get the full_name,
#             and compute success_rate as a percentage (rounded to 1 decimal).
#
# Return: full_name, total_missions, successful_missions, success_rate
# Order by: success_rate DESC
# ─────────────────────────────────────────────────────────────────────────────
Q11 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 12 — CTE + Window preview: best creature per species
#
# Using a CTE, compute total health checks per creature.
# Then, in the main query, rank creatures within each species by check count
# (highest first) and return only the top-ranked creature per species.
#
# Return: species name, creature name, check_count
# Order by: species name ASC
#
# 💡 You will need RANK() OVER (PARTITION BY ... ORDER BY ...) inside
#    the CTE or a second CTE. The outer query then filters WHERE rank = 1.
# ─────────────────────────────────────────────────────────────────────────────
Q12 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# CONCEPT: RECURSIVE CTE
# ─────────────────────────────────────────────────────────────────────────────
# WITH RECURSIVE cte AS (
#     -- Base case: starting rows
#     SELECT ...
#     UNION ALL
#     -- Recursive case: joins cte to itself to go one level deeper
#     SELECT ... FROM source JOIN cte ON cte.id = source.parent_id
# )
# SELECT * FROM cte;
#
# Used for hierarchical or graph data:
#   - org charts (employees → managers → managers)
#   - category trees
#   - any self-referential table
#
# ALWAYS include a depth counter or a cycle guard in production —
# an infinite loop will crash the query.
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 13 — Recursive CTE: keeper hierarchy
#
# Using a recursive CTE, traverse the keeper supervisor hierarchy.
# Start from the head keeper (supervisor_id IS NULL) and walk down.
#
# Return for each keeper:
#   full_name, supervisor_name (NULL for the head), depth
#   (0 = head, 1 = direct report, 2 = report of report, etc.)
#
# Order by: depth ASC, full_name ASC
#
# 💡 The base case selects the head keeper.
#    The recursive case joins keepers to the CTE on supervisor_id = cte.id.
# ─────────────────────────────────────────────────────────────────────────────
Q13 = """
SELECT 0


"""


# ═════════════════════════════════════════════════════════════════════════════
#
#  ██╗    ██╗██╗███╗   ██╗██████╗  ██████╗ ██╗    ██╗
#  ██║    ██║██║████╗  ██║██╔══██╗██╔═══██╗██║    ██║
#  ██║ █╗ ██║██║██╔██╗ ██║██║  ██║██║   ██║██║ █╗ ██║
#  ██║███╗██║██║██║╚██╗██║██║  ██║██║   ██║██║███╗██║
#  ╚███╔███╔╝██║██║ ╚████║██████╔╝╚██████╔╝╚███╔███╔╝
#   ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝  ╚══╝╚══╝
#       WINDOW FUNCTIONS
#
# ─────────────────────────────────────────────────────────────────────────────
# CONCEPT: WINDOW FUNCTIONS — the key idea
# ─────────────────────────────────────────────────────────────────────────────
# A window function computes a value across a set of rows (the "window")
# WITHOUT collapsing them into a single row the way GROUP BY does.
# Each row keeps its own identity AND gets a computed column from the window.
#
# Syntax:
#   function() OVER (
#       PARTITION BY col   -- divide rows into groups (like GROUP BY, but no collapse)
#       ORDER BY col       -- define row order within each partition
#       ROWS BETWEEN ...   -- optional frame clause
#   )
#
# ROW_NUMBER()     unique sequential integer, no ties, restarts per partition
# RANK()           same rank for ties → gap after (1,1,3,4)
# DENSE_RANK()     same rank for ties → no gap   (1,1,2,3)
# LAG(col, n)      value of col from n rows BEFORE current row in the window
# LEAD(col, n)     value of col from n rows AFTER current row in the window
# SUM() OVER (…)   running total or partition subtotal
# AVG() OVER (…)   running or partition average
# FIRST_VALUE(col) first value of col in the window frame
# LAST_VALUE(col)  last value of col in the window frame
#                  ⚠ LAST_VALUE needs ROWS BETWEEN UNBOUNDED PRECEDING
#                    AND UNBOUNDED FOLLOWING to see the true last row
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 14 — ROW_NUMBER: rank creatures by power within each species
#
# Assign a ROW_NUMBER to each creature, ordered by power_level DESC,
# partitioned by species_id.
#
# Return: species name, creature name, power_level, power_rank
# Order by: species name ASC, power_rank ASC
# ─────────────────────────────────────────────────────────────────────────────
Q14 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 15 — RANK vs DENSE_RANK: show the difference
#
# Using a CTE or subquery, compute both RANK() and DENSE_RANK() for all
# creatures ordered by power_level DESC (no partition — global ranking).
#
# Return: name, power_level, rnk (RANK), dense_rnk (DENSE_RANK)
# Order by: power_level DESC
#
# 💡 If multiple creatures share the same power_level you will see RANK and
#    DENSE_RANK diverge. Check the seed data — are there any ties?
# ─────────────────────────────────────────────────────────────────────────────
Q15 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 16 — Top creature per species (filter on window rank)
#
# Find the single most powerful creature in each species.
# Use ROW_NUMBER() OVER (PARTITION BY species_id ORDER BY power_level DESC).
# Wrap it in a CTE or derived table, then filter WHERE rn = 1.
#
# Return: species name, creature name, power_level
# Order by: power_level DESC
#
# 💡 This is the canonical interview pattern for "top N per group".
# ─────────────────────────────────────────────────────────────────────────────
Q16 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 17 — SUM() OVER: running total of creatures registered over time
#
# For each creature, show the cumulative count of creatures registered
# up to and including that creature's registered_at date.
# (i.e., a running COUNT ordered by registered_at)
#
# Return: name, registered_at, cumulative_count
# Order by: registered_at ASC
#
# 💡 Use COUNT(*) OVER (ORDER BY registered_at
#         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
# ─────────────────────────────────────────────────────────────────────────────
Q17 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 18 — LAG: power change between consecutive health checks
#
# For each creature that has more than one health check, show each check
# with the power_recorded, the previous check's power (aliased as prev_power,
# NULL for the first check), and the difference (power_recorded - prev_power,
# aliased as power_change, NULL for the first check).
#
# Use LAG(power_recorded, 1) OVER (PARTITION BY creature_id ORDER BY checked_at).
#
# Return: creature name, checked_at, power_recorded, prev_power, power_change
# Filter: only creatures that have at least 2 health checks
# Order by: creature name ASC, checked_at ASC
# ─────────────────────────────────────────────────────────────────────────────
Q18 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 19 — AVG() OVER + PARTITION BY: power vs species running average
#
# For each creature, show:
#   - name
#   - species name
#   - power_level
#   - the average power_level of its species (aliased as species_avg,
#     rounded to 2 decimals) — use AVG() OVER (PARTITION BY species_id)
#   - the difference between the creature's power and the species average
#     (aliased as diff, rounded to 2 decimals)
#
# Order by: species name ASC, diff DESC
#
# 💡 This is the window-function version of Exercise 6.
#    No GROUP BY, no subquery — each row keeps its identity.
# ─────────────────────────────────────────────────────────────────────────────
Q19 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 20 — LEAD: time between consecutive mission log events
#
# For each mission, show each log event with:
#   - mission_id
#   - event_type
#   - event_at
#   - next_event_type (the following event_type in that mission, or NULL)
#   - minutes_to_next (minutes between event_at and the next event, or NULL)
#     round to 0 decimal places
#
# Use LEAD() OVER (PARTITION BY mission_id ORDER BY event_at).
#
# Return all columns listed above.
# Order by: mission_id ASC, event_at ASC
# ─────────────────────────────────────────────────────────────────────────────
Q20 = """
SELECT 0


"""


# ═════════════════════════════════════════════════════════════════════════════
#
#  ██╗███╗   ██╗████████╗███████╗██████╗ ██╗   ██╗██╗███████╗██╗    ██╗
#  ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██║   ██║██║██╔════╝██║    ██║
#  ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝██║   ██║██║█████╗  ██║ █╗ ██║
#  ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗╚██╗ ██╔╝██║██╔══╝  ██║███╗██║
#  ██║██║ ╚████║   ██║   ███████╗██║  ██║ ╚████╔╝ ██║███████╗╚███╔███╔╝
#  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝
#       INTERVIEW-LEVEL QUERIES
#
# These are the classic questions that come up in SQL interviews at
# mid/senior level. Each one tests composition of multiple concepts.
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 21 — "Second highest power" (classic interview question)
#
# Find the creature(s) with the SECOND highest power_level.
# If there are ties for second place, return all of them.
# Do NOT use OFFSET. Use DENSE_RANK().
#
# Return: name, power_level
# Order by: name ASC
# ─────────────────────────────────────────────────────────────────────────────
Q21 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 22 — "Creatures with above-average power in every species"
#
# Using a CTE for the per-species average, find creatures whose power_level
# is above BOTH:
#   a) their own species average
#   b) the overall stable average
# Use two CTEs — one for species averages, one for the overall average.
#
# Return: creature name, species name, power_level,
#         species_avg (rounded 2), overall_avg (rounded 2)
# Order by: power_level DESC
# ─────────────────────────────────────────────────────────────────────────────
Q22 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 23 — "EXISTS vs IN": rewrite and compare
#
# Part a) Write a query using IN (subquery) to find all creatures
#         that belong to a species with danger_level >= 8.
#
# Part b) Rewrite the SAME query using EXISTS.
#
# Both queries must return identical results.
# Return: creature name, species_id, power_level
# Order by: power_level DESC
#
# Then add a comment explaining:
#   - In what situation would EXISTS be faster than IN?
#   - When are they equivalent?
# ─────────────────────────────────────────────────────────────────────────────
Q23a = """
SELECT 0


"""

Q23b = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 24 — Full pipeline: CTE + JOIN + Window + Filter
#
# The stable master wants a "danger report": for each species, show:
#   - species name
#   - danger_level
#   - number of creatures currently in the stable (in_stable = TRUE)
#   - the most powerful creature's name (use FIRST_VALUE or a ranked subquery)
#   - the species' rank by danger_level (RANK() — highest danger = rank 1)
#
# Use at least one CTE.
# Return all 5 columns above.
# Order by: danger_rank ASC
# ─────────────────────────────────────────────────────────────────────────────
Q24 = """
SELECT 0


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 25 — "Running total" (classic interview question)
#
# The stable master wants to see creature registrations over time as a
# running total — showing how the stable grew day by day.
#
# For each registration date (DATE, not TIMESTAMP), show:
#   - registration_date
#   - new_registrations  (creatures registered on that date)
#   - total_registered   (cumulative total up to and including that date)
#
# Use a CTE to aggregate by date, then a window function for the running total.
# Order by: registration_date ASC
# ─────────────────────────────────────────────────────────────────────────────
Q25 = """
SELECT 0


"""


# ═════════════════════════════════════════════════════════════════════════════
#  TEST RUNNER — do not modify below this line
# ═════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n" + "═" * 64)
    print("  STABLE SQL — Day 3: Subqueries, CTEs & Window Functions")
    print("═" * 64 + "\n")

    setup_database(get_conn())

    # ── SCALAR SUBQUERIES ────────────────────────────────────────────────
    print("── SCALAR SUBQUERIES ───────────────────────────────────────────")

    r1 = run_query(Q1)
    check(
        "Q1 — power vs stable average (scalar subquery in SELECT)",
        r1,
        lambda r: (
            len(r) == 8
            and "avg_stable_power" in r[0]
            and "diff" in r[0]
            and all(r[i]["diff"] >= r[i+1]["diff"] for i in range(len(r)-1))
            and len({row["avg_stable_power"] for row in r}) == 1
        ),
        "Expected 8 in-stable creatures, one shared avg_stable_power, ordered by diff DESC"
    )

    r2 = run_query(Q2)
    check(
        "Q2 — most recent health check per creature (correlated scalar subquery)",
        r2,
        lambda r: (
            len(r) == 10
            and "last_check" in r[0]
            and any(row["last_check"] is None for row in r)
        ),
        "Expected 10 rows (all creatures), NULL for creatures with no health check"
    )

    # ── WHERE SUBQUERIES ─────────────────────────────────────────────────
    print("\n── WHERE SUBQUERIES (IN / EXISTS / NOT EXISTS) ─────────────────")

    r3 = run_query(Q3)
    check(
        "Q3 — species with a high-power in-stable creature (IN subquery)",
        r3,
        lambda r: (
            len(r) == 2
            and "danger_level" in r[0]
            and list(r) == sorted(r, key=lambda x: -x["danger_level"])
        ),
        "Expected 2 species. Ordered by danger_level DESC"
    )

    r4 = run_query(Q4)
    check(
        "Q4 — keepers who performed at least one health check (EXISTS)",
        r4,
        lambda r: (
            len(r) == 3
            and "full_name" in r[0]
            and "email" in r[0]
            and list(r) == sorted(r, key=lambda x: x["full_name"])
        ),
        "Expected 3 keepers. Ordered by full_name ASC"
    )

    r5 = run_query(Q5)
    check(
        "Q5 — creatures with no health check (NOT EXISTS)",
        r5,
        lambda r: (
            len(r) == 6
            and "power_level" in r[0]
            and list(r) == sorted(r, key=lambda x: -float(x["power_level"]))
        ),
        "Expected 6 creatures with no health_checks row. Ordered by power_level DESC"
    )

    # ── CORRELATED SUBQUERIES ────────────────────────────────────────────
    print("\n── CORRELATED SUBQUERIES ───────────────────────────────────────")

    r6 = run_query(Q6)
    check(
        "Q6 — creatures above their species average power (correlated subquery)",
        r6,
        lambda r: (
            len(r) >= 3
            and "power_level" in r[0]
            and list(r) == sorted(r, key=lambda x: -float(x["power_level"]))
        ),
        "Expected at least 3 creatures above their species avg. Ordered by power_level DESC"
    )

    r7 = run_query(Q7)
    check(
        "Q7 — keeper's most recent mission objective (correlated scalar subquery)",
        r7,
        lambda r: (
            len(r) >= 3
            and "full_name" in r[0]
            and "latest_mission_objective" in r[0]
            and list(r) == sorted(r, key=lambda x: x["full_name"])
        ),
        "Expected all 3 keepers with their latest mission objective. "
        "Ordered by full_name ASC"
    )

    # ── DERIVED TABLES ───────────────────────────────────────────────────
    print("\n── DERIVED TABLES ──────────────────────────────────────────────")

    r8 = run_query(Q8)
    check(
        "Q8 — species avg power > 60 (derived table)",
        r8,
        lambda r: (
            len(r) == 5
            and "avg_power" in r[0]
            and all(float(row["avg_power"]) > 60 for row in r)
            and list(r) == sorted(r, key=lambda x: -float(x["avg_power"]))
        ),
        "Expected 5 species with avg_power > 60. Ordered by avg_power DESC"
    )

    r9 = run_query(Q9)
    check(
        "Q9 — creatures above species avg (derived table join)",
        r9,
        lambda r: (
            len(r) >= 3
            and "species_avg" in r[0]
            and "power_level" in r[0]
            and all(float(row["power_level"]) > float(row["species_avg"]) for row in r)
            and list(r) == sorted(r, key=lambda x: -float(x["power_level"]))
        ),
        "Expected creatures whose power > their species_avg. Ordered by power_level DESC"
    )

    # ── CTEs ─────────────────────────────────────────────────────────────
    print("\n── CTEs ────────────────────────────────────────────────────────")

    r10 = run_query(Q10)
    check(
        "Q10 — above species avg using CTE (equivalent to Q6/Q9)",
        r10,
        lambda r: (
            len(r) >= 3
            and "species_avg" in r[0]
            and "power_level" in r[0]
            and all(float(row["power_level"]) > float(row["species_avg"]) for row in r)
            and list(r) == sorted(r, key=lambda x: -float(x["power_level"]))
        ),
        "Same expected result as Q9 but written with a CTE. Ordered by power_level DESC"
    )

    r11 = run_query(Q11)
    check(
        "Q11 — keeper success rate (chained CTEs)",
        r11,
        lambda r: (
            len(r) == 1
            and "success_rate" in r[0]
            and "total_missions" in r[0]
            and all(row["total_missions"] >= 2 for row in r)
            and all(0 <= float(row["success_rate"]) <= 100 for row in r)
            and list(r) == sorted(r, key=lambda x: -float(x["success_rate"]))
        ),
        "Expected 1 keepers with >= 2 missions. success_rate 0–100. Ordered by success_rate DESC"
    )

    r12 = run_query(Q12)
    check(
        "Q12 — most health-checked creature per species (CTE + window rank)",
        r12,
        lambda r: (
            len(r) >= 1
            and "check_count" in r[0]
        ),
        "Expected one row per species that has health checks. "
        "Columns: species name, creature name, check_count"
    )

    r13 = run_query(Q13)
    check(
        "Q13 — keeper hierarchy (recursive CTE)",
        r13,
        lambda r: (
            len(r) == 3
            and "depth" in r[0]
            and any(row["depth"] == 0 for row in r)
            and any(row["depth"] == 1 for row in r)
            and list(r) == sorted(r, key=lambda x: (x["depth"], x["full_name"]))
        ),
        "Expected 3 keepers with depth 0 (head) and 1 (direct reports). "
        "Ordered by depth ASC, full_name ASC"
    )

    # ── WINDOW FUNCTIONS ─────────────────────────────────────────────────
    print("\n── WINDOW FUNCTIONS ────────────────────────────────────────────")

    r14 = run_query(Q14)
    check(
        "Q14 — ROW_NUMBER per species by power_level",
        r14,
        lambda r: (
            len(r) == 10
            and "power_rank" in r[0]
            and all(row["power_rank"] >= 1 for row in r)
        ),
        "Expected 10 rows, all creatures ranked within their species by power_level DESC"
    )

    r15 = run_query(Q15)
    check(
        "Q15 — RANK vs DENSE_RANK globally",
        r15,
        lambda r: (
            len(r) == 10
            and "rnk" in r[0]
            and "dense_rnk" in r[0]
            and list(r) == sorted(r, key=lambda x: -float(x["power_level"]))
        ),
        "Expected 10 rows with rnk and dense_rnk columns. Ordered by power_level DESC"
    )

    r16 = run_query(Q16)
    check(
        "Q16 — top creature per species (ROW_NUMBER filter = 1)",
        r16,
        lambda r: (
            len(r) == 6
            and "power_level" in r[0]
            and list(r) == sorted(r, key=lambda x: -float(x["power_level"]))
        ),
        "Expected 6 rows - one per species (6 species have creatures). "
        "Ordered by power_level DESC"
    )

    r17 = run_query(Q17)
    check(
        "Q17 — running count of creature registrations",
        r17,
        lambda r: (
            len(r) == 10
            and "cumulative_count" in r[0]
            and r[-1]["cumulative_count"] == 10
            and r[0]["cumulative_count"] >= 1
            and list(r) == sorted(r, key=lambda x: x["registered_at"])
        ),
        "Expected 10 rows ordered by registered_at ASC, "
        "last cumulative_count must be 10"
    )

    r18 = run_query(Q18)
    check(
        "Q18 — LAG: power change between health checks",
        r18,
        lambda r: (
            len(r) >= 2
            and "prev_power" in r[0]
            and "power_change" in r[0]
            and any(row["prev_power"] is None for row in r)
        ),
        "Expected rows for creatures with >= 2 health checks. "
        "First check per creature has NULL prev_power and NULL power_change"
    )

    r19 = run_query(Q19)
    check(
        "Q19 — AVG() OVER PARTITION BY: power vs species avg",
        r19,
        lambda r: (
            len(r) == 10
            and "species_avg" in r[0]
            and "diff" in r[0]
        ),
        "Expected 10 rows (all creatures), species_avg and diff columns. "
        "No GROUP BY — each row keeps its identity"
    )

    r20 = run_query(Q20)
    check(
        "Q20 — LEAD: time between mission log events",
        r20,
        lambda r: (
            len(r) == 13
            and "next_event_type" in r[0]
            and "minutes_to_next" in r[0]
            and any(row["next_event_type"] is None for row in r)
        ),
        "Expected 13 log rows total. Last event of each mission has NULL next_event_type"
    )

    # ── INTERVIEW QUESTIONS ──────────────────────────────────────────────
    print("\n── INTERVIEW QUESTIONS ─────────────────────────────────────────")

    r21 = run_query(Q21)
    check(
        "Q21 — second highest power_level (DENSE_RANK = 2)",
        r21,
        lambda r: (
            len(r) >= 1
            and "power_level" in r[0]
            and all(float(row["power_level"]) < 99 for row in r)
        ),
        "Expected creature(s) with second highest power_level. "
        "Not the max (99), not less than third. Use DENSE_RANK = 2"
    )

    r22 = run_query(Q22)
    check(
        "Q22 — above both species avg and overall avg (two CTEs)",
        r22,
        lambda r: (
            len(r) >= 1
            and "species_avg" in r[0]
            and "overall_avg" in r[0]
            and all(float(row["power_level"]) > float(row["species_avg"]) for row in r)
            and all(float(row["power_level"]) > float(row["overall_avg"]) for row in r)
            and list(r) == sorted(r, key=lambda x: -float(x["power_level"]))
        ),
        "Each returned creature must be above both its species avg and the overall avg"
    )

    r23a = run_query(Q23a)
    r23b = run_query(Q23b)
    check(
        "Q23a — danger species creatures using IN",
        r23a,
        lambda r: (
            len(r) >= 3
            and "power_level" in r[0]
            and list(r) == sorted(r, key=lambda x: -float(x["power_level"]))
        ),
        "Expected creatures belonging to species with danger_level >= 8. "
        "Ordered by power_level DESC"
    )
    check(
        "Q23b — same result using EXISTS (must match Q23a)",
        r23b,
        lambda r: (
            len(r) == len(r23a)
            and sorted([row["name"] for row in r]) ==
               sorted([row["name"] for row in r23a])
        ),
        "Q23b (EXISTS) must return the same creatures as Q23a (IN)"
    )

    r24 = run_query(Q24)
    check(
        "Q24 — species danger report (CTE + window rank + join)",
        r24,
        lambda r: (
            len(r) >= 2
            and "danger_rank" in r[0]
            and "danger_level" in r[0]
            and r[0]["danger_rank"] == 1
            and list(r) == sorted(r, key=lambda x: x["danger_rank"])
        ),
        "Expected one row per species with creatures. danger_rank 1 = most dangerous. "
        "Ordered by danger_rank ASC"
    )

    r25 = run_query(Q25)
    check(
        "Q25 — running total of creature registrations by date (CTE + window)",
        r25,
        lambda r: (
            len(r) >= 1
            and "new_registrations" in r[0]
            and "total_registered" in r[0]
            and r[-1]["total_registered"] == 10
            and list(r) == sorted(r, key=lambda x: x["registration_date"])
        ),
        "Last row's total_registered must equal 10. Ordered by registration_date ASC"
    )

    print("\n" + "═" * 64 + "\n")
