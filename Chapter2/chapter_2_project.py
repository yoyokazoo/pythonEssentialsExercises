# You are the captain of a pirate vessel and have a list of crew names and salaries.
# Some of your crew was sloppy during data entry however, so they weren't careful about capitalization.
# They also paid themselves too much.

# 1. Fix their capitalization
# 2. Remove $100 from each of their salaries
# 3. Remove any remaining cents from their salaries
# 4. Print a new salary list

# The final list should look like this:

# Tahngarth - $4900
# Orim - $235
# Ertai - $4460
# Karn - $113
# Mirri - $2034
# Crovax - $2100
# Gerrard capashen - $4200

# I've started you out with the crew_salaries data and a loop to print out the existing data.

# For extra credit, modify your code to get the final name to look like:
# Gerrard Capashen - $4200

crew_salaries = (
	("tahngarth", "5000"),
	("oRim", 335.22),
	("ERTAI", 4560.12),
	("Karn", 213.67),
	("mirri", 2134),
	("CrOvAx", 2200),
	("gerrard capashen", 4300),
)

print()
for crew_member in crew_salaries:
	crew_name = crew_member[0]
	crew_salary = crew_member[1]

	print(crew_name + " - $" + str(crew_salary))