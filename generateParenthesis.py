def generateParenthesis(n: int) -> list[str]:
        
    comb = [] 
    all_comb = []
    
    def backtrack(openB, closeB):

        if openB == closeB == n:
            all_comb.append("".join(comb))
            return 
        
        if openB < n:
            comb.append("(")
            backtrack(openB+1, closeB)
            comb.pop()
            
        if closeB < openB:
            comb.append(")")
            backtrack(openB, closeB+1)
            comb.pop()
            
    backtrack(0,0)        
    return all_comb
        

if __name__ == "__main__":
    print(generateParenthesis(n=3))