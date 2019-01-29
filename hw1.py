# import only standard Python 3 libraries here.

# input: positive integer x
# output: True or False
def isDivBySeven(x):
    print(x) # do not remove this line
    # negative case
    if x < 0: 
        return isDivBySeven(-x)
    # base case
    if( x == 0 or x == 7 )
        return True
    if ( x < 10 ):
        return False
    return isDivBySeven( x / 10 - 2 * ( x - x / 10 * 10 ) ) 
   
# input: positive integer x
# output: True or False
def isPrime(x):
	print(x)
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False

    return True
   

if __name__ == '__main__':
	'''Nothing below this line will be executed by the autograder ---
			use this space to test your code!'''
			
