def validatePasswordPolicy1(mi, ma, char, password):
	sorted_pass = sorted(password)
	i = 0
	found = 0
	while i < len(sorted_pass):
		if sorted_pass[i] == char:
			found += 1
		i += 1

	if found in range(mi, ma+1):
		return True
	else:
		return False
def validatePasswordPolicy2(indx1, indx2, char, password):
	found1 = False
	found2 = False
	indx1 -= 1
	indx2 -= 1
	if indx1 in range(0, len(password)) and password[indx1] == char:
		found1 = True
	if indx2 in range(0, len(password)) and password[indx2] == char:
		found2 = True

	return found1 != found2
def readPasswords(f_name):
	valid_count1 = 0
	valid_count2 = 0
	with open(f_name) as f_in:
		for line in f_in:
			line = line.strip()
			line = line.split(" ")
			limits = line[0].split("-")
			min_lim = int(limits[0])
			max_lim = int(limits[1])
			char = line[1][0]
			password = line[2]
			is_valid1 = validatePasswordPolicy1(min_lim, max_lim, char, password)
			is_valid2 = validatePasswordPolicy2(min_lim, max_lim, char, password)
			if is_valid1:
				valid_count1 += 1
			if is_valid2:
				valid_count2 += 1



	return valid_count1, valid_count2

if __name__ == '__main__':
	valid_count1, valid_count2 = readPasswords("AoC_day_2_2020_input.txt")
	print("Part 1:")
	print("I counted %d valid passwords with Policy 1" % (valid_count1))
	print("Part 2:")
	print("I counted %d valid passwords with Policy 2" % (valid_count2))
