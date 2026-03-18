from datetime import date, datetime, timedelta


def get_birthday_for_year(birthday: date, year: int) -> date:
    try:
        return birthday.replace(year=year)
    except ValueError:
        return birthday.replace(year=year, day=28)


def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    today = datetime.today().date()
    upcoming: list[dict[str, str]] = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = get_birthday_for_year(birthday, today.year)

        if birthday_this_year < today:
            birthday_this_year = get_birthday_for_year(
                birthday, today.year + 1
            )

        days_until = (birthday_this_year - today).days

        if 0 <= days_until <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime(
                        "%Y.%m.%d"
                    ),
                }
            )

    return upcoming


def main() -> None:
    users: list[dict[str, str]] = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Bob Dylan", "birthday": "2000.02.29"},
    ]
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)


if __name__ == "__main__":
    main()
