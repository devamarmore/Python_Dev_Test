def find_pattern(G, P):
    rows_G, cols_G = len(G), len(G[0])
    rows_P, cols_P = len(P), len(P[0])
    for r in range(rows_G - rows_P + 1):
        for c in range(cols_G - cols_P +1):
            match = all(G[r + i][c:c + cols_P] == P[i]
                        for i in range(rows_P)
                        )
            if match:
                print(f"Pattern not Found at G[{r}][{c}]")
                return "yes", 
            return "no"

G = [  
    '7283455864',  
    '6731158619',  
    '8988242643',  
    '3830589324',  
    '2229505813',  
    '5633845374',  
    '6473530293',  
    '7053106601'  
]  
P = [  
    '9505',  
    '3845',  
    '3530'  
]  

print(find_pattern(G, P))