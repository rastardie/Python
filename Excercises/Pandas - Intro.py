import pandas as pd

#Create a dictionary
XYZ_web = {'Day':[1,2,3,4,5,6], 'Visistos':[1000,700,6000,1000,400,350], 'Bounce_Rate':[20,20,23,15,10,34]}

#Convert the dictionary into Pandas dataframe
df = pd.DataFrame(XYZ_web)

print(df)