def assign_people_v2(db, mk_list, max_priority):
    # Функция распределения людей по МК
    # Внешний цикл - приоритет, внутренний - МК
    result = []
    satisf = 0   # Удовлетворённость распределением
    names = set(db.keys())
    for mk in mk_list:
        result.append([mk[0], mk[1], []])
    for priority in range(max_priority):
        for i, mk in enumerate(mk_list):
            if result[i][1] == 0:   # Если свободных мест в данном МК уже нет
                continue
            for name in db:
                if db[name][priority] == mk[0]:
                    if name not in names:
                        continue
                    result[i][2].append(name)
                    satisf += max_priority - priority
                    names.remove(name)  # Убираем распределённого
                    result[i][1] -= 1   # и уменьшаем кол-во свободных мест
                if result[i][1] == 0:
                    break
    return result, names, satisf / len(db) / max_priority


def sort_mk_list(db, mk_list):
    # Функция сортировочки списка МК по популярности
    # Можно менять направление сортировки и смотреть как это влияет на рез-т
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


def assign_people(db, mk_list, max_priority):
    # Функция распределения людей по МК
    # Внешний цикл - МК, внутренний - приоритет.
    result = []
    satisf = 0   # Удовлетворённость распределением
    for mk in mk_list:
        stu_list = []   # Список людей, которых запишут на данный МК
        free_slots = mk[1]
        for priority in range(max_priority):
            for name in db:
                if db[name][priority] == mk[0]:
                    stu_list.append(name)
                    satisf += max_priority - priority   # Удовлетворённость
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
    return result, satisf / len(db) / max_priority

