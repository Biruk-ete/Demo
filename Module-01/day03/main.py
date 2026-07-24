transaction_log = {}

try:
    with open ("transactions.txt") as t:
        for line in  t:
            name, amount = line.strip().split(",")
            transaction_log[name] = int(amount)

    print(transaction_log)
except:
    print('No transactions.txt file - starting empty')

sorted_transaction = sorted(transaction_log.items(), key=lambda item: item[1], reverse=True)
for name, amount in sorted_transaction:
    print(name, amount)

with open("report.txt", "w")as r:
    for name, amount in sorted_transaction:
         r.write(f"{name},{amount}\n")