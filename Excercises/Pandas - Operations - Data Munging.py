import pandas as pd

country = pd.read_csv('C:\\Users\\Kay\\Desktop\\Temp\PROGRAMMING WORKS\\PYTHON\\Test.csv', index_col=0)

#Convert csv to html
country.to_html('edu.html')