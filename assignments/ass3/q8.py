import cs3311
conn = cs3311.connect()

cur1 = conn.cursor()

# TODO

q8_1 = """
    SELECT m.day, m.start_time, m.end_time,
            s.code, ct.name
    FROM meetings m
    INNER JOIN classes cl ON m.class_id = cl.id
    INNER JOIN courses co ON cl.course_id = co.id
    INNER JOIN classtypes ct ON cl.type_id = ct.id
    INNER JOIN subjects s ON co.subject_id = s.id
    WHERE s.code = %s
    ORDER BY m.day ASC, start_time ASC, end_time ASC
    ;
"""

q8_2 = """
    SELECT m.day, m.start_time, m.end_time,
            s.code, ct.name
    FROM meetings m
    INNER JOIN classes cl ON m.class_id = cl.id
    INNER JOIN courses co ON cl.course_id = co.id
    INNER JOIN classtypes ct ON cl.type_id = ct.id
    INNER JOIN subjects s ON co.subject_id = s.id
    WHERE s.code = %s OR s.code = %s
    ORDER BY m.day ASC, start_time ASC, end_time ASC
    ;
"""

q8_3 = """
    SELECT m.day, m.start_time, m.end_time,
            s.code, ct.name
    FROM meetings m
    INNER JOIN classes cl ON m.class_id = cl.id
    INNER JOIN courses co ON cl.course_id = co.id
    INNER JOIN classtypes ct ON cl.type_id = ct.id
    INNER JOIN subjects s ON co.subject_id = s.id
    WHERE s.code = %s OR s.code = %s OR s.code = %s
    ORDER BY m.day ASC, start_time ASC, end_time ASC
    ;
"""

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# if (len(sys.argv) == 1):
#     cur1.execute(q8_2, ["COMP1511","MATH1131"])
# elif (len(sys.argv) == 2):
#     cur1.execute(q8_1, [sys.argv[1])
# elif (len(sys.argv) == 3):
#     cur1.execute(q8_2, [sys.argv[1], sys.argv[2]])
# elif (len(sys.argv) == 4):
#     cur1.execute(q8_3, [sys.argv[1], sys.argv[2], sys.argv[3]])
# subjects = cur1.fetchall();

subject1 = None
subject2 = None
subject3 = None
if (len(sys.argv) == 1):
    cur1.execute(q8_1, ["COMP1511"])
    subject1 = cur1.fetchall()
    cur1.execute(q8_1, ["COMP1511"])
    subject2 = cur1.fetchall()
elif (len(sys.argv) == 2):
    cur1.execute(q8_1, [sys.argv[1])
    subject1 = cur1.fetchall()
elif (len(sys.argv) == 3):
    cur1.execute(q8_1, [sys.argv[1]])
    subject1 = cur1.fetchall()
    cur1.execute(q8_1, [sys.argv[2]])
    subject2 = cur1.fetchall()
elif (len(sys.argv) == 4):
    cur1.execute(q8_1, [sys.argv[1]])
    subject1 = cur1.fetchall()
    cur1.execute(q8_1, [sys.argv[2]])
    subject2 = cur1.fetchall()
    cur1.execute(q8_1, [sys.argv[3]])
    subject3 = cur1.fetchall()

def basicScheduler1(subject):
    if (subject is None):
        return None
    s = []
    prev = None
    for record in subject:
        if (record[4] is not prev):
            prev = record[4]
            s.append(record)
    return s

def hourCalc(s):
    total = 0
    for record in s:
        total += record[2]-record[1]
    return total

s1 = basicScheduler1(subject1)
s2 = basicScheduler1(subject2)
s3 = basicScheduler1(subject3)

start = 2400
end = 2400
for day in days:
    day_valid = False
    for record in s1:
        if (record[0] == day):
            day_valid = True

cur1.close()
conn.close()
