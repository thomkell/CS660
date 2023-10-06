def maxCoins(A):
    # Init
    n = len(A)
    B = [1] + A + [1]

    dp = [[0] * (n+2) for _ in range(n+2)]
    
    # Base case
    for i in range(1, n+1):
        dp[i][i] = B[i-1] * B[i] * B[i+1]

    # Iterations for subarrays of different length
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            for k in range(i, j+1):
                coins = B[i-1] * B[k] * B[j+1] + dp[i][k-1] + dp[k+1][j]
                dp[i][j] = max(dp[i][j], coins)
                
    return dp[1][n]

# Example
A = [3,1,5,8]
print(maxCoins(A))  # Expected output: 167