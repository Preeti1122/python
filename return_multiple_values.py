
#######  Return multiple values #############

def raise_to_power(value1, value2):
    """Raise value1 to the power of value2."""
    new_value = value1 ** value2
    new_value1 = value1 + value2
    return new_value,new_value1
result = raise_to_power(2, 3)
print(result) 



'''def raise_both(value1, value2):
    """Raise value1 to the power of value2
 and vice versa."""
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    new_tuple = (new_value1, new_value2)
    return new_tuple
#Returning multiple values
result = raise_both(2, 3)
print(result) '''
