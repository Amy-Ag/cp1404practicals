from guitar import Guitar

YEAR= 2022
guitar1=Guitar("Gibson L-5 CES", 1922, 16035.40)
guitar2=Guitar("Another Guitar",2013, 1000)

print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age(YEAR)}")
print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age(YEAR)}")

# Test is_vintage()
print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage(YEAR)}")
print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage(YEAR)}")