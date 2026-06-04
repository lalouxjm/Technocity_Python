

"""
╔══════════════════════════════════════════════════════════════════════════╗
║       SQL EXERCISES — MYTHICAL CREATURE STABLE                           ║
║       Basic SQL Queries                                                  ║
╚══════════════════════════════════════════════════════════════════════════╝

HOW TO USE THIS FILE
────────────────────
1. Run the SETUP block below once in PgAdmin (Tools > Query Tool),
   in console or any other Database tool of your choice.
2. Come back here, read each exercise statement carefully.
3. Write your SQL query in the string assigned to the variable.
4. Run the test with:  python stable_sql_queries_exercises.py
   Each test prints PASS or FAIL with a clear message.

CONCEPTS COVERED
────────────────
  SELECT, FROM, WHERE, ORDER BY, LIMIT, OFFSET
  Filtering: =, !=, >, <, BETWEEN, IN, LIKE, IS NULL, IS NOT NULL
  INSERT INTO ... VALUES and RETURNING
  UPDATE ... SET ... WHERE
  DELETE FROM ... WHERE
  DISTINCT
  Aliases (AS)
  String functions: LOWER(), UPPER(), TRIM(), CONCAT(), LENGTH()
  Date functions: NOW(), EXTRACT(), DATE_TRUNC(), AGE()
  COALESCE()
  Casting: CAST() and ::
"""

import psycopg
import psycopg.rows

# ─────────────────────────────────────────────────────────────────────────────
# CONNECTION — adjust to your local setup
# ─────────────────────────────────────────────────────────────────────────────
DB_CONFIG = {
    "host":     "localhost",
    "port":     5432,
    "dbname":   "mythical_creature_stable",      # change if your DB has a different name
    "user":     "postgres",       # change to your user
    "password": "postgrespwd",       # change to your password
}


# ─────────────────────────────────────────────────────────────────────────────
# SETUP — run this block ONCE in your PyCharm Database console or in PgAdmin
# ─────────────────────────────────────────────────────────────────────────────
SETUP_SQL = """
-- Run this entire block in your PyCharm Database console or in PgAdmin first.
-- It creates the schema and inserts seed data so the exercises work.

DROP TABLE IF EXISTS health_checks, creature_missions, missions, creatures, keepers, species CASCADE;
DROP TABLE IF EXISTS creature_ratings CASCADE;

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

DROP TABLE IF EXISTS creature_ratings CASCADE;
DROP TABLE IF EXISTS mission_logs CASCADE;
"""


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS — do not modify
# ─────────────────────────────────────────────────────────────────────────────
def get_conn():
    return psycopg.connect(**DB_CONFIG)

def reset_database():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(SETUP_SQL)
            conn.commit()
            
def run_query(sql: str) -> list[dict]:
    with get_conn() as conn:
        with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
            cur.execute(sql)
            return cur.fetchall()

def run_write(sql: str) -> list[dict] | None:
    with get_conn() as conn:
        with conn.cursor(row_factory=psycopg.rows.dict_row) as cur:
            cur.execute(sql)
            conn.commit()
            try:
                return cur.fetchall()
            except Exception:
                return None

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
#  EXERCISES
#  Write your SQL query inside the triple-quoted string for each exercise.
#  Do not change anything outside the query strings.
# ═════════════════════════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 1 — SELECT, WHERE with LIKE
#
# Find all creatures whose origin contains the word 'Peaks'.
# Return: name, origin
# Order by: name ASC
# ─────────────────────────────────────────────────────────────────────────────
Q1 = """
SELECT name, origin 
FROM creatures
WHERE origin like '%Peaks%'
ORDER BY name ASC


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 2 — WHERE with comparison operators
#
# Find all creatures with a power_level strictly above 70.
# Return: name, power_level
# Order by: power_level DESC
# ─────────────────────────────────────────────────────────────────────────────
Q2 = """
SELECT name, power_level 
FROM creatures
WHERE power_level > 70
ORDER BY power_level DESC    


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 3 — WHERE with BETWEEN
#
# Find all creatures whose power_level is between 50 and 80 (inclusive).
# Return: name, power_level
# Order by: power_level ASC
# ─────────────────────────────────────────────────────────────────────────────
Q3 = """
SELECT name, power_level 
FROM creatures
WHERE power_level BETWEEN 50 AND 80
ORDER BY power_level ASC


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 4 — WHERE with IN
#
# Find all creatures whose species_id is in the list (1, 2)
# (Dragons and Ice Dragons).
# Return: name, species_id, power_level
# Order by: species_id ASC, name ASC
# ─────────────────────────────────────────────────────────────────────────────
Q4 = """
SELECT  name, species_id, power_level 
FROM creatures
WHERE species_id IN (1,2)
ORDER BY species_id ASC, name ASC


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 5 — WHERE with boolean and IS NULL / IS NOT NULL
#
# Find all creatures that are currently NOT in the stable
# AND whose mission end date (look at missions.ended_at) is NULL
# — meaning their mission is still ongoing.
#
# HINT: for this exercise, query the missions table directly.
# Return: creature_id, objective, started_at, ended_at
# ─────────────────────────────────────────────────────────────────────────────
Q5 = """
    SELECT creature_id, objective, started_at, ended_at 
    FROM missions as m
    JOIN creatures as c ON m.creature_id = c.id
    WHERE c.in_stable = FALSE and m.ended_at IS NULL


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 6 — DISTINCT
#
# List all distinct origins that appear in the creatures table.
# Return: origin
# Order by: origin ASC
# ─────────────────────────────────────────────────────────────────────────────
Q6 = """
SELECT DISTINCT origin
FROM creatures
ORDER BY origin ASC

"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 7 — Aliases (AS) + string functions
#
# For every creature, display:
#   - their name in UPPERCASE, aliased as 'creature_name'
#   - their origin in LOWERCASE, aliased as 'origin_lower'
#   - the length of their name, aliased as 'name_length'
# Order by: name_length DESC
# ─────────────────────────────────────────────────────────────────────────────
Q7 = """
SELECT UPPER(name) as "creature_name", LOWER(origin) as "origin_lower", lENGTH(name) as "name_length"
FROM creatures
ORDER BY name_length DESC


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 8 — Date functions
#
# Find all creatures registered in the last 30 days.
# Return: name, registered_at
# Order by: registered_at DESC
# ─────────────────────────────────────────────────────────────────────────────
Q8 = """
SELECT name, registered_at
FROM creatures
WHERE registered_at > NOW() - INTERVAL '30 days'
ORDER BY registered_at DESC

"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 9 — EXTRACT + date functions
#
# For each mission, display:
#   - the objective
#   - the year it started, aliased as 'mission_year'
#   - the month it started, aliased as 'mission_month'
# Order by: started_at ASC
# ─────────────────────────────────────────────────────────────────────────────
Q9 = """
SELECT objective, EXTRACT(YEAR FROM started_at) AS "mission_year", EXTRACT(MONTH FROM started_at) AS "mission_month"
FROM missions
ORDER BY started_at ASC


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 10 — COALESCE
#
# For each health check, display:
#   - the creature_id
#   - the notes — but if notes is NULL, display 'No notes recorded' instead
#     (use COALESCE), aliased as 'notes'
#   - the power_recorded
# Order by: creature_id ASC
# ─────────────────────────────────────────────────────────────────────────────
Q10 = """
SELECT creature_id, COALESCE(notes, 'No notes recorded') as "notes", power_recorded
FROM health_checks
ORDER BY creature_id ASC

"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 11 — Casting
#
# Display each creature's name and their power_level cast to INTEGER,
# aliased as 'power_int'.
# Order by: power_int DESC
# ─────────────────────────────────────────────────────────────────────────────
Q11 = """
SELECT name, CAST(power_level AS INTEGER) AS "power_int"
FROM CREATURES
ORDER BY power_int DESC


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 12 — LIMIT and OFFSET
#
# Paginate the creatures table: return page 2, with 3 creatures per page.
# (i.e. skip the first 3, return the next 3)
# Return: id, name, power_level
# Order by: id ASC   ← always sort before paginating
# ─────────────────────────────────────────────────────────────────────────────
Q12 = """
SELECT id, name, power_level
FROM creatures
ORDER BY id ASC
LIMIT 3
OFFSET 3


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 13 — INSERT INTO ... VALUES + RETURNING
#
# Insert a new keeper into the keepers table:
#   full_name = 'Elowen Drakemoor'
#   email     = 'elowen@stable.com'
#
# Use RETURNING to get back the generated id and hired_at.
# ─────────────────────────────────────────────────────────────────────────────
Q13 = """
INSERT INTO keepers (full_name, email)
VALUES ('Elowen Drakemoor', 'elowen@stable.com')
ON CONFLICT (email)
DO UPDATE SET
    email = keepers.email
RETURNING id, hired_at



"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 14 — UPDATE ... SET ... WHERE
#
# A power surge hit the stable! Increase the power_level of all creatures
# from the 'Nordic Realms' origin by 2 points.
#
# ⚠️  Do NOT forget the WHERE clause.
# Use RETURNING to see which rows were updated (id, name, power_level).
#
# NOTE: power_level has a CHECK constraint — it cannot exceed 100.
#       The seed data is designed so no creature goes over 100 here.
# ─────────────────────────────────────────────────────────────────────────────
Q14 = """
UPDATE creatures
SET power_level = power_level + 2
WHERE origin = 'Nordic Realms'
RETURNING id, name, power_level


"""


# ─────────────────────────────────────────────────────────────────────────────
# EXERCISE 15 — DELETE ... WHERE
#
# The health check records older than 15 days must be purged.
# Delete all health_checks where checked_at is older than 15 days.
#
# ⚠️  Do NOT forget the WHERE clause.
# Use RETURNING to confirm which rows were deleted (id, creature_id, checked_at).
# ─────────────────────────────────────────────────────────────────────────────
Q15 = """
DELETE FROM health_checks
WHERE checked_at < NOW() - INTERVAL '15 days'
RETURNING id, creature_id, checked_at


"""


# ═════════════════════════════════════════════════════════════════════════════
#  TEST RUNNER — updated tests below (fixes incorrect expectations)
# ═════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":

    reset_database()

    print("\n" + "═" * 60)
    print("  STABLE SQL EXERCISES — Test Runner")
    print("═" * 60 + "\n")

    # --- Q1 ---
    r1 = run_query(Q1)
    check(
        "Q1 — creatures whose origin contains 'Peaks'",
        r1,
        lambda r: (
            len(r) == 4
            and all("peaks" in row["origin"].lower() for row in r)
            and [row["name"] for row in r] == sorted(row["name"] for row in r)
        ),
        "Expected 4 rows (Volcanic Peaks x2, Solar Peaks x2), ordered by name ASC"
    )

    # --- Q2 ---
    r2 = run_query(Q2)
    check(
        "Q2 — creatures with power_level > 70",
        r2,
        lambda r: (
            len(r) == 5
            and all(float(row["power_level"]) > 70 for row in r)
            and list(r) == sorted(r, key=lambda x: float(x["power_level"]), reverse=True)
        ),
        "Expected 5 rows, ordered by power_level DESC"
    )

    # --- Q3 ---
    r3 = run_query(Q3)
    check(
        "Q3 — power_level BETWEEN 50 AND 80",
        r3,
        lambda r: (
            len(r) == 5
            and all(50 <= float(row["power_level"]) <= 80 for row in r)
            and list(r) == sorted(r, key=lambda x: float(x["power_level"]))
        ),
        "Expected 5 rows (50–80 inclusive), ordered by power_level ASC"
    )

    # --- Q4 ---
    r4 = run_query(Q4)
    check(
        "Q4 — creatures with species_id IN (1, 2)",
        r4,
        lambda r: (
            len(r) == 5
            and all(row["species_id"] in (1, 2) for row in r)
        ),
        "Expected 5 rows (3 Dragons + 2 Ice Dragons)"
    )

    # --- Q5 ---
    # Exercise requires: creature NOT in stable AND mission ended_at IS NULL.
    r5 = run_query(Q5)
    not_in_stable_ids = {row["id"] for row in run_query("SELECT id FROM creatures WHERE in_stable = FALSE;")}
    check(
        "Q5 — ongoing missions for creatures NOT in the stable (ended_at IS NULL AND in_stable = FALSE)",
        r5,
        lambda r: (
            len(r) == 1
            and r[0]["ended_at"] is None
            and r[0]["creature_id"] in not_in_stable_ids
        ),
        "Expected 1 row — a mission with ended_at NULL whose creature is not in stable (Shadowcoil)."
    )

    # --- Q6 ---
    r6 = run_query(Q6)
    check(
        "Q6 — DISTINCT origins, ordered ASC",
        r6,
        lambda r: (
            len(r) == 7
            and "origin" in r[0]
            and r == sorted(r, key=lambda x: x["origin"])
        ),
        "Expected 7 distinct origins, ordered alphabetically"
    )

    # --- Q7 ---
    r7 = run_query(Q7)
    check(
        "Q7 — UPPER(name), LOWER(origin), LENGTH(name), ordered by name_length DESC",
        r7,
        lambda r: (
            len(r) == 10
            and "creature_name" in r[0]
            and "origin_lower" in r[0]
            and "name_length" in r[0]
            and r[0]["creature_name"] == r[0]["creature_name"].upper()
            and r[0]["origin_lower"] == r[0]["origin_lower"].lower()
            and list(r) == sorted(r, key=lambda x: x["name_length"], reverse=True)
        ),
        "Check aliases: creature_name, origin_lower, name_length. Ordered by name_length DESC"
    )

    # --- Q8 ---
    r8 = run_query(Q8)
    check(
        "Q8 — creatures registered in the last 30 days",
        r8,
        lambda r: (
            len(r) == 3
            and "name" in r[0]
            and "registered_at" in r[0]
        ),
        "Expected 3 rows (registered within 30 days), ordered by registered_at DESC"
    )

    # --- Q9 ---
    r9 = run_query(Q9)
    check(
        "Q9 — EXTRACT year and month from missions.started_at",
        r9,
        lambda r: (
            len(r) == 4
            and "mission_year" in r[0]
            and "mission_month" in r[0]
            and "objective" in r[0]
        ),
        "Expected 4 rows with columns: objective, mission_year, mission_month"
    )

    # --- Q10 ---
    r10 = run_query(Q10)
    check(
        "Q10 — COALESCE(notes, 'No notes recorded')",
        r10,
        lambda r: (
            len(r) >= 1
            and all(row["notes"] is not None for row in r)
            and any(row["notes"] == "No notes recorded" for row in r)
        ),
        "Expected no NULL notes — NULLs replaced by 'No notes recorded'"
    )

    # --- Q11 ---
    r11 = run_query(Q11)
    check(
        "Q11 — power_level cast to INTEGER, aliased as power_int",
        r11,
        lambda r: (
            len(r) == 10
            and "power_int" in r[0]
            and isinstance(r[0]["power_int"], int)
            and list(r) == sorted(r, key=lambda x: x["power_int"], reverse=True)
        ),
        "Expected 10 rows, power_int as integer type, ordered DESC"
    )

    # --- Q12 ---
    r12 = run_query(Q12)
    check(
        "Q12 — LIMIT 3 OFFSET 3 (page 2)",
        r12,
        lambda r: (
            len(r) == 3
            and r[0]["id"] == 4
            and r[1]["id"] == 5
            and r[2]["id"] == 6
        ),
        "Expected creatures with id 4, 5, 6 (ordered by id ASC, skip first 3)"
    )

    # --- Q13 ---
    r13 = run_write(Q13)
    check(
        "Q13 — INSERT new keeper, RETURNING id and hired_at",
        r13,
        lambda r: (
            r is not None
            and len(r) == 1
            and "id" in r[0]
            and "hired_at" in r[0]
            and r[0]["id"] is not None
        ),
        "Expected 1 returned row with id and hired_at columns"
    )

    # --- Q14 ---
    r14 = run_write(Q14)
    check(
        "Q14 — UPDATE power_level +2 for Nordic Realms creatures",
        r14,
        lambda r: (
            r is not None
            and len(r) == 2
            and all("name" in row and "power_level" in row for row in r)
        ),
        "Expected 2 updated rows (Frostbite and Glacierfang), with RETURNING id, name, power_level"
    )

    # --- Q15 ---
    r15 = run_write(Q15)
    check(
        "Q15 — DELETE health_checks older than 15 days",
        r15,
        lambda r: (
            r is not None
            and len(r) == 1
            and all("id" in row and "checked_at" in row for row in r)
        ),
        "Expected 1 deleted row (the check from 30 days ago), with RETURNING"
    )

    print("\n" + "═" * 60 + "\n")