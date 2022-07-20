def parse_raw(raw):
    with open('raw.txt', 'r',  encoding="utf8") as fd:
        lines = fd.readlines()
        for line in lines:
            parts = line.split(' ')
            if len(parts) == 2:
                raw[parts[0]] = int(parts[1])
            else:
                raw[parts[0]] = raw[parts[1]]*int(parts[2])


def calculate_profit(raw, profit):
    with open('price.txt', 'r',  encoding="utf8") as fd:
        lines = fd.readlines()
        for line in lines:
            parts = line.strip().split(' ')
            if len(parts) == 1:
                continue
            name = parts[0]
            price = int(parts[1])
            cost = 0
            for i in range(2,len(parts)):
                if (len(parts[i].split('*')) == 1):
                    cost += raw[parts[i].strip()]
                else:
                    item_name = parts[i].split('*')[0]
                    item_unit = int(parts[i].split('*')[1])
                    cost += raw[item_name] * item_unit
                profit[name] = price - cost


raw = {}
menu = []
peifangs = {}
price = []
profit = {}

parse_raw(raw)
calculate_profit(raw, profit)
print(profit)