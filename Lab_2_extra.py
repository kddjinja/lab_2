import os

end = '\u001b[0m'
color = '\u001b[44m'
# extra task
k = 3
kk = int(input('Введите количество кадров: '))
while kk > 0:
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

    os.system('clear')

    kk -= 1
