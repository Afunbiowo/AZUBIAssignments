products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

#1 Average price for all products
sum_prices = sum(prices)
print('Sum price:', sum_prices)
average = sum_prices / len(prices)
print('Average', average)
print()

#2 New price list

index = 0
print('The new prices are below')
for new_price in prices:
    index += 1
    new_price = new_price - 5
    print(index,':', new_price)
   #print(index,new_price)
    


#3 Total revenue generated from the product
print()

revenue_list = []

for index in range(0, len(prices)):
       revenue_list.append(prices[index] * last_week[index])     
print('Rev_list:',revenue_list)

print('Total revenue: $', sum(revenue_list))

#4 Average daily revenue for all the products
avrge_rev = sum(revenue_list)/7
print('$',avrge_rev)

#5 Prices less than $30
