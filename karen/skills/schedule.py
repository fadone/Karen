from os.path import basename
from datetime import datetime

import pandas as pd

name = basename(__file__[:-3])
command = [
    [name, "show_schedule", ["show my schedule", "show me my schedule"]],
    [name, "whats_on_schedule", ["whats on my schedule", "what i am doing right now"]],
]

enable = True

def show_schedule(text):
    time_now = datetime.now()
    # time_now = datetime(2021, 7, 29, 13, 0)

    schedule_file = "schedule.xlsx"
    df = pd.read_excel(schedule_file, dtype={'Name': str, 'From': str, 'To': str, 'Duration': str})
    column_names = df.columns.values
    values = df.values.tolist()
    max_len = 0
    for v in values:
        name = v[0]
        name_len = len(name)
        if max_len < name_len:
            max_len = name_len
    m_str = ""
    count = 0
    for v in values:
        name = v[0]
        # from_time = datetime.strptime(v[1], "%H:%M:%S").strftime("%I:%M %p")
        from_time = datetime.strptime(v[1], "%H:%M:%S")
        to_time = datetime.strptime(v[2], "%H:%M:%S").strftime("%I:%M %p")
        # duration = datetime.strptime(v[3], "%H:%M:%S").strftime("%H:%M")
        if time_now.time() < from_time.time():
            m_str += "{n:<{max}} {f:<7} - {t:<7}\n".format(n=name, f=from_time.strftime("%I:%M %p"), t=to_time, max=max_len)
            count += 1
        if count == 3:
            break
    if count == 0:
        return "Nothing on your day schedule. Sleeping time!"
    return m_str


def whats_on_schedule(text):
    time_now = datetime.now()
    # time_now = datetime(2021, 7, 29, 11, 0)

    schedule_file = "schedule.xlsx"
    df = pd.read_excel(schedule_file, dtype={'Name': str, 'From': str, 'To': str, 'Duration': str})
    column_names = df.columns.values
    values = df.values.tolist()
    max_len = 0
    for v in values:
        n = v[0]
        name_len = len(n)
        if max_len < name_len:
            max_len = name_len
    for v in values:
        n = v[0]
        # from_time = datetime.strptime(v[1], "%H:%M:%S").strftime("%I:%M %p")
        from_time = datetime.strptime(v[1], "%H:%M:%S")
        to_time = datetime.strptime(v[2], "%H:%M:%S")
        # duration = datetime.strptime(v[3], "%H:%M:%S").strftime("%H:%M")
        if from_time.time() < time_now.time() < to_time.time():
            m_str = "{} from {} to {}".format(n, from_time.strftime("%I:%M %p"), to_time.strftime("%I:%M %p"))
            # m_str = "{n:<{max}} {f:<7} - {t:<7}\n".format(n=name, f=from_time.strftime("%I:%M %p"), t=to_time.strftime("%I:%M %p"), max=max_len)
            return m_str
    return "Its your rest time!"
