import argparse


def get_bmi(weight: float, height: float) -> float:

    if weight <= 0:
        raise ValueError("Weight cannot be zero or negative")
    if height <= 0:
        raise ValueError("Height cannot be zero or negative")

    if weight > 1000:
        raise ValueError("Weight cannot be greater than 1000 pounds")
    if height > 1000:
        raise ValueError("Height cannot be greater than 1000 inches")

    weight_in_kg = weight * 0.453592
    height_in_meters = height * 0.0254
    squared_height = height_in_meters**2
    bmi = weight_in_kg / squared_height
    return bmi


def get_category(bmi: float) -> str:
    if bmi >= 30:
        return "Obese"
    elif bmi >= 25:
        return "Overweight"
    elif bmi >= 18.5:
        return "Normal"
    else:
        return "Underweight"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate BMI")
    parser.add_argument("weight", type=float, help="Weight in pounds")
    parser.add_argument("height", type=float, help="Height in inches")
    args = parser.parse_args()

    bmi = get_bmi(args.weight, args.height)
    category = get_category(bmi)

    print(f"BMI: {bmi:.2f}, Category: {category}")
