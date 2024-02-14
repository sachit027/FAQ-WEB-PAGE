n=int(input("no."))
distinct_coun=set()
for _ in range(n):
    c=input("name")
    distinct_coun.add(c)
    dis=len(distinct_coun)
print(dis)
