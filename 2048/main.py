def x (mas):
    print('-'*10)
    for y in mas:
        print(*y)
    print('-'*10)


def gnfi (i, j):
    return (i*4+j+1)


def gel (mas):
    empt = []
    for i in range(4):
        if mas [i] == 0:
            num = gnfi(i, j)
            empt.append(num)
    return empt


mas = [[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]

mas[1][2] = 2
mas[3][0] = 4
print(gel (mas))
x(mas)