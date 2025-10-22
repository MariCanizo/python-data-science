import pandas as pd

file_path = 'online_retail.csv'
sales_data = pd.read_csv(file_path)
print(sales_data.head())

import numpy as np

data = np.array([[1,2,3], [4,5,6], [7,8,9]])

dt_from_array = pd.DataFrame(data, columns=['A','B', 'c'])
print(dt_from_array)

data = [[1,'Jhon', 22], [2,'Anna', 24]]

df_from_list = pd.DataFrame(data, columns = ['ID', 'Name', 'Age'])
print(df_from_list)

data = [{'ID': 1,
         'Name': 'Jhon',
         'Age' : 22}]
dt_from_dict_list = pd.DataFrame(data)
print(dt_from_dict_list )

data = {'ID': [1,2,3], 'Name': ['Jhon', 'Anna', 'Mike'], 'Age': [22,24,21]}

df_from_dict = pd.DataFrame(data)
print(df_from_dict)

data = {'ID': pd.Series([1,2,3]),
        'Name': pd.Series(['Jhon', 'Anna', 'Mike']),
        'Age': pd.Series([22,24,21])}

df_from_series_dict = pd.DataFrame(data)
print(df_from_series_dict)

#from google.colab import drive
#drive.mount('/content/drive')
#file_path = "/content/drive/My Drive/online_retail.csv"
#sales_data = pd.read_csv(file_path)
#print(sales_data.head())
#from google.colab import drive
#drive.mount('/content/drive')