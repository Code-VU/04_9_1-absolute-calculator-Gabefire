def calculateAbsolute():
    
    # This first line is provided for you
    try:
        in_num = input("Enter a number: ")
        in_num = int(in_num)
    except:
        print("bad number")

    if in_num < 21:
        in_num = 21 - in_num
        print("Result:", in_num)
    elif in_num > 21:
        in_num = 2 * (in_num - 21)
        print("Result:", in_num)
    else:
        print("Result:", '0')
   
    
    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
