#!/usr/bin/env python3
import datetime
from pprint import pprint
import sys


def make_cleaning_list(start_week):
    year = datetime.datetime.now().year
    rooms = [i for i in range(36, 49)]
    weeks = [i for i in range(start_week, start_week + 13)]
    room_weeks = zip(rooms, weeks)
    res = []

    for room, week in room_weeks:
        monday = datetime.datetime.strptime(
            f"{year}-W{int(week)-1}-1", "%Y-W%W-%w"
        ).date()
        friday = monday + datetime.timedelta(days=4)
        sunday = monday + datetime.timedelta(days=6)

        format_friday = f"{friday.day:02}/{friday.month:02}"
        format_sunday = f"{sunday.day:02}/{sunday.month:02}"

        a = f" - Week {week} - {format_friday}-{format_sunday} - Room {room}\n"
        res.append(a)
    return res


def write_to_file(formatted_date):
    with open("cleaning_schedule.txt", "w") as f:
        f.writelines(formatted_date)


if __name__ == "__main__":
    start_week = sys.argv[1]
    start_week = int(start_week)
    cleaning = make_cleaning_list(start_week)
    write_to_file(cleaning)
