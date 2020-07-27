def CodelandUsernameValidation(str):

    # code goes here
    this_is_true = "true"
    this_is_false = "false"

    dict_b = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
              'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}

    dict_a = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
              'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "_"}
    length_string = len(str)
    if length_string > 25 and length_string < 5:
        return this_is_false
    print(str[-1])
    for char in range(len(str)):
        # print(str[0])
        print(str[char])
        # print(str[-1])
        first_letter = str[0]
        if first_letter not in dict_b:
            print(str[0])
            return this_is_false

        elif str[-1] == '_':
            return this_is_false
        elif str[char] not in dict_a:
            return this_is_false

    return this_is_true

    # return str


# keep this function call here
print(CodelandUsernameValidation("u__hello_world123"))
