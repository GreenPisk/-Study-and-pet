
def polinom_line(S):
    S1 = S[::-1]
    if S == S1:
        print("Строка является полиномом")
    else:
        print("Строка не является полиномом")

if __name__ == '__main__':
    print("Ведите строку")
    S = input()
    polinom_line(S)

