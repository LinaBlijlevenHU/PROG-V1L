# List lst is a list of prices for a pair of boots at different online retailers
lst = [120.00, 50.00, 150.00, 170.00, 160.00]

# a. You found another retailer selling the boots for $160.00; add this price to list lst
lst.append(160.00)
print(lst)

# b. Compute the number of retailers selling the boots for $160.00
print(lst.count(160.00))

# c. Find the minimum price in lst
min_price = min(lst)
print(min_price)

# d. Using c), find the index of the minimum price in list lst
print(lst.index(min_price))

# e. Using c) remove the minimum price from list lst
lst.remove(min_price)
print(lst)

# f. Sort list lst in increasing order
lst.sort()
print(lst)
