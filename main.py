x=open("Victor.txt", "w")
x.write("My teacher is Martin")
x.close()

b=open("Victor.txt", "r")
print(b.read())
b.close()

t=open("Victor.txt", "a")
t.write(" and his friend is dennis")