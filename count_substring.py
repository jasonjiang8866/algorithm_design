#Count Substring
#an algorithm that counts the number of substrings that begin with character 'A' and ends with character 'X'. For example, given the input string "CAXAAYXZA", there are four substrings that begin with 'A'
#and ends with 'X', namely: "AX", "AXAAYX", "AAYX", and "AYX".
def count_substring(string):
    countA=0
    substrNo=0
    for element in string:
        if element=='A': countA+=1
        if element=='X': substrNo+=countA
    return substrNo
