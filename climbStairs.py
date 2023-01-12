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