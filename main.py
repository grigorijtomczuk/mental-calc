from operator import add, sub, mul, truediv
from random import randint, choice
from time import time


class Problem():
	
	def __init__(self, operator: str, x: int, y: int):
		self.operator = operator
		self.x = x
		self.y = y
		operator_map = {
			"+": add,
			"-": sub,
			"*": mul,
			"/": truediv,  # float solution will be casted to int (temporarily)
		}
		self.solution = int(operator_map[self.operator](x, y))
	
	def __str__(self):
		return f"\n{self.x} {self.operator} {self.y}"


def generate_random_problem() -> Problem:
	operator = choice(["+", "-", "*", "/"])
	x = randint(1, 100)
	y = randint(1, 100)
	return Problem(operator, x, y)


def main():
	print("Welcome to Mental Math Calculations!")

	while True:
		try:
			problem_amount = int(input("How many problems do you want to solve?: "))
			break
		except ValueError:
			print("\nPlease, enter a valid number.")
	
	correct_answer_cnt = 0
	start_time_seconds = time()
	
	for _ in range(problem_amount):
		problem = generate_random_problem()
		print(problem)

		while True:
			try:
				user_attempt = int(input("Answer: "))
				break
			except ValueError:
				print("\nPlease, enter a valid number.")
		
		if user_attempt == problem.solution:
			print("Solved successfully!")
			correct_answer_cnt += 1
		else:
			print("Wrong answer.")
	
	end_time_seconds = time()
	result_time_seconds = end_time_seconds - start_time_seconds
	completeness_percentage = (correct_answer_cnt / problem_amount) * 100

	print(f"\nSolved correctly {correct_answer_cnt} out of {problem_amount} ({completeness_percentage:.1f}%) in {result_time_seconds:.1f}s.")


if __name__ == "__main__":
	main()
