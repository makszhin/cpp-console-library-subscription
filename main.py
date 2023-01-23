


def read_all_lines():
    """
    Функция для разбивки всех данных файла на списки, состоящие из отдельных данных строки
    """
    with open("primer.txt", "r", encoding="UTF-8") as op:
        lines = []
        for line in op.readlines():
            current_line = [line[0:10], line[11:19], line[20:26], int(line[27:43])]
            index = line[44::].index(" ")
            current_line.append(float(line[44:44+index]))
            current_line.append(line[45+index:-1])
            lines.append(current_line)
    return lines


lines = read_all_lines()


def first_exe(lines: list):
    """
    Функция для вывода построчно данных из файла
    """
    for line in lines:
        print(f'''Вывод изначальных данных
        {line[0]} {line[1]} {line[2]} {line[3]} {line[4]} {line[5]}
        ''')


def second_exe():
    """
    Вывод данных за ноябрь 2021
    """
    for line in lines:
        if "11.2021" in line[0]:
            print(f'''Данные за ноябрь 2021
            {line[0]} {line[1]} {line[2]} {line[3]} {line[4]} {line[5]}
            ''')


def sel_sort(array):
    """
    Функция сортировки данных по назначению в порядке убывания
    """
    lenght = len(array)
    copied_array = array.copy()
    for i in range(lenght - 1):
        m = i
        j = i + 1
        while j < lenght:
            if ord(copied_array[j][5][0]) < ord(copied_array[m][5][0]):
                m = j
            j = j + 1
        copied_array[i], copied_array[m] = copied_array[m], copied_array[i]
    print(f'''Данные сортировки
    {copied_array}
    ''')
    return copied_array





if __name__ == "__main__":
    first_exe(lines)
    second_exe()
    sel_sort(lines)
