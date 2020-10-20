import numpy as np

# Just change the function to whatever you need to find the root of
def fx(x):
   return x**6 - x**4 - x**3 - 1

def regula_falsi_method(a, b, accuracy):
    i = 0
    x = []
    while True:
        print("ITERATION " + str(i+1))
        print("a = " + str(a) + " , b = ", str(b))
        x.append(((a*fx(b)) - (b*fx(a)))/(fx(b) - fx(a)))
        xval = 'x' + str(i) + '='
        print()
        print(xval, end='')
        print(x[i])
        print()
        fx_val = fx(x[i])
        fx_str = "f(x" + str(i) + ")="
        print(fx_str, end='')
        print(fx_val)
        if fx_val > 0:
            b = x[i]
        else:
            a = x[i]
        if i > 0:

            if int(x[i] * 10**accuracy) == int(x[i-1]* 10**accuracy):
                final_str = "Since xn and xn-1 are same upto 4 decimal places, we have final x as:"
                print(final_str , end='')
                print(x[i])
                break
        
        print()
        print()
        i += 1
    return

def main():

    # Inputs initial approximation
    a = float(input("Enter the initial lower approx:"))
    b = float(input("Enter the initial upper approx:"))
    accuracy = int(input("Accuracy(correct upto how many digits after decimal point):"))

    print()
    print()

    regula_falsi_method(a,b,accuracy)

if __name__=="__main__":
    main()