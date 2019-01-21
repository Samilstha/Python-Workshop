 Suppose the cover price of a book is Rs. 240, but bookstores get a 40% discount. Shipping costs
Rs. 25 for the first 20 copies and Rs. 15 for each additional copy. What is the total wholesale cost for
60 copies?
Solution:

discount = 40
ship20 = 25
shipAdd = 15

numcopies = 60
coverp = 250
totdiscount =  numcopies * (discount / 100) * coverp
totship = (ship20 * 20) + ( (numcopies - 20) * shipAdd )
wholesale = (coverp * numcopies) - totdiscount + totship

print(f"The total wholesale cost for {numcopies} copies of the book is Rs. {wholesale}.")
