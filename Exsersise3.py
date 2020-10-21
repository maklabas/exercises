a = [2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for check1 in range(len(a) - 1):
    for check2 in range(check1 + 1, len(a)):
        if a[check1] == a[check2]:
            print("есть одинаковые")
            quit()
print("все уникальны")

