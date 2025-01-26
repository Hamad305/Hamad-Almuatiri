#function that performs the Euclidean Algorithm to find the greatest Common Divisor of two numbers
#@param two integers; a and b
#@return returns an integer value (GCD of a and b)
#the function is a recursive function
def EuclideanAlgo (a,b):
    #base case for the recursive function, the recursive calls continue until the number b becomes zero   
    if (a==0):
         return b
    elif (b==0):
       #when the base condition becomes true it return the value of 'a', which will be the value of GCD
       return a
    else :
       #the main logic of Euclidean Algorithm is that it repeatedly divides the first number with the remainder of the division; a/b 
       #until be remainder is zero and the return the value of 'a'; (base condition)
       # the following step calculates the remainder of a divided by b and stores it into temp
     temp = a % b 
     #this is the recursive call, the value of 'a' updates to b and  value of b updates to the remainder of division (according to the algorithm)
     return EuclideanAlgo(b,temp)

def main():
    print(EuclideanAlgo(48,18))

if __name__ == "__main__":
  main()
