import cs3311
import sys

conn = cs3311.connect()

cur1 = conn.cursor()

# TODO

q3_helper = """
    CREATE OR REPLACE VIEW q3_helper AS
    SELECT SUBSTRING(s.code, 1, 4) as stream, 
            s.code as code, 
            b.name as building
    FROM subjects s
    INNER JOIN courses co ON s.id = co.subject_id
    INNER JOIN classes cl ON co.id = cl.course_id
    INNER JOIN meetings m ON cl.id = m.class_id
    INNER JOIN rooms r ON m.room_id = r.id
    INNER JOIN buildings b ON r.within = b.id
    WHERE co.term_id = 5196
    GROUP BY stream, s.code, building
    ORDER BY building ASC, stream ASC, code ASC
    ;
"""

q3 = """
    SELECT building, stream, code
    FROM q3_helper q
    WHERE stream = %s
    ;
"""

cur1.execute(q3_helper)
conn.commit()

if (len(sys.argv) == 1):
    cur1.execute(q3, ["ENGG"])
else:
    cur1.execute(q3, [sys.argv[1]])

prev = None
for record in cur1.fetchall():
    if (prev != record[0]):
        print(record[0])
        prev = record[0]
    print(" "+str(record[2]))



cur1.close()
conn.close()
