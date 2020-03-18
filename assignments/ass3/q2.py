import cs3311
import sys

conn = cs3311.connect()
cur1 = conn.cursor()

# TODO

q2_helper1 = """
    CREATE OR REPLACE VIEW q2_helper1 AS
    SELECT SUBSTRING(s.code, 1, 4) AS stream, 
            SUBSTRING(s.code, 5, 4) AS code
    FROM subjects s
    ORDER BY code ASC, stream ASC
    ;
"""

q2_helper2 = """
    CREATE OR REPLACE VIEW q2_helper2 AS
    SELECT code, COUNT(DISTINCT stream) as codenum
    FROM q2_helper1
    GROUP BY code
    ;
"""

q2 = """
    SELECT t.code, STRING_AGG(o.stream, ' ') AS streams
    FROM q2_helper2 t, q2_helper1 o
    WHERE t.codenum = %s AND t.code = o.code
    GROUP BY t.code
    ;
"""

cur1.execute(q2_helper1)
cur1.execute(q2_helper2)
conn.commit()

if (len(sys.argv) == 1):
    cur1.execute(q2, [2])
else:
    cur1.execute(q2, [int(sys.argv[1])])

for record in cur1.fetchall():
    print(str(record[0])+":",record[1])


cur1.close()
conn.close()
