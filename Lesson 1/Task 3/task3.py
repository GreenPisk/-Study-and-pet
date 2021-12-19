
def unique_simbol(s):
    dictionary = dict()

    for i in range(len(s)):
        if s[i] not in dictionary:
            dictionary[s[i]] = 1
        else:
            dictionary[s[i]] += 1

    k = 0
    for key in dictionary:
        if dictionary[key] == 1:
            k += 1

    return k


if __name__ == '__main__':
    print("Ведите строку")
    s = input()
    print(unique_simbol(s))