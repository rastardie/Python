import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

df = pd.DataFrame({"Day":[1,2,3,4], "Visitors":[200,100,230,300], "Bounce_Rate":[20,45,60,10]})
print(df)
print("---------------------------------------")

df.set_index("Day", inplace=True)     #Set "Day" as the index value
print(df)
print("---------------------------------------")

#Changle a column heading
df = df.rename(columns={"Visitors":"Users"})
print(df)
print("---------------------------------------")

#Plot a graph
df.plot()
plt.show()