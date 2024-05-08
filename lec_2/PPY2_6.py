# oblicz silnię podanej liczby
num = 6

if __name__ == '__main__':

    result: int = 1
    for i in range(1, num + 1):
        result *= i

    print(result)
