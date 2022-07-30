age = input("what is your current age:\n")
age_as_int = int(age)
years_remaining = 90-age_as_int
days_remaining = 365*years_remaining
weeks_remaining = 52*years_remaining
months_remaining = 12*years_remaining
print(f"You have {days_remaining} days, {weeks_remaining} weeks,{months_remaining} months left!")