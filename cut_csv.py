
import pandas as pd
import random

## Указываем полный путь к файлу "C:\Users\xxxxx\flights.csv"
split_source_file = input("Введите полный путь к файлу. Пример: C:\Users\xxxxx\ваш файл.csv" : ")

## При помощи Pandas определяем количество строк в файле
pd_dataframe = pd.read_csv(split_source_file, header=0)
number_of_rows = len(pd_dataframe.index) + 1


print(f"{number_of_rows}")

## Если нужно разделить файл на одинаковые количества строк, указываем один и тот же диапазон минимальной длины и максимальной
print('Если нужно порезать файл на одинаковые количества строк, указываем один и тот же диапазон минимальной длины и максимальной')
min_rows = int(input("Минимальное количество строк в разделенном файле : "))
max_rows = int(input("Максимально количество строк в разделенном файле : "))

file_increment = 1
skip_rows = 1

## Первый файл определяем рандомом
number_of_rows_perfile = random.randint(min_rows, max_rows)

while True:

    if number_of_rows_perfile <= 0:
        break
    df = pd.read_csv(split_source_file, header=None, nrows = number_of_rows_perfile,skiprows = skip_rows)

    ## Указываем имя файла
    split_target_file = f"{split_source_file[:-4]}_{file_increment}.csv"

    ## Записываем в csv
    df.to_csv(split_target_file, index=False, header=False, mode='a', chunksize=number_of_rows_perfile)

    file_increment += 1

    skip_rows += number_of_rows_perfile

    ## Последняя обработка файлов
    if skip_rows >= number_of_rows:
        number_of_rows_perfile = number_of_rows - skip_rows
    else:
        number_of_rows_perfile = random.randint(min_rows, max_rows)