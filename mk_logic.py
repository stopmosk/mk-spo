def assign_people(db, mk_list, max_priority):
    # Список МК сортирован от малопопулярных к популярным?
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
        result.append([mk[0], stu_list])
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
    result.sort(key=lambda res: res[2], reverse=True)
    return result
