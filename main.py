from ortools.algorithms.python import knapsack_solver

import time
import get_testcase
def main():
 
	data = get_testcase.input_data()

	for name in range(0, len(data)):
	
		start = time.time()
		ex_time = 0
		print('Testcase_name: ' + data[name])
		print('Package number: ' + str(name))
		with open(data[name] + ".kp") as level_test:
			rows = level_test.read().split('\n')

		number_items = (int)(rows[1])
    
		capacities = [(int)(rows[2])] # vector with just one entry, the capacity of the knapsack.
		values = [] # vector containing the values of the items.
		weights = [[]] # vector containing the weights of the items.
		for i in range(4, number_items + 5 - 1):
			x = rows[i].split(" ")[0]
			y = rows[i].split(" ")[1]
			values.append((int)(x))
			weights[0].append((int)(y))
			
		solver = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, "KnapsackExample",
    )

		#Set time limit - 3 minutes = 180 seconds
		solver.set_time_limit(180)

		solver.init(values, weights, capacities)
		computed_value = solver.solve() # Solve the problem and get the optimal value.

		packed_items = [] # a list of the optimal packed items.
		packed_weights = [] # the weights of the packed items
		total_weight = 0
		for i in range(len(values)):
			if solver.best_solution_contains(i):
				packed_items.append(i)
				packed_weights.append(weights[0][i])
				total_weight += weights[0][i]

		ex_time = time.time() - start

		print("Capacity = {} \nExecution time: {} \nTotal weight = {} \nTotal value = {} \nNumber of items: {} \nPacked items: {} \nPacked weights: {} \n" \
							.format(capacities[0], ex_time, total_weight, computed_value, len(packed_items), packed_items, packed_weights))

		with open("result/" + "testcase" + str(name) + ".txt", 'w') as solver_file:
			solver_file.write('Testcase name: {}.kp\n' \
							.format(data[name]))

			solver_file.write('Execution time: {} sec\n'.format(ex_time))
			solver_file.write('Capacity = {} \n'.format(str(capacities[0])))
			solver_file.write('Total weight = {} \n'.format(str(total_weight)))
			solver_file.write('Total value = {} \n'.format(computed_value))
			solver_file.write('Number of items: {} \n'.format(str(len(packed_items))))
			solver_file.write('Packed items: {} \n'.format(packed_items))
			solver_file.write('Packed weights: {}'.format(packed_weights))

if __name__ == '__main__':
	main()

 