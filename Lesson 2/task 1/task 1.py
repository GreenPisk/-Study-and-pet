# https://codeforces.com/problemset/problem/939/A
# Задача не решена, сохранил на будущее

def triangle_line():
    print("Ведите число самолетов")
    number_air = input()
    print("Ведите зависимость")
    Like_air = '1' + input()
    Like_air = Like_air.replace(' ', '')
    graph = {}
    for i in range(int(number_air)):
        # {Cамолет,['тот который нравится','тот которому нравится']}
        graph[str(i+1)] = [Like_air[i+1], Like_air[int((Like_air[i+1]))]]
        print(graph)
        print(graph.get(str(i+1)))
        print(graph.get(graph.get(str(i+1))[1]))
        #if str(1 + i) == graph.get(Like_air[i+1][2]):
           # break




if __name__ == '__main__':
    triangle_line()
