def multi(number):
    print('Некрасивая таблица умножения:')
    multi_arr = ''
    count = 1
    for i in range(number):
        for n in range(10):
            if i+1 == count:
                multi_arr += (f'{i + 1} * {n + 1} = {(i+1) * (n+1)}, ')
            else:
                multi_arr += f'\n{i + 1} * {n + 1} = {(i+1) * (n+1)}, '
                count += 1

    return multi_arr

print(multi(5))


def beauty_multi(number):
    print('Красивая таблица умножения:')
    multi = ''
    for i in range(10):
        if i+1 > 1:
            multi += '\n|  '
        else:
            multi += '|  '
        for n in range(number):
            if i + 1 < 10:
                if (n+1)*(i+1) < 10:
                    multi += f'{n+1} * {i+1} = {(n+1)*(i+1)}   |  '
                elif (n+1)*(i+1) < 100:
                    multi += f'{n + 1} * {i + 1} = {(n + 1) * (i + 1)}  |  '
                else:
                    multi += f'{n + 1} * {i + 1} = {(n + 1) * (i + 1)} |  '
            else:
                if (n+1)*(i+1) < 100:
                    multi += f'{n + 1} * {i + 1} = {(n+1)*(i+1)} |  '
                else:
                    multi += f'{n + 1} * {i + 1} = {(n + 1) * (i + 1)}|  '
    return multi

print(beauty_multi(20))
