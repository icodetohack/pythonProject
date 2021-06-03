<h1 align="center">CodeWars #14 Playing with digits</h1>
<h3 align="center">Some numbers have funny properties. For example: 89 --> 8¹ + 9² = 89 * 1 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51 Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n. In other words: Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k If it is the case we will return k, if not return -1. Note: n and p will always be given as strictly positive integers.</h3>

- Example **dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1 dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2 dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51**


<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Solution : 

def dig_pow(n, p):
    import math as m
    sum=0
    for i in str(n):
        sum=sum+m.pow(int(i),p)
        p=p+1
    y = list(m.modf(sum/n))
    if y[0]==0.0: return y[1]
    else: return -1
