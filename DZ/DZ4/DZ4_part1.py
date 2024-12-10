import json
purchases = {}

f = open("C:\\Users\\N1k\\python\\DZ\\DZ4\\purchase_log.txt", 'r',encoding='utf-8')

line = ""
for line in f:
    record = json.loads(line)
    user_id = record.get('user_id')
    category = record.get('category')
    if user_id and category:
            purchases[user_id] = category
#purchases = f.readlines()


print(purchases)


f.close()