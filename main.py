def to_alternating_caps(input_string):
    """
    Args:
        input_string (str): The string to convert.
    
    Returns:
        str: The string with alternating capitalization.
    """
    result = []
    capitalize = True  
    
    for char in input_string:
        if char.isalpha():
            if capitalize:
                result.append(char.upper())
            else:
                result.append(char.lower())
            capitalize = not capitalize  
        else:
            result.append(char) 
    
    return ''.join(result)

# Test cases
print(to_alternating_caps("hello world! 123"))  
print(to_alternating_caps("Testing alternating CAPS!"))  
print(to_alternating_caps("12345!@#$%")) 