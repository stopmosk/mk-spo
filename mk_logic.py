def assign_people(db, mk_list, max_priority):
    # Функция распределения людей по МК
    # Внешний цикл - МК, внутренний - приоритет.
    result = []
    for mk in mk_list:
        stu_list = []   # Список людей, которых запишут на данный МК
        free_slots = mk[1]
        for priority in range(max_priority):
            for name in db:
                if db[name][priority] == mk[0]:
                    stu_list.append(name)
                    db[name] = list(' ' * max_priority)
                    # Я негодяй и меняю аргументы функции. Знаю, плохо
                    free_slots -= 1
                if free_slots == 0:
                    break
            if free_slots == 0:
                break
        # Теперь забьём оставшиеся пустые места МК прочерками
        for f_slot in range(free_slots, 0, -1):
            stu_list.append('---')
        result.append([mk[0], free_slots, stu_list])
    return result


def assign_people_v2(db, mk_list, max_priority):
    # Функция распределения людей по МК.
    # Внешний цикл - приоритет, внутренний - МК

    result = []
    for mk in mk_list:
        result.append([mk[0], mk[1], []])
    print(result)

    for priority in range(max_priority):
        print(priority)
        print(mk_list)
        for i, mk in enumerate(mk_list):
            print('\t', i, mk[0], result[i][1])
            if result[i][1] == 0:   # Если свободных мест в данном МК уже нет
                continue
            for name in db:
                if db[name][priority] == mk[0]:
                    result[i][2].append(name)
                    db[name] = list(' ' * max_priority)
                    print('\t\t\t', name)
                    # Я негодяй и меняю аргументы функции. Знаю, плохо
                    result[i][1] -= 1   # Уменьшить кол-во свободных мест
                if result[i][1] == 0:
                    break

        # Теперь забьём оставшиеся пустые места МК прочерками
        '''for f_slot in range(free_slots, 0, -1):
            stu_list.append('---')'''

    return result


def sort_mk_list(db, mk_list):
    result = []
    for mk in mk_list:
        cnt = 0
        for name in db:
            for p, sel in enumerate(db[name]):
                if sel == mk[0]:
                    cnt += 1
        result.append([mk[0], mk[1], cnt / mk[1]])
    # result.sort(key=lambda res: res[2])
    result.sort(key=lambda res: res[2], reverse=True)
    return result
