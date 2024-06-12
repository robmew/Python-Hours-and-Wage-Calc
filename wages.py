import datetime
now = datetime.datetime.now()
sun = int(input("Enter Sunday hours: "))
mon = int(input("Enter Monday: "))
tue = int(input("Enter Tuesday: "))
wed = int(input("Enter Wednesday: "))
thu = int(input("Enter Thursday: "))
fri = int(input("Enter Friday: "))
sat = int(input("Enter Saturday: "))
minutes = float(input("Enter minutes total: "))
overspill = minutes / 60
print(overspill)
totalhours = sun + mon + tue + wed + thu + fri + sat + overspill
print(totalhours)
value = totalhours * 14.5
enhancement = float(input("Enter enhancement: "))
total = value + enhancement
print("the amount is: ", total)
if (total <= (961.54)):
    a = ((total - 240) * 0.2)
    pension = ((total - a) + 240) * 0.03
    print(pension)
    b = ((total - 183) * 0.12)
    c = ((total - 494.71) * 0.09)
    d = 72.46
else:
    print("too high for this calculator!")
if (a <= 0):
    a = 0
if (b <= 0):
    b = 0
if (c <= 0):
    c = 0
result = total - a - b - c - d - pension
print(result)
notes = input("enter note for reference: ")
print(str(now), result, notes, file=open('pythonwage.txt', 'a')) 