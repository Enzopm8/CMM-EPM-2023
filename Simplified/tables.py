from tabulate import tabulate

def generate_table(*headers_and_data):
    """
    Generate a table from headers and data.

    Parameters:
    - headers_and_data (list): The first element is the list of headers (the 1st row),
      and the remaining elements are lists of data which represent rows.

    Returns:
    - str: The formatted table.
    """
    try:
        if len(headers_and_data) < 2:
            raise ValueError("At least two elements are required: headers and data.")

        headers = headers_and_data[0]
        data = headers_and_data[1:]

        if len(headers) != len(data[0]):
            raise ValueError("Number of headers must match the number of columns in data.")

        if any(len(row) != len(headers) for row in data):
            raise ValueError("All rows in data must have the same number of columns.")

        table = tabulate(data, headers=headers, tablefmt="grid")
        return table
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage for generate_table function
result_table = generate_table(
    ["Name", "Age", "Occupation"],
    ["John", 25, "Engineer"],
    ["Alice", 22, "Student"],
    ["Bob", 30, "Developer"]
)

print(result_table)

# ------------------------------------------------------------------------------
from tabulate import tabulate
def transpose_array(input_array, header=None):
    """
    Transpose a 2D array.

    Parameters:
    - input_array (list): The 2D array to be transposed.
    - header (list, optional): The header to be added after transposing.

    Returns:
    - list: The transposed array.
    """
    try:
        if not all(isinstance(row, list) for row in input_array) or not input_array:
            raise ValueError("Input must be a non-empty 2D array.")

        if any(len(row) != len(input_array[0]) for row in input_array):
            raise ValueError("All rows must have the same number of elements.")

        transposed_array = [list(row) for row in zip(*input_array)]

        if header is not None:
            transposed_array.insert(0, header)

        return transposed_array
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage for transpose_array function CHANGE
# wil turn rows into columns
original_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#plots the arrays 
transposed_array = transpose_array(original_array, header=["A", "B", "C"])
print("Original Array:")
print(tabulate(original_array, tablefmt="grid"))
print("\nTransposed Array:")
print(tabulate(transposed_array, headers="firstrow", tablefmt="grid"))
