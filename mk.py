from mk_logic import *
from mk_google_spreadsheets import *


pr = 4   # Длина списка приоритетов

db = google_db_read()
mk_list = [['МК Сиьска', 1],  # Название МК и вместимость в кож.мешках
           ['МК Жопа', 2],
           ['МК Лох', 1],
           ['МК Ублюдок, мать твою', 5],
           ['МК Заебись', 4],
           ['Пустой', 2],
           ['Пустой2', 2]]

sorted_list = sort_mk_list(db, mk_list)   # Отсортировали МК по популярности

print()
print('***************** РАСПРЕДЕЛЕНИЕ ПО МК ***************************')
mk_result, loosers, satisfaction = assign_people_v2(db, mk_list, pr)
for mk in mk_result:
    print(mk[0])
    for name in mk[2]:
        print('\t', name)
    for free_slot in range(mk[1]):
        print('\t ---')

print('*************** ЛЮДИ, ОСТАВШИЕСЯ НЕРАСПРЕДЕЛЁННЫМИ ****************')
for name in loosers:
    print(name)

print('********** УДОВЛЕТВОРЁННОСТЬ РАСПРЕДЕЛЕНИЕМ ************')
print(str(int(satisfaction * 100)) + '%')
