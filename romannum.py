def solution(roman):
   
    acc = 0 # accumlator of the values of the roman characters 
    
    char_roman = [*str(roman)] # breaks down the string into alist of chars 
    
    roman_numerals = {# the dictonary of th values of the roma numbers 
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    for i in range(len(char_roman)+1):
        acc += roman_numerals(char_roman[i])
        
    print(acc)
    
    return 1

solution("MCMLXXXIX")