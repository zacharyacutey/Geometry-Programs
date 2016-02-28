import math
solution=None
def law_of_cosines():
	global solution

	#supposed to loop until the user inputs either "1" or "2"
	while True:
		is_user_solving_for_side_or_angle = input("Are you solving for a \n1. Side\n2. Angle\n\nAnswer: ")
		if is_user_solving_for_side_or_angle == "1" or is_user_solving_for_side_or_angle == "2":
			break
		else:
			print("\n\nI don't quite understand what you're trying to tell me.  Could you type that again?\n\n")

	if is_user_solving_for_side_or_angle == "1":
		a = int(input("A: "))
		b = int(input("B: "))
		angle_across_from_a = int(input("Angle Given: "))

		#apply law of cosines (solving for side)
		solution = math.sqrt(a**2+b**2-2*a*b*math.cos(math.radians(angle_across_from_a)))

	elif is_user_solving_for_side_or_angle == "2":
		a = int(input("A: "))
		b = int(input("B: "))
		c = int(input("C: "))

		#apply law of cosines (solving for angle)
		solution = math.degrees(math.acos((a**2-(b**2+c**2))/(-2*b*c)))

	#prints the result of what is being solved for
	print(solution)


law_of_cosines()
