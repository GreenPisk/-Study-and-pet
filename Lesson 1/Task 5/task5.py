
def queue_list(n,t,s):
    i = 1
    s = s + 'EE' #костыль
    while i <= t:
        print(i)
        i = i + 1
        j = 0
        while j <= n:
            if s[j] == 'B' and s[j+1] == 'G':
                s = s[:j] + s[int(j + 1):]
                s = s[:j] + 'G' + s[int(j+1):]
                s = s[:j + 1] + s[j + 1:]
                s = s[:j+1] + 'B' + s[j + 1:]
                j = j + 2
            else:
                j = j + 1
    s = s[:n]
    print(s)

if __name__ == '__main__':
    n,t = map(int,input().strip().split(" "))
    s = input()
    queue_list(n,t,s)