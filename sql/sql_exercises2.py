"""
╔══════════════════════════════════════════════════════════════════════════╗
║       SQL EXERCISES - MYTHICAL CREATURE STABLE                           ║
║       Exercises - JOINs, Aggregates & Grouping                           ║
╚══════════════════════════════════════════════════════════════════════════╝

HOW TO USE THIS FILE
────────────────────
1. Adjust the values of DB_CONFIG to your local setup.
2. Read each concept definition and exercise statement carefully.
3. Write your SQL query in the string assigned to the variable.
4. Run the tests with:  python 02_stable_sql_joins_exercises.py
   Each test prints ✅ PASS or ❌ FAIL with a clear message.

CONCEPTS COVERED
────────────────
  INNER JOIN, LEFT JOIN, FULL OUTER JOIN, SELF-JOIN, ANTI-JOIN
  COUNT(*) vs COUNT(col)
  SUM(), AVG(), MIN(), MAX()
  GROUP BY — every non-aggregated column must be listed
  HAVING — filters groups after aggregation (≠ WHERE)
  Execution order: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
  The NULL trap: WHERE on right-side column silently kills LEFT JOIN rows
  Anti-join pattern: LEFT JOIN + WHERE right.id IS NULL (safer than NOT IN)

────────────────────────────────────────────────────────────────────────────
SCHEMA REMINDER
────────────────────────────────────────────────────────────────────────────

  species      id, name, danger_level, habitat
  keepers      id, full_name, email, hired_at
  creatures    id, name, species_id → species, origin, power_level,
               in_stable, registered_at
  missions     id, creature_id → creatures, keeper_id → keepers,
               objective, started_at, ended_at, success
  health_checks id, creature_id → creatures, keeper_id → keepers,
               checked_at, notes, power_recorded

NEW TABLES
────────────────────────────────────────────────
  creature_ratings  id, creature_id → creatures, keeper_id → keepers,
                    score (1-10), rated_at
               → Some creatures have no rating yet (LEFT JOIN territory)

  keepers.supervisor_id → keepers (self-referential)
               → Keepers have a supervisor who is also a keeper (SELF-JOIN)
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
    ('Solaris',     3, 'Solar Peaks',          72,   TRUE,  NOW() - INTERVAL '1 year'),
    ('Stonewing',   4, 'Highland Cliffs',      65,   TRUE,  NOW() - INTERVAL '8 months'),
    ('Pearlhoof',   5, 'Enchanted Forest',     45,   TRUE,  NOW() - INTERVAL '5 months'),
    ('Shadowcoil',  6, 'Dark Caverns',         99,   FALSE, NOW() - INTERVAL '3 months'),
    ('Blazethorn',  1, 'Volcanic Peaks',       55,   TRUE,  NOW() - INTERVAL '40 days'),
    ('Glacierfang', 2, 'Nordic Realms',        78,   TRUE,  NOW() - INTERVAL '15 days'),
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
DROP TABLE IF EXISTS mission_logs CASCADE;
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
#   ███████╗██████╗██╗███╗   ██╗███████╗
#        ██║██╔═██║██║████╗  ██║██╔════╝
#        ██║██║ ██║██║██╔██╗ ██║███████╗
#   ██╗  ██║██║ ██║██║██║╚██╗██║╚════██║
#   ███████║██████║██║██║ ╚████║███████║
#   ╚══════╝╚═════╝╚═╝╚═╝  ╚═══╝╚══════╝
#
# ─────────────────────────────────────────────────────────────────────────────
# CONCEPT: INNER JOIN
# ─────────────────────────────────────────────────────────────────────────────
# Returns only rows with a match on BOTH sides.
# If a creature has no matching species row → excluded.
# If a species has no creatures → excluded.
# Syntax:
#   SELECT ... FROM a JOIN b ON b.fk = a.id
#
# ═════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 1 — INNER JOIN (creatures × species)
#
# List all creatures currently in the stable with their species name
# and danger level.
# Return: creature name (aliased as creature), species name (aliased as species),
#         danger_level, power_level
# Condition: in_stable = TRUE
# Order by: danger_level DESC, power_level DESC
# ─────────────────────────────────────────────────────────────────────────────
Q1 = """
SELECT c.name as "creature", s.name as "species", s.danger_level, c.power_level
FROM creatures as c
JOIN species as s ON c.species_id = s.id
WHERE c.in_stable = TRUE
ORDER BY danger_level DESC, power_level DESC

"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 2 — INNER JOIN across 3 tables (creatures × missions × keepers)
#
# List all completed missions (ended_at IS NOT NULL) with:
#   - the creature's name
#   - the keeper's full name (aliased as keeper)
#   - the mission objective
#   - whether it was a success
# Order by: missions.started_at DESC
# ─────────────────────────────────────────────────────────────────────────────
Q2 = """
SELECT c.name, k.full_name AS "keeper", m.objective, m.success 
FROM creatures as c
JOIN missions as m ON c.id = m.creature_id
JOIN keepers as k ON k.id = m.keeper_id
WHERE m.ended_at IS NOT NULL
ORDER BY m.started_at DESC

"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 3 — INNER JOIN (health_checks × creatures × keepers)
#
# List every health check with the creature's name, the keeper's full name,
# the recorded power level, and the check date.
# Return: creature_name, keeper_name, power_recorded, checked_at
# Order by: checked_at DESC
# ─────────────────────────────────────────────────────────────────────────────
Q3 = """
SELECT c.name as creature_name, k.full_name as keeper_name, hc.power_recorded, hc.checked_at
FROM health_checks as hc
JOIN creatures as c ON c.id = hc.creature_id
JOIN keepers as k ON k.id = hc.keeper_id
ORDER BY hc.checked_at DESC


"""


# ═════════════════════════════════════════════════════════════════════════════
# CONCEPT: LEFT JOIN
# ─────────────────────────────────────────────────────────────────────────────
# Returns ALL rows from the left table.
# Rows from the right table are matched where possible.
# Where there is no match, right-side columns are NULL.
# Nothing from the left table is ever dropped.
#
# ⚠️  NULL TRAP — the most common interview killer:
#   A WHERE filter on a right-side column runs AFTER the JOIN.
#   It eliminates NULL rows, silently converting LEFT JOIN → INNER JOIN.
#
#   WRONG:  LEFT JOIN ratings r ON r.creature_id = c.id
#           WHERE r.score > 5                         ← kills unrated creatures
#
#   RIGHT:  LEFT JOIN ratings r ON r.creature_id = c.id
#                              AND r.score > 5        ← filter during the JOIN
# ═════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 4 — LEFT JOIN (creatures → creature_ratings)
#
# List ALL creatures with their average rating score.
# Creatures that have never been rated must appear with NULL as avg_score.
# Return: creature name, avg_score (rounded to 1 decimal, aliased as avg_score)
# Order by: avg_score DESC NULLS LAST, name ASC
# ─────────────────────────────────────────────────────────────────────────────
Q4 = """
SELECT c.name, ROUND(AVG(cr.score),1) as avg_score
FROM creatures as c
LEFT JOIN creature_ratings as cr ON cr.creature_id = c.id
GROUP BY c.name
ORDER BY avg_score DESC NULLS LAST, c.name ASC
"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 5 — LEFT JOIN (creatures → missions)
#
# List ALL creatures with the total number of missions they have been on.
# Creatures that have never been on a mission must appear with 0 missions.
# Return: creature name, mission_count
# Order by: mission_count DESC, name ASC
#
# 💡 Hint: COUNT(col) ignores NULLs — use it wisely.
# ─────────────────────────────────────────────────────────────────────────────
Q5 = """
SELECT c.name as name, COUNT(creature_id) as mission_count
FROM creatures as c
LEFT JOIN missions as m ON c.id = m.creature_id
GROUP BY c.name
ORDER BY mission_count DESC, c.name ASC


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 6 — LEFT JOIN (keepers → missions)
#
# List ALL keepers with the number of missions they have led.
# Keepers who have led no missions must appear with 0.
# Return: keeper full_name, mission_count
# Order by: mission_count DESC
# ─────────────────────────────────────────────────────────────────────────────
Q6 = """
SELECT k.full_name, COUNT(m.keeper_id) as mission_count
FROM keepers as k
LEFT JOIN missions as m ON k.id = m.keeper_id
GROUP BY k.full_name
ORDER BY mission_count DESC


"""


# ═════════════════════════════════════════════════════════════════════════════
# CONCEPT: ANTI-JOIN
# ─────────────────────────────────────────────────────────────────────────────
# Finds rows in table A with NO match in table B.
# Pattern: LEFT JOIN + WHERE right_table.id IS NULL
#
# Why not NOT IN?
#   NOT IN (subquery) returns 0 rows if the subquery contains ANY NULL.
#   LEFT JOIN + IS NULL is always safe.
#
#   WRONG (fragile):  WHERE c.id NOT IN (SELECT creature_id FROM missions)
#   RIGHT (safe):     LEFT JOIN missions m ON m.creature_id = c.id
#                     WHERE m.id IS NULL
# ═════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 7 — ANTI-JOIN (creatures with no missions)
#
# Find all creatures that have NEVER been on a mission.
# Return: creature name, species_id, power_level
# Order by: power_level DESC
# ─────────────────────────────────────────────────────────────────────────────
Q7 = """
SELECT c.name, c.species_id, c.power_level
FROM creatures as c
LEFT JOIN missions as m On c.id = m.creature_id
WHERE m.id IS NULL
ORDER BY c.power_level DESC


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 8 — ANTI-JOIN (creatures with no rating)
#
# Find all creatures that have received NO rating yet.
# Return: creature name, in_stable
# Order by: name ASC
# ─────────────────────────────────────────────────────────────────────────────
Q8 = """
SELECT c.name, c.in_stable
FROM creatures as c
LEFT JOIN creature_ratings as cr ON cr.creature_id = c.id
WHERE cr.id IS NULL
ORDER BY c.name ASC


"""


# ═════════════════════════════════════════════════════════════════════════════
# CONCEPT: SELF-JOIN
# ─────────────────────────────────────────────────────────────────────────────
# A table joined to itself using two different aliases.
# Used when rows in a table reference other rows in the same table.
# Classic use case: employees and their managers in the same table.
# Here: keepers and their supervisors, all in the keepers table.
# ═════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 9 — SELF-JOIN (keepers → supervisors)
#
# List each keeper alongside their supervisor's name.
# The head keeper (no supervisor) must still appear with NULL as supervisor.
# Return: keeper_name, supervisor_name (NULL if none)
# Order by: supervisor_name NULLS FIRST, keeper_name ASC
# ─────────────────────────────────────────────────────────────────────────────
Q9 = """
SELECT k.full_name as keeper_name, sk.full_name as supervisor_name
FROM keepers as k
LEFT JOIN keepers as sk on k.supervisor_id = sk.id
ORDER BY supervisor_name NULLS FIRST, keeper_name ASC


"""


# ═════════════════════════════════════════════════════════════════════════════
#
#   █████╗  ██████╗  ██████╗ ██████╗ ███████╗ ██████╗  █████╗ ████████╗███████╗███████╗
#  ██╔══██╗██╔════╝ ██╔════╝ ██╔══██╗██╔════╝██╔════╝ ██╔══██╗╚══██╔══╝██╔════╝██╔════╝
#  ███████║██║  ███╗██║  ███╗██████╔╝█████╗  ██║  ███╗███████║   ██║   █████╗  ███████╗
#  ██╔══██║██║   ██║██║   ██║██╔══██╗██╔══╝  ██║   ██║██╔══██║   ██║   ██╔══╝  ╚════██║
#  ██║  ██║╚██████╔╝╚██████╔╝██║  ██║███████╗╚██████╔╝██║  ██║   ██║   ███████╗███████║
#  ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝
#
# ─────────────────────────────────────────────────────────────────────────────
# CONCEPT: AGGREGATE FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
# COUNT(*)      → counts all rows, including NULLs
# COUNT(col)    → counts only non-NULL values in that column
# SUM(col)      → total of all values
# AVG(col)      → average (ignores NULLs)
# MIN(col)      → smallest value
# MAX(col)      → largest value
#
# CONCEPT: GROUP BY
# ─────────────────────────────────────────────────────────────────────────────
# Collapses rows into groups — one row per unique value of the grouped column.
# Every non-aggregated column in SELECT must appear in GROUP BY.
# Rule of thumb: if it is not inside COUNT/SUM/AVG/MIN/MAX → it goes in GROUP BY.
#
# CONCEPT: HAVING
# ─────────────────────────────────────────────────────────────────────────────
# Filters groups AFTER aggregation — the only place you can use aggregate
# functions in a condition.
# WHERE  → filters rows before grouping  (cannot use SUM, COUNT, etc.)
# HAVING → filters groups after grouping (can use SUM, COUNT, etc.)
#
# EXECUTION ORDER (memorise this):
#   FROM / JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
# ═════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 10 — GROUP BY (species)
#
# Count the number of creatures per species.
# Return: species name (aliased as species), creature_count
# Order by: creature_count DESC, species ASC
# ─────────────────────────────────────────────────────────────────────────────
Q10 = """
SELECT s.name as species, COUNT(c.id) as creature_count
FROM species as s
JOIN creatures as c ON c.species_id = s.id
GROUP BY s.name
ORDER BY creature_count DESC, species ASC


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 11 — AVG + GROUP BY
#
# Compute the average power level per species.
# Return: species name, avg_power (rounded to 2 decimal places)
# Order by: avg_power DESC
# ─────────────────────────────────────────────────────────────────────────────
Q11 = """
SELECT s.name, ROUND(AVG(c.power_level),2) as avg_power
FROM species as s
JOIN creatures as c ON c.species_id = s.id
GROUP BY s.name
ORDER BY avg_power DESC

"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 12 — GROUP BY + HAVING
#
# Find species that have MORE than 1 creature registered.
# Return: species name, creature_count
# Order by: creature_count DESC
# ─────────────────────────────────────────────────────────────────────────────
Q12 = """
SELECT s.name, COUNT(c.id) as creature_count
FROM species as s
JOIN creatures as c ON c.species_id = s.id
GROUP BY s.name
HAVING COUNT(c.id) > 1
ORDER BY creature_count DESC


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 13 — SUM / COUNT across JOIN (missions per keeper)
#
# For each keeper, compute:
#   - total missions led (aliased as total_missions)
#   - successful missions (success = TRUE, aliased as successful_missions)
#   - failed missions (success = FALSE, aliased as failed_missions)
# Include only keepers who have led AT LEAST ONE mission.
# Return: full_name, total_missions, successful_missions, failed_missions
# Order by: total_missions DESC
#
# 💡 Hint: COUNT(col) ignores NULLs. COUNT(CASE WHEN ... END) counts conditionally.
# ─────────────────────────────────────────────────────────────────────────────
Q13 = """
SELECT k.full_name, 
       CASE WHEN k.id = m.keeper_id THEN COUNT(m.id) END  AS total_missions, 
       CASE WHEN k.id = m.keeper_id AND m.success = TRUE THEN COUNT(m.id) END AS successful_missions, 
       CASE WHEN k.id = m.keeper_id AND m.success = FALSE THEN COUNT(m.id) END AS failed_missions
FROM keepers as k
JOIN missions as m ON k.id = m.keeper_id
GROUP BY k.full_name, k.id, m.keeper_id, m.success
ORDER BY total_missions DESC


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 14 — AVG + LEFT JOIN + GROUP BY + HAVING (NULL trap territory)
#
# Find all species whose creatures have an average power level above 60,
# counting ALL creatures — including those not currently in the stable.
# Return: species name, avg_power (rounded to 2 decimals), creature_count
# Condition: avg_power > 60
# Order by: avg_power DESC
# ─────────────────────────────────────────────────────────────────────────────
Q14 = """
SELECT s.name, ROUND(AVG(c.power_level),2) as avg_power, COUNT(c.id) as creature_count
FROM species as s
LEFT JOIN creatures as c ON c.species_id = s.id
GROUP BY s.name
HAVING ROUND(AVG(c.power_level),2) > 60
ORDER BY avg_power DESC


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 15 — MIN / MAX + GROUP BY (health_checks per creature)
#
# For each creature that has had AT LEAST ONE health check, compute:
#   - the minimum power recorded (aliased as min_power)
#   - the maximum power recorded (aliased as max_power)
#   - total number of health checks (aliased as check_count)
# Return: creature name, min_power, max_power, check_count
# Order by: check_count DESC, name ASC
# ─────────────────────────────────────────────────────────────────────────────
Q15 = """
SELECT c.name, MIN(hc.power_recorded) AS min_power, MAX(hc.power_recorded) AS max_power, COUNT(hc.id) AS check_count 
FROM creatures as c
JOIN health_checks as hc On c.id = hc.creature_id
GROUP BY c.name
HAVING COUNT(hc.id) >= 1
ORDER BY check_count DESC, c.name ASC

"""


# ═════════════════════════════════════════════════════════════════════════════
#
#  ██╗  ██╗███████╗██╗   ██╗     ██████╗ ██╗   ██╗███████╗██████╗ ██╗███████╗███████╗
#  ██║ ██╔╝██╔════╝╚██╗ ██╔╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗██║██╔════╝██╔════╝
#  █████╔╝ █████╗   ╚████╔╝     ██║   ██║██║   ██║█████╗  ██████╔╝██║█████╗  ███████╗
#  ██╔═██╗ ██╔══╝    ╚██╔╝      ██║▄▄ ██║██║   ██║██╔══╝  ██╔══██╗██║██╔══╝  ╚════██║
#  ██║  ██╗███████╗   ██║       ╚██████╔╝╚██████╔╝███████╗██║  ██║██║███████╗███████║
#  ╚═╝  ╚═╝╚══════╝   ╚═╝        ╚══▀▀═╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
#
# ─────────────────────────────────────────────────────────────────────────────
# These exercises combine JOIN + GROUP BY + HAVING + ordering in ways that
# mirror real interview questions. No new concepts — just composition.
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 16 — Top-rated creatures
#
# Find the 3 creatures with the highest average rating score.
# Only include creatures that have been rated at least TWICE.
# Return: creature name, avg_score (rounded to 2 decimals), rating_count
# Order by: avg_score DESC
# ─────────────────────────────────────────────────────────────────────────────
Q16 = """
SELECT c.name, ROUND(AVG(cr.score),2) as avg_score, COUNT(cr.id) AS rating_count
FROM creatures as c
JOIN creature_ratings as cr ON cr.creature_id = c.id
GROUP BY c.name
HAVING COUNT(cr.id) >= 2
ORDER BY avg_score DESC
LIMIT 3
"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 17 — Mission success rate per keeper
#
# For each keeper who has led at least one COMPLETED mission (ended_at IS NOT NULL),
# compute their success rate as a percentage (0–100, rounded to 1 decimal).
# Return: keeper full_name, completed_missions, success_rate
# Order by: success_rate DESC
#
# 💡 Hint: success is a BOOLEAN. Cast it to INTEGER to SUM it.
#          CASE WHEN success THEN 1 ELSE 0 END works too.
# ─────────────────────────────────────────────────────────────────────────────
Q17 = """
SELECT k.full_name, 
       COUNT(m.ended_at) AS completed_missions, 
       ROUND(100.0 * COUNT(CAST(m.success AS INTEGER)) / COUNT(*), 1) AS success_rate
from keepers as k
JOIN missions as m ON k.id = m.keeper_id
WHERE ended_at IS NOT NULL
GROUP BY k.full_name
ORDER BY success_rate DESC

"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 18 — Most active keeper per species
#
# For each species, find the keeper who has performed the most health checks
# on creatures of that species.
# Return: species name, keeper full_name, check_count
# Order by: check_count DESC, species ASC
#
# 💡 This is harder — you need GROUP BY on species + keeper, then filter
#    for the maximum. Use a subquery or CTE (WITH) if you know them,
#    or solve it with a carefully ordered GROUP BY first.
# ─────────────────────────────────────────────────────────────────────────────
Q18 = """
SELECT s.name AS species, k.full_name, COUNT(hc.keeper_id) AS check_count
FROM species as s
JOIN creatures as c ON c.species_id = s.id
JOIN health_checks as hc ON hc.creature_id = c.id
JOIN keepers as k ON k.id = hc.keeper_id
GROUP BY s.name, k.full_name
ORDER BY check_count DESC, species ASC

"""


# ═════════════════════════════════════════════════════════════════════════════
#
#  ██╗███╗   ██╗████████╗███████╗██████╗ ██╗   ██╗██╗███████╗██╗    ██╗
#  ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██║   ██║██║██╔════╝██║    ██║
#  ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝██║   ██║██║█████╗  ██║ █╗ ██║
#  ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗╚██╗ ██╔╝██║██╔══╝  ██║███╗██║
#  ██║██║ ╚████║   ██║   ███████╗██║  ██║ ╚████╔╝ ██║███████╗╚███╔███╔╝
#  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝
#
# ─────────────────────────────────────────────────────────────────────────────
# CONCEPT: THE NULL TRAP
# ─────────────────────────────────────────────────────────────────────────────
# A WHERE filter on a right-side column runs AFTER the JOIN.
# It evaluates NULL = 'value' → UNKNOWN → row is dropped.
# Your LEFT JOIN silently becomes an INNER JOIN. No error. No warning.
#
# FIX: move the condition into the ON clause so it runs during the JOIN.
#
# CONCEPT: NOT IN vs ANTI-JOIN
# ─────────────────────────────────────────────────────────────────────────────
# NOT IN (subquery) returns 0 rows if the subquery contains ANY NULL.
# LEFT JOIN + WHERE right.id IS NULL is always safe.
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 19 — Spot and fix the NULL trap
#
# The query below is BROKEN. It tries to list all creatures with any
# high rating (score >= 8) they may have, showing NULL for unrated ones.
# But it silently drops unrated creatures.
#
# YOUR TASK:
#   a) Explain in a comment WHY the query below is wrong.
#   b) Write the fixed version that preserves all creatures.
#
# BROKEN (do not submit this):
#   SELECT c.name, r.score
#   FROM creatures c
#   LEFT JOIN creature_ratings r ON r.creature_id = c.id
#   WHERE r.score >= 8;
#
# Return: creature name, score (NULL if no rating >= 8)
# Order by: score DESC NULLS LAST, name ASC
# ─────────────────────────────────────────────────────────────────────────────
Q19 = """
-- a) WHY is the broken query wrong?
--    (write your explanation as a comment here)
--
--
-- b) Write the fixed query below:
SELECT c.name, r.score
FROM creatures c
LEFT JOIN creature_ratings r ON r.creature_id = c.id
AND r.score >= 8
ORDER BY r.score DESC NULLS LAST, c.name ASC


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 20 — NOT IN vs ANTI-JOIN
#
# Find all creatures that have NEVER been rated — using the safe ANTI-JOIN
# pattern (LEFT JOIN + WHERE r.id IS NULL), NOT a NOT IN subquery.
#
# Then, as a comment, explain what would go wrong if you used:
#   WHERE c.id NOT IN (SELECT creature_id FROM creature_ratings)
# … if creature_ratings ever contained a NULL creature_id.
#
# Return: creature name, origin, power_level
# Order by: power_level DESC
# ─────────────────────────────────────────────────────────────────────────────
Q20 = """
-- Write the safe anti-join query here.
-- Add a comment explaining the NOT IN NULL risk.

SELECT c.name, c.origin, c.power_level
FROM creatures as c
LEFT JOIN creature_ratings as cr ON cr.creature_id = c.id 
WHERE cr.id IS NULL
ORDER BY power_level DESC
"""


# ═════════════════════════════════════════════════════════════════════════════
#  TEST RUNNER — do not modify below this line
# ═════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\n" + "═" * 64)
    print("  STABLE SQL EXERCISES — Day 2: JOINs, Aggregates & Grouping")
    print("═" * 64 + "\n")

    setup_database(get_conn())

    # ── JOINs ─────────────────────────────────────────────────────────────

    print("── INNER JOIN ──────────────────────────────────────────────────")

    r1 = run_query(Q1)
    check(
        "Q1 — in-stable creatures with species name and danger_level",
        r1,
        lambda r: (
            len(r) == 8
            and "creature" in r[0]
            and "species"  in r[0]
            and "danger_level" in r[0]
            and all(isinstance(row["danger_level"], int) for row in r)
            and list(r) == sorted(r, key=lambda x: (-x["danger_level"], -float(x["power_level"])))
        ),
        "Expected 8 rows (in_stable=TRUE), columns: creature, species, danger_level, power_level. "
        "Ordered by danger_level DESC then power_level DESC"
    )

    r2 = run_query(Q2)
    check(
        "Q2 — completed missions with creature name and keeper name",
        r2,
        lambda r: (
            len(r) == 3
            and "keeper" in r[0]
            and "objective" in r[0]
            and "success"   in r[0]
        ),
        "Expected 3 rows (ended_at IS NOT NULL), columns include: keeper, objective, success"
    )

    r3 = run_query(Q3)
    check(
        "Q3 — health checks with creature and keeper names",
        r3,
        lambda r: (
            len(r) == 5
            and "creature_name" in r[0]
            and "keeper_name"   in r[0]
            and "power_recorded" in r[0]
            and "checked_at"    in r[0]
            and list(r) == sorted(r, key=lambda x: x["checked_at"], reverse=True)
        ),
        "Expected 5 rows, columns: creature_name, keeper_name, power_recorded, checked_at. Ordered by checked_at DESC"
    )

    print("\n── LEFT JOIN ───────────────────────────────────────────────────")

    r4 = run_query(Q4)
    check(
        "Q4 — all creatures with avg rating (NULL for unrated)",
        r4,
        lambda r: (
            len(r) == 10
            and "avg_score" in r[0]
            and any(row["avg_score"] is None for row in r)
            and all(
                r[i]["avg_score"] is None or r[i+1]["avg_score"] is None
                or float(r[i]["avg_score"]) >= float(r[i+1]["avg_score"])
                for i in range(len(r) - 1)
                if r[i]["avg_score"] is not None and r[i+1]["avg_score"] is not None
            )
        ),
        "Expected 10 rows (all creatures), avg_score NULL for unrated ones, "
        "ordered by avg_score DESC NULLS LAST"
    )

    r5 = run_query(Q5)
    check(
        "Q5 — all creatures with mission count (0 if none)",
        r5,
        lambda r: (
            len(r) == 10
            and "mission_count" in r[0]
            and any(row["mission_count"] == 0 for row in r)
            and list(r) == sorted(r, key=lambda x: (-x["mission_count"], x["name"]))
        ),
        "Expected 10 rows, mission_count = 0 for creatures with no missions. "
        "Ordered by mission_count DESC, name ASC"
    )

    r6 = run_query(Q6)
    check(
        "Q6 — all keepers with mission count (0 if none)",
        r6,
        lambda r: (
            len(r) >= 3
            and "mission_count" in r[0]
            and any(row["mission_count"] >= 0 for row in r)
            and list(r) == sorted(r, key=lambda x: -x["mission_count"])
        ),
        "Expected at least 3 rows (all keepers), mission_count = 0 for keepers "
        "with no missions. Ordered by mission_count DESC"
    )

    print("\n── ANTI-JOIN ───────────────────────────────────────────────────")

    r7 = run_query(Q7)
    check(
        "Q7 — creatures with no mission (anti-join)",
        r7,
        lambda r: (
            len(r) == 6
            and "power_level" in r[0]
            and list(r) == sorted(r, key=lambda x: -float(x["power_level"]))
        ),
        "Expected 6 creatures that have never been on a mission, ordered by power_level DESC"
    )

    r8 = run_query(Q8)
    check(
        "Q8 — creatures with no rating (anti-join)",
        r8,
        lambda r: (
            len(r) == 5
            and "in_stable" in r[0]
            and list(r) == sorted(r, key=lambda x: x["name"])
        ),
        "Expected 5 creatures with no rating entry, ordered by name ASC"
    )

    print("\n── SELF-JOIN ───────────────────────────────────────────────────")

    r9 = run_query(Q9)
    check(
        "Q9 — keepers with their supervisor (NULL for head keeper)",
        r9,
        lambda r: (
            len(r) == 3
            and any(row.get("supervisor_name") is None for row in r)
            and "keeper_name" in r[0]
            and "supervisor_name" in r[0]
        ),
        "Expected 3 rows, head keeper has NULL supervisor_name. "
        "Columns: keeper_name, supervisor_name"
    )

    print("\n── AGGREGATES & GROUP BY ───────────────────────────────────────")

    r10 = run_query(Q10)
    check(
        "Q10 — creature count per species",
        r10,
        lambda r: (
            len(r) == 6
            and "creature_count" in r[0]
            and "species" in r[0]
            and list(r) == sorted(r, key=lambda x: (-x["creature_count"], x["species"]))
        ),
        "Expected 6 species rows (only species that have creatures). "
        "Ordered by creature_count DESC, species ASC"
    )

    r11 = run_query(Q11)
    check(
        "Q11 — avg power per species",
        r11,
        lambda r: (
            len(r) == 6
            and "avg_power" in r[0]
            and list(r) == sorted(r, key=lambda x: -float(x["avg_power"]))
        ),
        "Expected 6 rows ordered by avg_power DESC"
    )

    r12 = run_query(Q12)
    check(
        "Q12 — species with more than 1 creature (HAVING)",
        r12,
        lambda r: (
            len(r) == 3
            and all(row["creature_count"] > 1 for row in r)
            and list(r) == sorted(r, key=lambda x: -x["creature_count"])
        ),
        "Expected 3 species (Dragon ×3, Phoenix ×2, Ice Dragon ×2). Ordered by creature_count DESC"
    )

    r13 = run_query(Q13)
    check(
        "Q13 — missions per keeper with success/fail breakdown",
        r13,
        lambda r: (
            len(r) == 3
            and "total_missions"      in r[0]
            and "successful_missions" in r[0]
            and "failed_missions"     in r[0]
            and list(r) == sorted(r, key=lambda x: -x["total_missions"])
        ),
        "Expected 3 keepers (those who led at least 1 mission), "
        "with total_missions, successful_missions, failed_missions. Ordered by total_missions DESC"
    )

    r14 = run_query(Q14)
    check(
        "Q14 — species with avg power > 60",
        r14,
        lambda r: (
            len(r) == 4
            and "avg_power" in r[0]
            and "creature_count" in r[0]
            and all(float(row["avg_power"]) > 60 for row in r)
            and list(r) == sorted(r, key=lambda x: -float(x["avg_power"]))
        ),
        "Expected 4 species whose avg power_level > 60. Ordered by avg_power DESC"
    )

    r15 = run_query(Q15)
    check(
        "Q15 — min/max power and check count per creature",
        r15,
        lambda r: (
            len(r) == 4
            and "min_power"   in r[0]
            and "max_power"   in r[0]
            and "check_count" in r[0]
            and list(r) == sorted(r, key=lambda x: (-x["check_count"], x["name"]))
        ),
        "Expected 4 creatures (those with at least 1 health check), "
        "columns: name, min_power, max_power, check_count. Ordered by check_count DESC, name ASC"
    )

    print("\n── KEY QUERIES ─────────────────────────────────────────────────")

    r16 = run_query(Q16)
    check(
        "Q16 — top 3 creatures rated at least twice",
        r16,
        lambda r: (
            len(r) == 1
            and "avg_score"     in r[0]
            and "rating_count"  in r[0]
            and all(row["rating_count"] >= 2 for row in r)
            and list(r) == sorted(r, key=lambda x: -float(x["avg_score"]))
        ),
        "Expected 1 creature rated >= 2 times (Frostbite has 2 ratings). "
        "Ordered by avg_score DESC, LIMIT 3"
    )

    r17 = run_query(Q17)
    check(
        "Q17 — mission success rate per keeper (completed missions only)",
        r17,
        lambda r: (
            len(r) == 2
            and "success_rate"        in r[0]
            and "completed_missions"  in r[0]
            and all(0 <= float(row["success_rate"]) <= 100 for row in r)
            and list(r) == sorted(r, key=lambda x: -float(x["success_rate"]))
        ),
        "Expected 2 keepers with completed missions, success_rate 0–100. "
        "Ordered by success_rate DESC"
    )

    r18 = run_query(Q18)
    check(
        "Q18 — most active keeper per species (health checks)",
        r18,
        lambda r: (
            len(r) >= 2
            and "check_count" in r[0]
            and list(r) == sorted(r, key=lambda x: (-x["check_count"], x.get("species", "")))
        ),
        "Expected at least 2 rows (species that have health checks). "
        "Ordered by check_count DESC, species ASC"
    )

    print("\n── INTERVIEW TRAPS ─────────────────────────────────────────────")

    r19 = run_query(Q19)
    check(
        "Q19 — NULL trap fixed: all creatures with high ratings or NULL",
        r19,
        lambda r: (
            len(r) == 11
            and any(row.get("score") is None for row in r)
            and all(
                row.get("score") is None or int(row["score"]) >= 8
                for row in r
            )
        ),
        "Expected 11 rows (ALL creatures). Unrated or score < 8 → score is NULL. "
        "Fix: move score >= 8 into the ON clause, not WHERE"
    )

    r20 = run_query(Q20)
    check(
        "Q20 — anti-join (no rating) using LEFT JOIN + IS NULL",
        r20,
        lambda r: (
            len(r) == 5
            and "origin"      in r[0]
            and "power_level" in r[0]
            and list(r) == sorted(r, key=lambda x: -float(x["power_level"]))
        ),
        "Expected 5 unrated creatures, ordered by power_level DESC. "
        "Use LEFT JOIN + WHERE r.id IS NULL — not NOT IN"
    )

    print("\n" + "═" * 64 + "\n")
