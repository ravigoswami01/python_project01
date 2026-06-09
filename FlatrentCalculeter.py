# total  flat rent 
# what amount of total food 
# what amout charege of electric bill par unite
# total bill amount 
# total persion in room 

rent = int(input("Enter your total room rent Amount="))
food = int(input("Enter your total food Amount = "))
electri_parUnite_charge= int(input("Enter electric bill charge par Uinte = "))
electric_unite_total = int(input("Enter total bill in Unite = "))
persion =int(input("total persion in the room/Flat = "))

total_bill_amount = electric_unite_total * electri_parUnite_charge

# output for user 

output = (rent + food +total_bill_amount) // persion

print("Each person pay will = ",output)