from mk_logic import *
from mk_google_spreadsheets import *


pr = 4   # Длина списка приоритетов

db = google_db_read()
mk_list = [['МК Сиьска', 3],  # Название и вместимость МК
           ['МК Жопа', 2],
           ['МК Лох', 1],
           ['МК Ублюдок, мать твою', 2],
           ['МК Заебись', 2],
           ['Пустой', 2],
           ['Пустой2', 2]]

sorted_list = sort_mk_list(db, mk_list)   # Отсортировали МК по популярности

print('***************** РАСПРЕДЕЛЕНИЕ ПО МК ***************************')
mk_result = assign_people(db, sorted_list, pr)
for mk in mk_result:
    print(mk[0])
    for name in mk[1]:
        print('\t', name)

print('*************** ЛЮДИ, ОСТАВШИЕСЯ НЕРАСПРЕДЕЛЁННЫМИ ****************')
for name in db:
    if db[name].count(' ') == 0:
        print(name)
