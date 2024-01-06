""" 509. Fibonacci Number
Easy

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 


Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.


Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Constraints:

0 <= n <= 30 """


class Leet_509_FibonacciNumber:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        fibarray = [1, 1]

        def rec(N):
            if N == 2:
                return
            fibarray.append(sum(fibarray))
            fibarray.pop(0)
            #print (fibarray)
            rec(N-1)
        rec(n)

        return fibarray[-1]
    
""" print (Leet_509_FibonacciNumber().fib(0))
print (Leet_509_FibonacciNumber().fib(1))
print (Leet_509_FibonacciNumber().fib(2))
print (Leet_509_FibonacciNumber().fib(3))
print (Leet_509_FibonacciNumber().fib(4))
print (Leet_509_FibonacciNumber().fib(5))
print (Leet_509_FibonacciNumber().fib(6))
print (Leet_509_FibonacciNumber().fib(7)) """

for i in range(20):
    print ("Fibonacci Number: {} = {} ".format(i, Leet_509_FibonacciNumber().fib(i)))

        