# Рефлексия:
# 3.1: В первую очередь бросается в глаза то , что можно было сразу при создании файла в цикле присвоить ему текстовое значение в свойствах и создавать кажждый файл одной командой, как это я не сделал. Также вижу, что я не указал, что каждый файл открывается в текстовом виде. И не использовал второй цикл, но три строчки это не страшно. Также мог бы использовать простую эталонную запись уравнения "x = str(random.randint(1,100))", но так как о ней не догадался - наказал себя более долгим и сложным решением.

# 3.2:
# Вижу, что неправильно организовал функцию. Нужно было использовать две функции, а не одну. И не выполнил условия задачи - получить на вход функции три значения - путь и два случайных числа, а использовал их только внутри функции.

# 3.3:
# Вижу интересную запись "s.rstrip().split(" ")" - не знал, что так можно, в таком случае возможно бы смог решить задачу через цикл, а не через условие. Также вижу , как можно было вывести ошибку в конкретной строке(потому что в случае ошибки нужно искать ее самому)


#4.1:
import os


def func1(path_dir, ext, do_include_subdirs):
    files = []
    dirs = []

    item_list = os.listdir(path_dir)

    for item in item_list:
        path_to_item = os.path.join(path_dir, item)
        if os.path.isdir(path_to_item):
            dirs.append(item)
            continue
        if item.endswith(ext):
            files.append(item)

    if not do_include_subdirs:
        return (files, dirs)

    subdirs = []

    for dir in dirs:
        path_to_subdir = os.path.join(path_dir, dir)
        items_in_subdir = os.listdir(path_to_subdir)

        for item in items_in_subdir:
            path_to_item = os.path.join(path_to_subdir, item)
            if os.path.isdir(path_to_item):
                subdirs.append(item)
                continue
            if item.endswith(ext):
                files.append(item)

    dirs.extend(subdirs)

    return (files, dirs)


#4.2:
import os

def clear_catalog(src):
    if not os.path.exists(src):
        return False
            
    item_list = os.listdir(src)

    for item in item_list:
        path_to_item = os.path.join(src, item)

        if os.path.isdir(path_to_item):
            return False

    for item in item_list:
        path_to_item = os.path.join(src, item)
        os.remove(path_to_item)

    os.rmdir(src)
    return True



# 4.3 : Изучил дополнительную информацию, частично успешно использовал в текущем задании.