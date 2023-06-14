from yandex_geocoder import Client
import pandas as pd
import csv

csv_file = 'data.csv'
result_file = 'res_data.csv'

with open(result_file, "w", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(
        (
            'Широта',
            'Долгота',
            'Описание',
            'Подпись',
            'Номер метки'
        )
    )

client = Client("0fe362d6-8111-4d8d-af09-3e67f2f2b80c")
file_read = pd.read_csv(csv_file, usecols=['Name', 'Phone', 'Email', 'mesto-prozhivaniya'], delimiter=',')
count = file_read.Name.count()
j = 0
for i in range(count):
    j = i + 1
    adress = 'Россия, ' + str(file_read['mesto-prozhivaniya'][i])
    try:
        coordinates = client.coordinates(adress)
        if coordinates[1] is not None:
            with open(result_file, "a", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(
                    (
                        coordinates[1],
                        coordinates[0],
                        str(file_read['Name'][i]) + ', ' + str(file_read['Phone'][i]) + ', ' + str(file_read['Email'][i]) + ', ' + str(file_read['mesto-prozhivaniya'][i]),
                        file_read['Name'][i],
                        j
                    )
                )

    except():
        print('error')

print('Done')