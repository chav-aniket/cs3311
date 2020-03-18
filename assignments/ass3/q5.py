import cs3311
import sys

conn = cs3311.connect()

cur1 = conn.cursor()

# TODO

q5 = """
    SELECT s.code AS code, 
            cl.quota AS quota, 
            COUNT(DISTINCT ce.person_id) AS enrols,
            ct.name as classtype,
            cl.tag
    FROM courses c
    INNER JOIN subjects s ON c.subject_id = s.id
    INNER JOIN classes cl ON cl.course_id = c.id
    INNER JOIN class_enrolments ce ON cl.id = ce.class_id
    INNER JOIN classtypes ct ON cl.type_id = ct.id
    WHERE c.term_id = 5199 AND code = %s
    GROUP BY c.id, cl.quota, s.code, classtype, cl.tag
    ORDER BY classtype ASC
    ;
"""

if (len(sys.argv) == 1):
    cur1.execute(q5, ["COMP1521"])
else:
    cur1.execute(q5, [sys.argv[1]])

for record in cur1.fetchall():
    percent = round((record[2]/record[1])*100)
    if (percent < 50):
        print(record[3],record[4],"is", str(percent)+"%", "full")


cur1.close()
conn.close()
