from datetime import datetime, timedelta

# list of users
day_of_birth = [
    {"name": "Bob", "birthday": "2002-06-22"},
    {"name": "Kira", "birthday": "1981-06-21"},
    {"name": "Jack", "birthday": "1997-06-19"},
    {"name": "Jerry", "birthday": "1976-06-18"},
    {"name": "Tom", "birthday": "1976-06-20"},
    {"name": "Bayraktar", "birthday": "2001-06-24"},
    {"name": "Kirill", "birthday": "1985-06-27"},
    {"name": "Juliia", "birthday": "1999-07-02"},
    {"name": "Olga", "birthday": "1989-06-26"},
    {"name": "Andrii", "birthday": "1987-06-12"}
]
# days name
days_name = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def get_birthdays(users: list) -> str:
    # find of start and end period
    birth_in_year = {}
    # start_period = ((datetime(year=2022, month=6, day=7)
    start_period = ((datetime.now() - timedelta(days=datetime.now().weekday()) + timedelta(days=5))).date()
    end_period = start_period + timedelta(days=6)

    for info in users:
        birth = info.get("birthday")
        name = info.get("name")

        # date conversion list-->date
        birthday = datetime.strptime(birth, "%Y-%m-%d").date()
        year_now_date = birthday.replace(start_period.year)

        if start_period <= year_now_date <= end_period:
            day_of_week = days_name.get(year_now_date.weekday())  # get day of week now
            if year_now_date.weekday() in (5, 6):  # add list of birthdays in weekend
                if birth_in_year.get("Monday"):  # create Monday list
                    birth_in_year["Monday"].append(name)
                else:
                    birth_in_year["Monday"] = [name]
            else:
                if birth_in_year.get(day_of_week):  # create other days list
                    birth_in_year[day_of_week].append(name)
                else:
                    birth_in_year[day_of_week] = [name]
    birthdays = ""

    # output list of results
    for day_of_week, name in birth_in_year.items():
        birthdays += f'{day_of_week}: {", ".join(name)} \n'

    return birthdays


if __name__ == "__main__":
    print(get_birthdays(day_of_birth))
