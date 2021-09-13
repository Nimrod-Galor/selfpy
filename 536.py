def filter_teens(a=13, b=13, c=13):
    ages_sum = fix_age(a) + fix_age(b) + fix_age(c)
    return ages_sum



def fix_age(age):
    if age >= 13 and age <= 19 and age != 15 and age != 16:
       return 0
    return age




print(filter_teens())
print(filter_teens(1, 2, 3))
print(filter_teens(2, 13, 1))
print(filter_teens(2, 1, 15))