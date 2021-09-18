def replace_double_single_quotes(input_string: str) -> str:
    def replace_char(ch: str)-> str:
        if ch =='"':
            return "'"
        if ch =="'":
            return '"'
        return ch
    return ''.join(list(map(replace_char, [char for char in input_string])))



def is_palindrome(input_string:str)-> bool:
    return True if input_string == input_string[::-1] else False

