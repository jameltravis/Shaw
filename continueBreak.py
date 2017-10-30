shoppingList = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shoppingList:
    if item == "spam":
        continue
        # 'continue' bypasses or a certain part of the code
        # you can also use 'break' to exit out of the for loop altogether
    print("Buy " + item)

meal = ["eggs", "bacon", "sausages", "spam"]
nastyFood = ''

for item in meal:
    if item == 'spam':
        nastyFood = item
        break
else:
    print("I'll have a plate of that, then, please.")

