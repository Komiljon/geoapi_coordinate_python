import pandas as pd
import csv

csv_file = 'data.csv'
result_file = 'res_data.csv'

#Получаем url  url_list.csv
file_read = pd.read_csv(csv_file, usecols=['Name', 'Phone', 'Email', 'mesto-prozhivaniya'], delimiter=',')
count = file_read.Name.count()
for i in range(count):
    print(file_read['mesto-prozhivaniya'][i])