def percentage_plus(total_bill,percent_tip):
    return (total_bill) * (1 + (percent_tip/100))

def tip_calculator():
    total_bill = int(input('What is the total bill?: '))
    percent_tip = int(input('What percentage would you like to tip?: '))
    return total_bill, percent_tip

total_bill, percent_tip = tip_calculator()
total = percentage_plus(total_bill,percent_tip)

print(f'Total bill is ${round(total,2)}')