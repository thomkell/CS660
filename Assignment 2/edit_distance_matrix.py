def edit_distance(A, B):
    m, n = len(A), len(B)
    
    # Initialize the table with zeros
    ED = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    # Base cases
    for i in range(m+1):
        ED[i][0] = i
    for j in range(n+1):
        ED[0][j] = j
        
    # Fill the table using the recurrence relation
    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                ED[i][j] = ED[i-1][j-1]
            else:
                ED[i][j] = 1 + min(ED[i-1][j], ED[i][j-1], ED[i-1][j-1])
                
    return ED

A = "THE"
B = "TWO"
ED_table = edit_distance(A, B)

# Print the table
for row in ED_table:
    print(row)
