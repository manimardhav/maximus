import pandas as pd
screen_time = [1,2,3,4]
sd_name =["aa","bb","hi","hello"]
id = [2,3,1,6]
dict1 = {"screen_time":screen_time,"sd_name": sd_name,"id":id}
print(dict1)
df =pd.DataFrame(dict1)
print(df)