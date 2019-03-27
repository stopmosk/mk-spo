from mk_logic import *
from mk_google_spreadsheets import *


pr = 4   # Длина списка приоритетов

db = google_db_read()
mk_list = [['МК Сиьска', 1],  # Название и вместимость МК
           ['МК Жопа', 2],
           ['МК Лох', 2],
           ['МК Ублюдок, мать твою', 4],
           ['МК Заебись', 3],
           ['Пустой', 2],
           ['Пустой2', 2]]

sorted_list = sort_mk_list(db, mk_list)   # Отсортировали МК по популярности

print('***************** РАСПРЕДЕЛЕНИЕ ПО МК ***************************')
mk_result, satisfaction = assign_people_v2(db, mk_list, pr)
for mk in mk_result:
    print(mk[0])
    for name in mk[2]:
        print('\t', name)

print('*************** ЛЮДИ, ОСТАВШИЕСЯ НЕРАСПРЕДЕЛЁННЫМИ ****************')
for name in db:
    if db[name].count(' ') == 0:
        print(name)

print('Процент удовлетворённости распределением: ' +
      str(int(satisfaction * 100)) + '%')
