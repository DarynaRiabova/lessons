from datetime import datetime

KEY = "TSTFEED0300|7E3E|0400"

with open("lesson_19/hblog.txt", "r") as file:
    filtered_log = []

    for line in file:
        if KEY in line:
            filtered_log.append(line)

with open("hb_test.log", "w") as log:
    for i in range(len(filtered_log) - 1):
        time1 = filtered_log[i].split("Timestamp ")[1][:8]
        time2 = filtered_log[i + 1].split("Timestamp ")[1][:8]

        t1 = datetime.strptime(time1, "%H:%M:%S")
        t2 = datetime.strptime(time2, "%H:%M:%S")

        diff = abs((t2 - t1).total_seconds())

        if 31 < diff < 33:
            log.write(f"WARNING {time1} heartbeat = {diff}\n")
        elif diff >= 33:
            log.write(f"ERROR {time1} heartbeat = {diff}\n")
