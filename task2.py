import random


def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list[int]:
    if (
        not isinstance(min_num, int)
        or not isinstance(max_num, int)
        or not isinstance(quantity, int)
    ):
        return []

    if min_num < 1 or max_num > 1000 or quantity < 1:
        return []

    if min_num > max_num or quantity > (max_num - min_num + 1):
        return []

    return sorted(random.sample(range(min_num, max_num + 1), quantity))


def main() -> None:
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)

    lottery_numbers = get_numbers_ticket(1, 36, 5)
    print("Ваші лотерейні числа:", lottery_numbers)

    print(get_numbers_ticket(1, 49, 50))
    print(get_numbers_ticket(0, 49, 6))
    print(get_numbers_ticket(1, 1001, 6))


if __name__ == "__main__":
    main()
