# 3A.
# napisz program, który policzy ile jest cyfr w liczbie, przy pomocy funckji len()


# 3B.
# napisz program, który policzy ile jest cyfr w tej samej liczbie innym sposobem
# pomyśl o szybkości obliczeń

if __name__ == '__main__':
    # 3A.

    number: str = input("Podaj liczbe: ")
    print(f"Liczba zawiera {len(number.strip("-"))} cyfr")


    #3B.

    number: int = int(input("Podaj liczbe: "))
    count: int = 0
    while number != 0:
        number //= 10
        count += 1

    print(f"Liczba zawiera {count} cyfr")
