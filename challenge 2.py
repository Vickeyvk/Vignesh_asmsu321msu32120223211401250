def isleapyear(year):
    if(year%4== and year%100!=0 or year%400==0):
      return true
    else:
      return false
print("Enter a year")
year=int(input())
if isleapyear(year)
    print(year,"is a leapyear")
    else:
      print(year,"is not a leapyear")