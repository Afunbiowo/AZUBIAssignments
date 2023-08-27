# A code to calculate the food charge after tax and tip

#food = input('Enter the Food price: ')
#print('Basic amount' + food)


food = 50
print('Amount of food N',food)

#calculations for tip and tax
tip_on_item = food * 0.18
print('tip: N',tip_on_item)
print()
sale_tax = food * 0.07
print('tax: N',sale_tax)
print()
print('See below for grand total')
Grand_total = (food + tip_on_item + sale_tax)
print('N',Grand_total)