# napisz kod, który wyświetli ciąg fibonnaciego do 10 miejsc (https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego)
# pierwsze dwie liczby w ciągu
num1, num2 = 0, 1
print("Ciąg Fibonacciego:")

if __name__ == '__main__':
    for i in range(10):
        print(num1, end=' ')
        num2 += num1
        num1 = num2 - num1
