data = open("nosql.db", "w")
for i in range(10):
    data.write(f"key{i}: value{i}, ")
data.close()

