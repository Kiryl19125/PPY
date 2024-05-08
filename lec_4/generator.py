def numner_generator():
    num = 0
    while True:
        yield num
        num += 1


if __name__ == '__main__':
    wywolanie = numner_generator()

    num = next(wywolanie)
    num1 = next(wywolanie)
    num2 = next(wywolanie)


    # num = next(numner_generator())
    # num1 = next(numner_generator())
    # num2 = next(numner_generator())

    print(num, num1, num2)
    # print(next(numner_generator))
    print(next(numner_generator()))
    print(next(numner_generator()))
    print(next(numner_generator()))
    print(next(numner_generator()))
