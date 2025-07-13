

#1 Temperature
def median_temperature(temps):
    """
    Median  temperature calculation. (None) value will be dropped
    (parameter temps) full numbers and <None> value
    (return) Median temperature as (float) type.
    """
    cleaned = [t for t in temps if t is not None]
    return sum(cleaned) / len(cleaned)

temperature_input = input("Task 1. Enter temperature values, if no value type <None>:")
temperatures = [int(x) if x != "None" else None for x in temperature_input.split()]
mdt = median_temperature(temperatures)
print(f"Medianne temperature:{mdt:.2f}")


#2 Positive and Negative numbers
def posneg_numbers(*args):
    """
    Split numbers by positive and negative (Ascending) values (Descending)
    (parameter args) Unlimited amount in numbers
    (return) tulp pf 2 lists: negative and positive values.
    """
    negative = sorted([x for x in args if x < 0], reverse=True)
    positive = sorted([x for x in args if x >= 0])
    return negative, positive

datainput = input(f"\nTask 2. Enter numbers wit space separator: ")
numbers = list(map(float, datainput.split()))
neg, pos = posneg_numbers(*numbers)
print(f"Task 2. Negative numbers, descending:: {neg}")
print(f"Task 2. Positive numbers, ascending: {pos}")


#3 Number exponent
def exponent(base, exponent):
    """
    Raise number to the power of exponent.
    (parameter base) Inptuting number is  (float) or (int)
    (parameter exponent) power of as (int)
    """
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    return result if exponent >= 0 else 1 / result

def exponent_recursive(base, exponent):
    """
    Everything  is equal twith straight exponent
    """
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * exponent_recursive(base, exponent - 1)
    else:
        return 1 / exponent_recursive(base, -exponent)

a1 = float(input("\nTask 3. Enter number: "))
a2 = int(input("Task 3. Enter needed power of a number (not FLOAT!): "))
print(f"Task 3. Straight power: {exponent(a1, a2) :.2f}")
print(f"Task 3. Recursive power: {exponent_recursive(a1, a2) :.2f}")
