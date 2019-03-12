def budget():
    salary = float(input("Please input your salary: "))
    monthly_income = round(salary/12, 2)
    print("Your monthly income is:", monthly_income)
    print()

    housing = round(monthly_income * .25, 2)
    transport = round(monthly_income * .15, 2)
    food = round(monthly_income * .12, 2)
    savings = round(monthly_income * .10, 2)
    utilities = round(monthly_income * .10, 2)
    charity = round(monthly_income * .05, 2)
    entertainment = round(monthly_income * .05, 2)
    medical = round(monthly_income * .05, 2)
    gift = round(monthly_income * .05, 2)

    print("Housing:", housing)
    print("Transportation:", transport)
    print("Food:", food)
    print("Savings:", savings)
    print("Utilities:", utilities)
    print("Charity:", charity)
    print("Entertainment:", entertainment)
    print("Medical", medical)
    print("Holidays/Gifts:", gift)
    print()

    total = round(housing + transport + food + savings + utilities + charity + entertainment + medical + gift, 2)

    print("Total spent:", total)

budget()
