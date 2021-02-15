# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path
data=pd.read_csv(path)
#Code starts here
data.rename(columns={"Total":"Total_Medals"},inplace=True)
# Data Loading 
data.head(10)

# Summer or Winter
data["Better_Event"]=np.where(data["Total_Summer"]>data["Total_Winter"],"Summer","Winter")
data["Better_Event"]=np.where(data["Total_Summer"]==data["Total_Winter"],"Both",data["Better_Event"])
better_event=data["Better_Event"].value_counts().index.values[0]

# Top 10
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(index=146,inplace=True)
def top_ten(df,col):
    country_list=list(df.nlargest(n=10,columns=col)["Country_Name"])
    return country_list

top_10_summer=top_ten(top_countries,"Total_Summer")
top_10_winter=top_ten(top_countries,"Total_Winter")
top_10=top_ten(top_countries,"Total_Medals")
common=(set(top_10_summer)&set(top_10_winter)&set(top_10))
# Plotting top 10
summer_df=data[data["Country_Name"].isin(top_10_summer)]
winter_df=data[data["Country_Name"].isin(top_10_winter)]
top_df=data[data["Country_Name"].isin(top_10)]
summer_df.plot("Country_Name",'Total_Medals',"bar")
winter_df.plot("Country_Name",'Total_Medals',"bar")
top_df.plot("Country_Name",'Total_Medals',"bar")


# Top Performing Countries
summer_df["Golden_Ratio"]=summer_df["Gold_Summer"]/summer_df["Total_Summer"]
winter_df["Golden_Ratio"]=winter_df["Gold_Summer"]/winter_df["Total_Summer"]
top_df["Golden_Ratio"]=top_df["Gold_Total"]/top_df["Total_Medals"]
summer_max_ratio=max(summer_df["Golden_Ratio"])
summer_country_gold=summer_df[summer_df["Golden_Ratio"]==summer_max_ratio]["Country_Name"].item()
winter_max_ratio=max(winter_df["Golden_Ratio"])
winter_country_gold=winter_df[winter_df["Golden_Ratio"]==winter_max_ratio]["Country_Name"].item()
top_max_ratio=max(top_df["Golden_Ratio"])
top_country_gold=top_df[top_df["Golden_Ratio"]==top_max_ratio]["Country_Name"].item()

# Best in the world 
data_1=data[:-1]
data_1["Total_Points"]=data_1["Gold_Total"]*3 +data_1["Silver_Total"]*2+data_1["Bronze_Total"]*1
most_points=max(data_1["Total_Points"])
best_country=data_1[data_1["Total_Points"]==most_points]["Country_Name"].item()

# Plotting the best
best=data[data["Country_Name"]==best_country][['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)


