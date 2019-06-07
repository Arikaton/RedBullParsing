mas = []
for line in open('balls.txt', 'r'):
    mas.append(line.split())


sort_mas = sorted(mas, key=lambda x: int(x[-1]), reverse=True)

f = open("sorted_balls.txt", 'w')
i = 1
for comand in sort_mas:
    f.write(str(i)+": " + " ".join(comand) + '\n')
    i += 1


