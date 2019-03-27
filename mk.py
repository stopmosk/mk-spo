from mk_logic import *
from mk_google_spreadsheets import *


pr = 4   # Длина списка приоритетов

db = google_db_read()
mk_list = [['МК Сиьска', 3],  # Название МК и вместимость в кож.мешках
           ['МК Жопа', 3],
           ['МК Лох', 2],
           ['МК Ублюдок, мать твою', 2],
           ['МК Заебись', 4],
           ['Пустой', 2],
           ['Пустой2', 2]]

sorted_list = sort_mk_list(db, mk_list)   # Отсортировали МК по популярности
print()
print('******************* ПОПУЛЯРНОСТЬ МК *************************')
for mk in sorted_list:
    print(mk[0], '-', round(mk[2], 2), 'человек на место')

print()
print('******************* РАСПРЕДЕЛЕНИЕ ПО МК *************************')
mk_result, loosers, satisfaction = assign_people_v2(db, sorted_list, pr)
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
