import cs3311
import sys

conn = cs3311.connect()
cur1 = conn.cursor()

# TODO

q7 = """
    SELECT r.id, 
            m.class_id, 
            t.name AS term, 
            m.day, 
            m.start_time AS start, 
            m.end_time AS end, 
            m.weeks_binary AS weeks
    FROM meetings m
    INNER JOIN classes cl ON m.class_id = cl.id
    INNER JOIN courses co ON cl.course_id = co.id
    INNER JOIN terms t ON co.term_id = t.id
    INNER JOIN rooms r ON m.room_id = r.id
    WHERE SUBSTRING(r.code, 1, 1) = 'K' AND t.name = %s
    ORDER BY r.id ASC
    ;
"""

total_query = """
    SELECT COUNT(DISTINCT r.id)
    FROM rooms r
    WHERE SUBSTRING(r.code, 1, 1) = 'K'
    ;
"""

cur1.execute(total_query)
total_rooms = cur1.fetchone()[0]
underused = 0

if (len(sys.argv) == 1):
    cur1.execute(q7, ["19T1"])
else:
    cur1.execute(q7, [sys.argv[1]])

rooms_dict = {}
for record in cur1.fetchall():
    weeks = record[6][:-1]
    weeknum = weeks.count('1')
    # print(record[6],weeknum)
    total = (record[5]-record[4])*weeknum

    if (record[0] in rooms_dict.keys()):
        rooms_dict.get(record[0]).append(total)
    else:
        rooms_dict[record[0]] = [total]
    
for i, j in rooms_dict.items():
    if (sum(j)/10 < 2000):
        underused+=1

underused += (total_rooms - len(rooms_dict))
print("underused is:", underused)
underused_percent = ((underused/total_rooms)*100)
print(str(round(underused_percent, 1))+"%")


cur1.close()
conn.close()
