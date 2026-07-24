customers = [
    ("Almaz", 1500), ("Dawit", 700), ("Tigist", 200),
    ("Hanna", 1200), ("Samuel", 450), ("Biruk", 550)
]

def tier(balance):
    if balance >= 1000:
        return "Premium"
    elif balance >= 500:
        return "Standard"
    return "Basic"

for name, balance in customers:
    print(f"{name}: {tier(balance)} ({balance} ETB)")

print('\n')
premium = 0
standard = 0
basic = 0

for name, balance in customers:
    customer_tier = tier(balance)

    if customer_tier == "Premium":
        premium += 1
    elif customer_tier == "Standard":
        standard += 1
    else:
        basic += 1

print(f"Premium: {premium}")
print(f"Standard: {standard}")
print(f"Basic: {basic}")