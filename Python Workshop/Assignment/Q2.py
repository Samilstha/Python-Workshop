discount = 40
ship20 = 25
shipAdd = 15

numcopies = 60
coverp = 250
totdiscount =  numcopies * (discount / 100) * coverp
totship = (ship20 * 20) + ( (numcopies - 20) * shipAdd )
wholesale = (coverp * numcopies) - totdiscount + totship

print(f"The total wholesale cost for {numcopies} copies of the book is Rs. {wholesale}.")
