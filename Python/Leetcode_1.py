
def romanToInt(s):
#         We have a string as the input
#         Our output is an integer
#         s is in the range of 1 and 3999
#         Input the values into a dictionary
#         loop through string and input values of s into an array
#         loop through array and check whether value of i is lower than the value of i + 1
#         if it is, subtract the value of i + 1 from i and input the result into an array
#         if not, input result into array
#         add up results in results array and output final integer
    
    d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    value_of_s = []
    result = []
    
    for i in s:
        if i in d:
            value_of_s.append(d[i])
    print(value_of_s)
    if len(value_of_s) >= 3:
        result.append(value_of_s[0])
    for j in range(len(value_of_s)):

        if value_of_s[j] < value_of_s[j + 1] & value_of_s[j + 1] != None:
                
            t = value_of_s[j + 1] - value_of_s[j]
            result.append(t)
            
        # elif value_of_s[j] > value_of_s[j-1] & value_of_s[j-1] != None:
        #     continue
        else:
            result.append(value_of_s[j])

      
    print(result)

    sum_of_all_numbers = sum(result)

    return sum_of_all_numbers
    

print(romanToInt('IV'))