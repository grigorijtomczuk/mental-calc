from random import randint
from time import perf_counter


def isGeneratedProblemSolved():
	n1 = randint(1, 100)
	n2 = randint(1, 100)
	answer = n1 + n2
	while True:
		try:
			userTry = int(input(f"{n1} + {n2} = "))
			break
		except ValueError:
			print("Please, enter a valid number. Try again.")
	if answer == userTry:
		return True
	else:
		return False


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
		if isGeneratedProblemSolved():
			correctAnswerCnt += 1
			print("Solved successfully!")
		else:
			print("Wrong answer.")
	timeEnd = perf_counter()
	completePercentage = (correctAnswerCnt / difficulty) * 100
	print(f"Solved correctly {correctAnswerCnt} out of {difficulty} ({completePercentage:0.1f}%) in {timeEnd - timeStart:0.1f}s.")
	if completePercentage >= 80:
		print("Keep it up!")
	else:
		print("Consider trying once more!")


if __name__ == "__main__":
	main()
