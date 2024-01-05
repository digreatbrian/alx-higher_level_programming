import os

tests_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "tests")

test_number = 0

for test_file in sorted(os.listdir(tests_dir)):
	print(f"========= TEST {test_number} ========")
	print(f'FILE: {test_file}')
	print('========================== ')
	with open(os.path.join(tests_dir, test_file), 'r') as fd:
		f = fd.read()
		exec(f)
	print(f"========= END TEST ========\n\n")
	test_number += 1