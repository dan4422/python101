def percentage_plus(total_bill,percent_tip):
    return (total_bill) * (1 + (percent_tip/100))

def group_tip_calculator():
    total_bill = int(input('What is the total bill?: '))
    percent_tip = int(input('What percentage would you like to tip?: '))
    people = int(input('How many people are in your group?: '))
    return total_bill, percent_tip, people

total_bill, percent_tip, people = group_tip_calculator()
the_total_bill = percentage_plus(total_bill, percent_tip)
cost_per_person = percentage_plus(total_bill, percent_tip)/people

print(f'''Total bill is ${the_total_bill}
Cost per person is ${round(cost_per_person,2)}''')

