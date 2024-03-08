def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True
    # Write your logic here
    
    return leap

year = int(input()) # 1990  
print(is_leap(year))


#you can recomended the exemple of the problem

# 1990  # False                 
# 2000  # True
# 2400  # True
