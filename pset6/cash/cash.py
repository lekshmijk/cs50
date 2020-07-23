from cs50 import get_float

while True:
    change = get_float("Change owed (in dollars):")
    if change > 0:
        break
    
coins = 0
cents = round(change * 100)
    
while (cents > 0):
    
    if cents >= 25:
        cents -= 25
        coins += 1
        
    elif cents >= 10:
        cents -= 10
        coins += 1
        
    elif cents >= 5:
        cents -= 5
        coins += 1
        
    else:
        cents -= 1
        coins += 1
        
        
print(f"The minimum number of coins:{coins}")
    

