def year(n):
    if(n>0):
        if(n%4==0):
            print("the given year is a leap year")
        else:
            print("the given year is not a leap year")
#main
n= int(input("ENTER A YEAR:"))
year(n)
                
