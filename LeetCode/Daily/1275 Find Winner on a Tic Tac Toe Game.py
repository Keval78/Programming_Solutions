'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def tictactoe(self, moves: List[List[int]]) -> str:
            def winner(moves: List[List[int]]):
                for i in range(3):
                    if len([m for m in moves if m[0]==i])==3 or len([m for m in moves if m[1]==i])==3:
                        return True
                return len([m for m in moves if m[0]==m[1]])==3 or len([m for m in moves if m[0]==2-m[1]])==3

            x_moves = [moves[i] for i in range(len(moves)) if i%2==0]
            o_moves = [moves[i] for i in range(len(moves)) if i%2!=0]
            if winner(x_moves): return "A"
            if winner(o_moves): return "B"
            if len(x_moves)+len(o_moves)<9: return "Pending"
            return "Draw"
    Solution().tictactoe()


if __name__ == "__main__":
    main()
