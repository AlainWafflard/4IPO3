import random
import timeit
import tracemalloc

fn = "some_csv.txt"


# create file with random numbers
def create_file(name, length):
	f = open(name, "w")
	for i in range(length):
		n = random.randint(0, 1000000)
		f.write(str(n) + "\n")
	f.close()


# opening file
# using return
def csv_reader_using_return():
	file = open(fn)
	result = file.read().split("\n")
	return result


# opening file
# using yield
def csv_reader_using_yield():
	for row in open(fn, "r"):
		yield row


def loop_on_csv(fct):
	csv_gen = fct()
	row_count = 0
	for row in csv_gen:
		row_count += 1
	print("Row count is {}".format(row_count))


# MAIN
action = int(input("""
	action ? 
	1 to make file, 
	2 to read file 
"""))


if action == 1:
	create_file(fn, 1000)
	exit()
elif action == 2:
	fct = csv_reader_using_return
	tracemalloc.start()
	execution_time = timeit.timeit(lambda:loop_on_csv(fct), number=1)
	print("Execution time is {}".format(execution_time))
	print("Memory used : {}".format(tracemalloc.get_traced_memory()[1]))
	tracemalloc.stop()

	fct = csv_reader_using_return
	tracemalloc.start()
	execution_time = timeit.timeit(lambda:loop_on_csv(fct), number=1)
	print("Execution time is {}".format(execution_time))
	print("Memory used : {}".format(tracemalloc.get_traced_memory()[1]))
	tracemalloc.stop()

