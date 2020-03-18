import cs3311

conn = cs3311.connect()

cur1 = conn.cursor()

# TODO

q6_1 = """
    SELECT id, weeks
    FROM meetings
"""

q6_2 = """
    UPDATE meetings
    SET weeks_binary = %(word)s
    WHERE id = %(id)s
"""

cur1.execute(q6_1)

for record in cur1.fetchall():
    binary = list("00000000000")

    valid = True
    for i in record[1]:
        if (i == "N" or i == "<"):
            valid = False

    if (valid):
        weeks = record[1].split(',')
        for i in weeks:
            if (len(i) < 3):
                binary[int(i)-1] = "1"
            else:
                period = i.split('-')
                for j in range(int(period[0]),int(period[1])+1):
                    binary[int(j)-1] = "1"
    word = "".join(binary)
    cur1.execute(q6_2, {'word': str(word),'id': record[0]})
    conn.commit()

cur1.close()
conn.close()
