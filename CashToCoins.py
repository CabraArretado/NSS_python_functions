dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

# Your magic Python code here

def count(amount): 
    toCount = amount * 100
    piggyBank["quarters"] = int(toCount // 25)
    toCount -= piggyBank["quarters"] * 25

    piggyBank["dimes"] = int(toCount // 10)
    toCount -= piggyBank["dimes"] * 10

    piggyBank["nickels"] = int(toCount // 5)
    toCount -= piggyBank["nickels"] * 5

    piggyBank["pennies"] = int(toCount)


count(dollarAmount)

print(piggyBank)