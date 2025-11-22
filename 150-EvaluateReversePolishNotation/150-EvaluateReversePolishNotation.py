# Last updated: 11/21/2025, 8:46:44 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for t in tokens:
            if t == '+':
                a, b = st.pop(), st.pop()
                st.append(b + a)
            elif t == '-':
                a, b = st.pop(), st.pop()
                st.append(b - a)
            elif t == '*':
                a, b = st.pop(), st.pop()
                st.append(b * a)
            elif t == '/':
                a, b = st.pop(), st.pop()
                st.append(int(b / a))
            else:
                st.append(int(t))

        return st.pop()