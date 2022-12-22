from random import randint, choice
from time import perf_counter


def generateProblem() -> dict:
	ops = {"+": lambda x, y: x + y, "-": lambda x, y: x - y}
	op_key: str = choice(list(ops))
	op: function = ops[op_key]
	x = randint(1, 100)
	y = randint(1, 100)
	answer = op(x, y)
	problem = {"x": x, "y": y, "op_key": op_key, "answer": answer}
	return problem


def isProblemSolved() -> bool:
	problem = generateProblem()
	op_key = problem["op_key"]
	x = problem["x"]
	y = problem["y"]
	answer = problem["answer"]
	while True:
		try:
			user_try = int(input(f"{x} {op_key} {y} = "))
			break
		except ValueError:
			print("Please, enter a valid number. Try again.")
	if answer == user_try:
		return True
	else:
		return False


def getSummary(results: dict) -> None:
	correctAnswerCnt = results["corr_cnt"]
	difficulty = results["diff"]
	timeStart = results["t_start"]
	timeEnd = results["t_end"]
	completePercentage = (correctAnswerCnt / difficulty) * 100
	print(f"Solved correctly {correctAnswerCnt} out of {difficulty} ({completePercentage:0.1f}%) in {timeEnd - timeStart:0.1f}s.")
	if completePercentage >= 80:
		print("Keep it up!")
	else:
		print("Consider trying once more!")


def main():
	print("Welcome to Mental Math Calculations!")
	while True:
		try:
			difficulty = int(input("How many problems do you want to solve? ... "))
			break
		except ValueError:
			print("Please, enter a valid number. Try again.")
	correctAnswerCnt = 0
	timeStart = perf_counter()
	for _ in range(difficulty):
		if isProblemSolved():
			correctAnswerCnt += 1
			print("Solved successfully!")
		else:
			print("Wrong answer.")
	timeEnd = perf_counter()
	results = {"corr_cnt": correctAnswerCnt, "diff": difficulty, "t_start": timeStart, "t_end": timeEnd}
	getSummary(results)


if __name__ == "__main__":
	main()
