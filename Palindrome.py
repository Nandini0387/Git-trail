def isPalindrome(x: int) -> bool:
        temp = x
        rev = 0
        if x<0:
            return False
        while(x>0):
                r = x%10
                rev = r+(rev*10)
                x = x//10
        if temp ==rev:
            return True
if isPalindrome(121):
    print("True")
else:
    print("False")