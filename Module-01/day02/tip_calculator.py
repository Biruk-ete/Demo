bill_total = 4500
friends = ['Biruk', 'Henok', 'Nati', 'Bella', 'Saron']
number_of_people = len(friends)

def split_bill(total, people, tip_rate= 0.10):
    total += total * tip_rate
    per_person_amount = total / people
    return per_person_amount

for name in friends:
    print(f'{name}: {split_bill(bill_total, number_of_people)}')

