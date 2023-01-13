def climbStairs(n):
        memoize={1:1,2:2}
        def cs(n):
            if n == 0:
                return 0
            elif n in memoize:
                return memoize[n]
            else:
                memoize[n] = cs(n-1) +cs( n-2)
            return memoize[n]
        return cs(n)

climbStairs(2)
climbStairs(4)
climbStairs(6)

# DP
def climbStairs(n):
    if n==0: return 0
    if n==1: return 1
    if n==2: return 2
    dp = [0]*(n+1) # considering zero steps we need n+1 places
    dp[1]= 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1] +dp[i-2]
    print(dp)
    return dp[n]
        
climbStairs(6)
climbStairs(4)