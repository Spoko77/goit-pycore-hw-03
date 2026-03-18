from datetime import datetime


def get_days_from_today(date: str) -> int:
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        difference = today - target_date
        return difference.days
    except ValueError as error:
        raise ValueError(
            f"Невірний формат дати: '{date}'. Очікується 'РРРР-ММ-ДД'"
        ) from error


def main() -> None:
    print(get_days_from_today("2020-10-09"))


if __name__ == "__main__":
    main()
