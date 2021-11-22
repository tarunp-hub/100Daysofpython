total_amount=int(input('what was the total bill? '))
tip=int(input('What percentage tip would you like to give? '))
no_of_people=int(input('How many peeople to split the bill?'))
bill_after_tip=(total_amount*(100+tip))/100
amount_per_persion=round((bill_after_tip/no_of_people),2)
print(f'Each persion should pay: ${amount_per_persion}')
