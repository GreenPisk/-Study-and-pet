# Входные данные


def home_list(n,t,teleport):
    num = [int(i) for i in teleport if i.isdigit()]

    S = 0
    for i in range(len(num)):
        if t != S:
            S = S + num[i]
            if i+1 == (len(num)):
                print("No")
        elif t == S:
            print("Yes")
            break

if __name__ == '__main__':
    n,t = map(int,input().strip().split(" "))
    teleport = input()
    home_list(n,t,teleport)
