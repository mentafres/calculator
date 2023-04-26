bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80
income = 0
net_income = 0

# our income
print('Earned amount:')
print('Bubblegum: $', bubblegum)
print('Toffee: $', toffee)
print('Ice cream: $', ice_cream)
print('Milk chocolate: $', milk_chocolate)
print('Doughnut: $', doughnut)
print('Pancake: $', pancake)

income = bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake

print('Income: $', income)

# our expenses
staff_expenses = float(input('Staff expenses:'))
other_expenses = float(input('Other expenses:'))

net_income = income - staff_expenses - other_expenses

print('Net income: $', net_income)
