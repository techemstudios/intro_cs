"""
Example exercise on python lists:
how they're structured and what you can do with them.
"""

foods = ['apple']
foods.append('orange')
foods.extend(('yams','bannanas','tomatoes','TOES'))
#foods = [apples,orange,yams,bannanas,tomatoes]
print(foods[1])
if'apple' in foods:
	print("TRUE")
for food in foods:
	print food.title()
	

print(foods)
