# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    gender = input('Please enter your gender (M or F): ')
    birthday = input('Enter your birthdate (YYYY-MM-DD): ')
    weight = float(input('Enter your weight in U.S. pounds: '))
    height = float(input('Enter your height in U.S. inches: '))
    age_in_years = compute_age(birthday)

    weight_in_kg = kg_from_lb(weight)
    height_in_cm = cm_from_in(height)

    BMI = body_mass_index(weight_in_kg, height_in_cm)
    BMR = basal_metabolic_rate(gender, weight_in_kg, height_in_cm, age_in_years)

    print(f'Age (years): {age_in_years}')
    print(f'Weight (kg): {weight_in_kg}')
    print(f'Height (cm): {height_in_cm}')
    print(f'Body mass index: {BMI}')
    print(f'Basal metabolic rate (kcal/day): {BMR}')

    
    
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    kg = pounds / 0.45359237
    return kg


def cm_from_in(inches):
    cm = inches / 2.54
    return cm


def body_mass_index(weight, height):
    BMI = ( 10000 * weight) / ( height ** 2 )
    return BMI


def basal_metabolic_rate(gender, weight, height, age):
    if(gender == 'M'):   
        BMR = 88362 + ( 13397 * weight ) + ( 4799 * height ) - ( 5677 * age ) 
    else:
        BMR = 447593 + ( 9.247 * weight ) + ( 3098 * height ) - ( 4330 * age )

    return BMR

main()
# Call the main function so that
# this program will start executing.
