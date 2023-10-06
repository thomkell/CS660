def minimumPenalty(D):
    # Initialization
    n = len(D)
    penalty = [float('inf')] * n
    # Base case
    penalty[0] = 0
    
    # Iterations
    for i in range(1, n):
        print(i)
        for j in range(i):
            print(j)
            distance = D[i] - D[j]
            day_penalty = (200 - distance)**2
            temp_penalty = penalty[j] + day_penalty
            if temp_penalty < penalty[i]:
                penalty[i] = temp_penalty    
    
    return penalty[n-1]

# Example
D = [1, 50, 150, 300, 350, 550]
min_penalty = minimumPenalty(D)
print("Minimum Penalty:", min_penalty)
