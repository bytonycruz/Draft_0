f = open ('text.txt','r')
m = f.read()
m = m.replace("\n", " ")
m = m.replace("", "")
print(m)
f.close()



# s = "Hola mundo mundo mundo"
# a = s.replace("mundo", "world")
# print(a)