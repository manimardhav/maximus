lit = [1,2,3,4,5,6]
iterate_var = iter(lit)
print(iterate_var)
type(iterate_var)
for i in iterate_var:
    if i % 2 == 0:
        print(i)