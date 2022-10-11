import csv

# flag
red = '\u001b[41m'
blue = '\u001b[44m'
white = '\u001b[107m'
end = '\u001b[0m'

for i in range(6):
    if i <= 1:
        print(red + ' ' * 23 + end)
    elif i <= 3:
        print(white + ' ' * 23 + end)
    else:
        print(blue + ' ' * 23 + end)

print('')

# picture
color = '\u001b[40m'
k = 3
print(color + ' ' * k + end + ' ' * 5 * k + color + ' ' * k + end + ' ' * 5 * k + color + ' ' * k + end)
print(
    ' ' * k + color + ' ' * k + end + ' ' * 3 * k + color + ' ' * k + end + ' ' * k + color + ' ' * k + end + ' ' * 3 * k + color + ' ' * k + end)
print(
    ' ' * 2 * k + color + ' ' * k + end + ' ' * k + color + ' ' * k + end + ' ' * 3 * k + color + ' ' * k + end + ' ' * k + color + ' ' * k + end)
print(' ' * 3 * k + color + ' ' * k + end + ' ' * 5 * k + color + ' ' * k + end)
print(
    ' ' * 2 * k + color + ' ' * k + end + ' ' * k + color + ' ' * k + end + ' ' * 3 * k + color + ' ' * k + end + ' ' * k + color + ' ' * k + end)
print(
    ' ' * k + color + ' ' * k + end + ' ' * 3 * k + color + ' ' * k + end + ' ' * k + color + ' ' * k + end + ' ' * 3 * k + color + ' ' * k + end)
print(color + ' ' * k + end + ' ' * 5 * k + color + ' ' * k + end + ' ' * 5 * k + color + ' ' * k + end)


# function

def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += white + str(plot[i][j])
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += red + '  ' + white
        line += end
        print(line)
    print(white + '0   1 2 3 4  5 6 7 8 9' + end)


array_plot = [[0 for col in range(10)] for row in range(10)]
result = [0 for i in range(10)]
for i in range(10):
    result[i] = i * 2
# print(result)

step = round(abs((result[9] - result[0])) / 9, 1)

array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)

# diagram

k1, k2 = 0, 0
with open('books.csv', encoding='windows-1251') as file:
    table = csv.reader(file, delimiter=';')
    for row in list(table)[1:]:
        if int(row[6][:4]) < 2016:
            k1 += 1
        else:
            k2 += 2

k11 = (k1 // 1000) + 1
k22 = (k2 // 1000) + 1

print('2016+ ' + blue + ' ' * k11 + end + ' ' + str(k1))
print('2015- ' + red + ' ' * k22 + end + ' ' + str(k2))

