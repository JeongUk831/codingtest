def solution(n,m):
    def gcd(n,m):
        while m > 0:
            n,m = m,n % m
        return n
    def lcm(n,m):
        return n*m // gcd(n,m)
    return [gcd(n,m),lcm(n,m)]


print(solution(3,12))