def move_element_to_end(array, num_move):
	i = 0
	j = len(array) - 1
	while i < j:
		while i < j and array[j] == num_move:
			j -= 1
		if array[i] == num_move:
			array[i], array[j] = array[j], array[i]
		i += 1
	return array


if __name__ == '__main__':
	"""You're given an array of integers and an integer. Write a function that moves all instances of that integer in 
	the array to the end of the array and returns the array.
	The function should perform this in place (i.e., it should mutate the input array) and doesn't need to maintain 
	the order of the other integers."""
	
	array_sample = [2, 1, 2, 2, 2, 3, 4, 2]
	to_move = 2
	move_element_to_end(array_sample, to_move)
