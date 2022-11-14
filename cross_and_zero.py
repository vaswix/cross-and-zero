massive = {'0-0': '-', '1-0': '-', '2-0': '-',
           '0-1': '-', '1-1': '-', '2-1': '-',
           '0-2': '-', '1-2': '-', '2-2': '-'}


n = 0
while n < 10:
    print(
        f'  0 1 2\n0 {massive["0-0"]} {massive["1-0"]} {massive["2-0"]}\n1 {massive["0-1"]} {massive["1-1"]} {massive["2-1"]}\n2 {massive["0-2"]} {massive["1-2"]} {massive["2-2"]}'
    )
    num = input('введите число (к примеру 0-0, 0-1, 2-0, 0-1, 1-1, 2-1, 0-2, 1-2, 2-2): ')
    if num in massive:
        if n % 2 == 0:
            massive[num] = '0'
            n += 1
        else:
            massive[num] = 'X'
            n += 1
    else:
        pass