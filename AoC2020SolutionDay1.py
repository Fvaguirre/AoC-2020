
map_int_sums_2020 = dict()

def find2Sumto2020(f_name):
	with open(f_name) as f_in:
		for line in f_in:
			num = int(line.strip())
			complement = 2020 - num
			if num not in map_int_sums_2020:
				map_int_sums_2020[num] = 1
			else:
				map_int_sums_2020[num] += 1

			if complement in map_int_sums_2020:
				if complement == num and map_int_sums_2020[num] > 1:
					return num, num
				else:
					return num, complement
def find3Sumto2020():
	map_num_to_occurrence = dict()
	for key1, val1 in map_int_sums_2020.items():
		complement1 = 2020 - key1
		for key2, val2 in map_int_sums_2020.items():
			complement2 = complement1 - key2

			if complement2 in map_int_sums_2020:
				map_num_to_occurrence[complement2] = map_num_to_occurrence.get(complement2, 0) + 1
				map_num_to_occurrence[key1] = map_num_to_occurrence.get(key1, 0) + 1
				map_num_to_occurrence[key2] = map_num_to_occurrence.get(key2, 0) + 1

				for num, occur in map_num_to_occurrence.items():
					if occur > 1 and map_int_sums_2020[num] != occur:
						map_num_to_occurrence.clear()
						break
					else:
						return key1, key2, complement2

if __name__ == '__main__':
	print("Part1 Solution:")
	num1, num2 = find2Sumto2020("AoC_day_1_2020_input.txt")
	print("%d and %d sum to 2020, their product is %d" % (num1, num2, num1 * num2))
	print("Part2 Solution:")
	num1, num2, num3 = find3Sumto2020()
	print("%d and %d and %d sum to 2020, their product is %d" % (num1, num2, num3, num1 * num2 * num3))
	print("Part2 Solution:")
