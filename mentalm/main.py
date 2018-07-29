import argparse
from math_test import *

parser = argparse.ArgumentParser("mentalm", description="Mental math tester", 
	epilog="Created by Daniel J. Perry (BioBox)")
parser.add_argument('-cfg', default="default.ini", 
	help="ini file for your settings. the defualt is default.ini")

args = parser.parse_args()

class CLIMathTest(MathTest):
	"""A MathTest implementation in the terminal"""
	def __init__(self, config_file):
		super(CLIMathTest, self).__init__(config_file)		

	def display_question(self, i):
		print("\nQuestion #{}: {} = ".format(i+1, self.questions[i]), end='')

	def get_input(self):
		user_input = input()
		if user_input.capitalize() == 'Q':
			self.quit = True
			return user_input

		try:
			return int(user_input)
		except ValueError:
			print("Please input a number: ", end='')
			return self.get_input()

	def end_test(self):
		ans = self.answers
		wrong_ans = [i+1 for i,ans in enumerate(ans) if self.u_answers[i] != ans]
		len_wrong = len(wrong_ans)

		print()
		if self.quit:
			print("TEST ABORTED.\n")

		if len_wrong == 0:
			if not self.quit:
				print("You got a perfect score. Congratulations!")
		elif len_wrong == 1:
			print("You got number ", wrong_ans[0], " wrong.")
		else:
			print("You got {} wrong. They are numbers ".format(len_wrong), end='')
			print(*wrong_ans[:len_wrong-1], sep=', ', end='')
			print(', and ', wrong_ans[len_wrong-1])


math_test = CLIMathTest(args.cfg)

print("This test is {} questions long.".format(math_test.numq))
print("Press ENTER to start the test...", end='')
input()
math_test.start()
