def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    current_mnemonic = ['0'] * len(phoneNumber)
    mnemonics_found = []

    phoneNumber_mnemonics_helper(0, phoneNumber, current_mnemonic, mnemonics_found)
    return mnemonics_found


def phoneNumber_mnemonics_helper(idx, phoneNumber, current_mnemonic, mnemonics_found):
    if idx == len(phoneNumber):
        mnemonic = ''.join(current_mnemonic)  # O(n)
        mnemonics_found.append(mnemonic)
    else:
        digit = phoneNumber[idx]
        letters = DIGIT_LETTERS[digit]
        for letter in letters:
            current_mnemonic[idx] = letter
            phoneNumber_mnemonics_helper(idx + 1, phoneNumber, current_mnemonic, mnemonics_found)


DIGIT_LETTERS = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}