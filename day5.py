import pandas as pd
screen_time = [1,2,3,4]
sd_name =["aa","bb","hi","hello"]
id = [2,3,1,6]
dict1 = {"screen_time":screen_time,"sd_name": sd_name,"id":id}
print(dict1)
df =pd.DataFrame(dict1)
print(df)


# list comprehension
list = [1,2,3,4,5]
res = [i+1 for i in list]
print(res)

#for even no in list
list = [1,2,3,4,5]
res = [i for i in list if i%2 == 0]
print(res)

#dictionary comprehension
dict = {"a":12, "b":24, "c":36}
res = {value:key for key,value in dict.items()}
print(res)

#tuple comprehension
import math
num1 = [1, 2, 3, 4, 5]
res = tuple(math.sqrt(i) for i in num1 )
print(res)

ts = [
    {"name": "Laptop", "price": 800},
    {"name": "table", "price": 500},
    {"name": "TV", "price": 300},
]
res = {i["name"]: i["price"] for i in ts if i["price"] <= 500}
print(res)