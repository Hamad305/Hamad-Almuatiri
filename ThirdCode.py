#class for defining the Euclidean Algorithm
#members – it has two functions
#EuclideanAlgo(a,b)
#taking_input()
class EuclideanAlgorithm:
 def __init__(self):
     pass
#function that performs the Euclidean Algorithm to find the greatest Common Divisor of two numbers
#@param two integers; a and b
#@return returns an integer value (GCD of a and b)
#the function is a recursive function

 def EuclideanAlgo (self,a,b):
   if (a==0):
    return b
    #base case for the recursive function, the recursive calls continue until the number b becomes zero
   if (b==0):
       #when the base condition becomes true it return the value of 'a', which will be the value of GCD
       return a
   else :
       #the main logic of Euclidean Algorithm is that it repeatedly divides the first number with the remainder of the division; a/b 
       #until be remainder is zero and the return the value of 'a'; (base condition)
       # the following step calculates the remainder of a divided by b and stores it into temp
     temp = a % b 
     #this is the recursive call, the value of 'a' updates to 'b' and value of b updates to the remainder of division (according to the algorithm)
     return self.EuclideanAlgo(b,temp)

 #function for taking input from user
 def taking_input(self):
     while(True):
        a = int(input("Enter first number (positive): "))
       #if the input is invalid, i.e a negative number then it will throw an error asks repeatedly to enter a valid number
        while (a<0):
           a = int(input(f"Enter a valid number: "))
        b = int(input("Enter second number (positive): "))
        while (b<0):
            b = int(input(f"Enter a valid  number"))
        print(f"The GCD of {a} and {b} is  {self.EuclideanAlgo(a,b)}")
        break

def main():
    obj1 = EuclideanAlgorithm()
    obj1.taking_input()


if __name__ == "__main__":
  main()


tuple (int) EuclideanAlgo (int a, int b)
if (b==0):
     return (a,1,0)
else:
   gcd, c, d = EuclideanAlgo (b, a mod b)
   x = c
   y = d
return (gcd, x, y)


