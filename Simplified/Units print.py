def edit_text_with_units(text, units, default_unit=""):
    """
    Edit a text string by appending engineering units.

    Parameters:
    - text (str): The original text.
    - units (dict): A dictionary mapping variable names to their units.
    - default_unit (str, optional): Default unit to use if a variable has no specified unit.

    Returns:
    - str: The modified text with appended units.
    """
    try:
        edited_text = text
        for variable, unit in units.items():
            placeholder = f"{{{variable}}}"
            formatted_unit = f" {unit}" if unit else f" {default_unit}"
            edited_text = edited_text.replace(placeholder, f"{placeholder}{formatted_unit}")

        return edited_text
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
original_text = "The temperature is {temp} and the speed is {speed}."
engineering_units = {"temp": "°C", "speed": "rads"}

edited_text = edit_text_with_units(original_text, engineering_units, default_unit="units")
print(edited_text)
