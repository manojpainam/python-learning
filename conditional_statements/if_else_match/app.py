#it is used to make the decisions based on the condition evalutions
a = 2
b = 20

if a > b:
    print(a, " is greater than ", b)
#if the if condition is not satisfied then it will check for the elif statement
elif a == b:
    print("a and b are equal")
#even if the elif is not satisfied then it will directly executes the whatever there in the else
else:
    print("a is lesser than b")

#python will treat "" or 0 or False or [] or {} or () or None will be treated as a False value
if not [] or not {} or not ():
    print("A empty list dict tuple")

age = 19
#in shorter form we can write the if else in the below format
print("eligible to vote") if age >= 18 else print("Not enogh age to vote")

#value assignment
bigger = a if a > b else b
print("bigger among the a and b is ", bigger)

'''
logical operators - and or not

and - both the conditions has to be satisfied (True and True = True, True and False = False)
or - can be any of the condition to be True
not - Reverse of the result
'''
x = 10
y = 5
z = 7
if x > y and x > z:
    print("yes x is greater than both the values")

if x > y or x < z:
    print("As i have used 'or' one statement is enough to satisfied")

if not y > z:
    print("Yep y is not greater than z")

is_indian_citizen = True
#combining multiple statements

if is_indian_citizen and age > 18:
    print("You are now okay to proceed for voting")

temprature = 31
is_raning = True
is_weekend = True

if (temprature <= 30 or not is_raning) and is_weekend:
    print("Its a perfect day for vacation")
else:
    print("Can't plan this day")

#if statement can't be empty but for some reasons if we need to keep it empty then use pass statement to avoid getting error
if not False:
    pass


#instead of having multiple if else statements we can have a match statements
day = 5
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Tursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Not a valid choice")

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Its a weekday")
    case 6 | 7:
        print("weekend")
    case _:
        print("Not a valid choice")
    