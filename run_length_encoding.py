def run_length_encoding(string):
    # Write your code here.
    # char_list = []
    # char_list_two = []
    # for i in range(len(string)):
    # 	if string[i] == string[i + 1]:
    # 		char_list.add(string[i])
    # 		if len(char_list >= 9):
    # 			for j in range(len(i, string)):
    # 				if string[j] == string[j + 1]:
    # 					char_list_two.add(string[j])
    # 				else:
    # 					return

    encoded_string_char = []
    current_length = 1

    for i in range(1, len(string)):
        current_char = string[i]
        previous_char = string[i - 1]

        if current_char != previous_char or current_length == 9:
            encoded_string_char.append(str(current_length))
            encoded_string_char.append(previous_char)
            current_length = 0

        current_length += 1

    encoded_string_char.append(str(current_length))
    encoded_string_char.append(string[len(string) - 1])

    # Testing purposes
    print("".join(encoded_string_char))

    return "".join(encoded_string_char)


if __name__ == '__main__':
    string = "AAAAAAAAAAAAABBCCCCDD"

    run_length_encoding(string)
