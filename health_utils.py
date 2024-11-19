def calculate_bmi(height: float, weight: float) -> float:
    """
    Calculate Body Mass Index (BMI)
    Args:
        height: Height in meters
        weight: Weight in kilograms
    Returns:
        float: BMI value
    """
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive numbers")
    return round(weight / (height ** 2), 2)

def calculate_bmr(height: float, weight: float, age: int, gender: str) -> float:
    """
    Calculate Basal Metabolic Rate (BMR) using Harris-Benedict equation
    Args:
        height: Height in centimeters
        weight: Weight in kilograms
        age: Age in years
        gender: 'male' or 'female'
    Returns:
        float: BMR value
    """
    if height <= 0 or weight <= 0 or age <= 0:
        raise ValueError("Height, weight and age must be positive numbers")
    
    gender = gender.lower()
    if gender not in ['male', 'female']:
        raise ValueError("Gender must be either 'male' or 'female'")

    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:  # female
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    return round(bmr, 2)
