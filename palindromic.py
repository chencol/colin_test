from math import floor


def is_palindromic(text):
    text_length = len(text)
    first_half = ""
    second_half = ""
    if text_length % 2 == 0:
        first_half = text[0:int(text_length/2)]
        second_half = text[int(text_length/2):]
    else:
        if text_length == 1:
            return True
        else:
            mid_point = floor(text_length/2)
            first_half = text[0:mid_point]
            second_half = text[mid_point+1:]
    for i in range(len(first_half)):
        if not first_half[i] == second_half[-(i+1)]:
            return False
    return True


def get_palindromic_by_length(text, length):
    start = 0
    palindromic_text = None
    while not palindromic_text:
        if start + length <= len(text):
            substring = text[start:start+length]
            if is_palindromic(substring):
                return substring
            else:
                start = start + 1
        else:
            break
    return None


def get_palindromic(text):
    proceed = True
    text_length = len(text)
    current_length = text_length
    palindromic_text = ""
    while proceed and current_length >= 1:
        palindromic_text = get_palindromic_by_length(text, current_length)
        if palindromic_text:
            proceed = False
        else:
            current_length = current_length-1
    return palindromic_text


text1 = "abcdcfda553fafdasfadfa7888886888887yyy"
text2 = "abcdcfda553f7888886888887afdasfadfayyy"
text3 = "abcdcfda553fafdasfadfayyy88888888888888888888888888888888"
text4 = "abbbbafasf12r2r1r23235566112e3223131414141interesting;gnitseretni"
text5 = "abcdcfda553f288888827afdasfadfayyy"
text6 = "abcdcfdXCLLLLLLLCXa553f288888827afdasfadfayyyabcdcfda553fafdasfadfayyy"


result1 = get_palindromic(text1)
result2 = get_palindromic(text2)
result3 = get_palindromic(text3)
result4 = get_palindromic(text4)
result5 = get_palindromic(text5)
result6 = get_palindromic(text6)


assert result1 == "7888886888887", "result1 should be '7888886888887'"
assert result2 == "7888886888887", "result2 should be '7888886888887'"
assert result3 == "88888888888888888888888888888888", "result3 should be '88888888888888888888888888888888'"
assert result4 == "interesting;gnitseretni", "result4 should be 'interesting;gnitseretni'"
assert result5 == "28888882", "result5 should be '28888882'"
assert result6 == "XCLLLLLLLCX", "result6 should be 'XCLLLLLLLCX'"
