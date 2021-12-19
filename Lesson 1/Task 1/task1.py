
def simbol_line(S):
    print("Количество символов")
    print(len(S) - S.count(" "))

if __name__ == '__main__':
    print("Ведите строку")
    S = input()
    simbol_line(S)
