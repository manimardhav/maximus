lit = [1,2,3,4,5,6]
iterate_var = iter(lit)
print(iterate_var)
type(iterate_var)
for i in iterate_var:
    if i % 2 == 0:
        print(i)

import pandas as pd
screen_time = [1,2,5,6]
stu_name = ["aa","bb","cc","dd"]
id= [1,2,3,4]
dict1 = {"screen_time":screen_time,"stu_name":stu_name,"id":id}
print(dict1)
df =pd.DataFrame(dict1)
print(df) 
df.head(5)