# Nested loops -> a general concept of having one loop within another loop
# Doesn't matter if it's a for or while loop

rows = input("How many rows: ")
columns = input("How many columns: ")
symbol = input("Choose a symbol: ")

rows = int(rows)
columns = int(columns)

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()