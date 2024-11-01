# файловая_переменная = open(имя_файла, режим_доступа, дополнительные_параметры)

# РЕЖИМЫ ДОСТУПА

# 'r' - read - открыть файл только для чтения. Такой файл не может быть изменен. Если такого файла не будет, то вылезет ошибка
# 'w' - write - открыть файл для записи. Если файл уже существет, то все данные из файла будут удалены. Если файла нету, то он будет создан
# 'a' - append - открыть файл для записи, но данные будут добавлены в конец файла. Если файла нету, то он будет создан
# 'r+' - read+write - открыть для чтения и записи. В этом режиме происходи частичная перезапись содержимого файла
# 'x' - создать новый файл. Если файл существует, то произойдет ошибка

# ДОПОЛНИТЕЛЬНЫЕ ПАРАМЕТРЫ
# encoding - uft-8


# файловые методы
# read() - читает всё содержимое файла. Читает в формате одной строки
# readlines() - читает все содержимое файла, но каждая строка будет являться отдельным элементом списка list

file = open('text.txt', 'r', encoding='utf-8')

res = file.readlines()

# for i in range(len(res)):
#     res[i] = res[i].replace('\n', '')

# print(res)

# for i in file:
#     print(i, end='\n')

# file.close()

# text = 'hello world\n123\nпривет мир\ntext'



# file = open('text.txt', 'r', encoding='utf-8')
#
# res = file.readlines()
# num = 0
# # print(res)

# for i in res:
#     newi = i.replace('\n', '')
#     srtwd = ''
#     for j in newi:
#         if j.isdigit():
#             srtwd += j
#         else:
#             srtwd += ' '
#     # print(srtwd.split())
#     lst = srtwd.split()
#
#     for k in lst:
#         num += int(k)
# print(num)
#
# file.close()


# with open('text.txt', 'r', encoding='utf-8') as file_obj:
#     num = 0
#     for i in file_obj:
#         i = i.replace('\n', '').split()
#         num += int(i[1])
#     print(num)


