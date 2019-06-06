mas = []
for line in open('balls.txt', 'r'):
    mas.append(line.split())


def key_func(x):
    try:
        x = int(x)
    except:
        x = 0
    return x


sort_mas = sorted(mas, key=lambda x: key_func(x[-1]), reverse=True)

f = open("sorted_balls.txt", 'w')
i = 1
for comand in sort_mas:
    f.write(str(i)+": " + " ".join(comand) + '\n')
    i += 1


