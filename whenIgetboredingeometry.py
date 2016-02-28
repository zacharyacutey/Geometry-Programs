import math
import cmath
solution=None

def distance():
	#user input
	x1 = int(input("1st X:  "))
	x2 = int(input ("\n2nd X:  "))
	y1 = int(input("\n1st Y:  "))
	y2 = int(input ("\n2nd Y:  "))

	#calculate and store the distance in 'calculate_distance'
	calculate_distance = str(math.sqrt((x1-x2)**2 + (y1 - y2)**2))

	print("\n\nThe distance is: {0}".format(calculate_distance))


def law_of_cosines():
	global solution

	#supposed to loop until the user inputs either "1" or "2"
	#has a bug though
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


def quadform():
	#user input
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))

	# calculate the discriminant
	d = (b**2) - (4*a*c)

	# find two solutions
	first_solution = (-b-cmath.sqrt(d))/(2*a)
	second_solution = (-b+cmath.sqrt(d))/(2*a)

	print("The solution are {0} and {1}".format(first_solution, second_solution))


while True:
	which_formula = int(input("Which formula would you like to use?\n\n1. Distance Formula\n2. Quadratic formula\n3. Law of Cosines\n\n"))

	if which_formula == 1 or which_formula==2 or which_formula==3:
		break
	else:
		print("\n\nI don't quite understand what you're trying to tell me.  Could you type that again?\n\n")
print("\n")
if which_formula == 1:
	distance()
elif which_formula == 2:
	quadform()
elif which_formula == 3:
	law_of_cosines()
