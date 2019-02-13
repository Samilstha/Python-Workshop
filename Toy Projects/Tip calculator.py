bill_Amount = float(input("How much is your bill amount?"))
service_quality = int(input("How was the quality of service?"))
num_of_people_served = int(input("How many people did you serve?"))
quality_of_service = (service_quality/100)
tip = (bill_Amount*quality_of_service)/(num_of_people_served)
print("Your tip amount is ",tip)

