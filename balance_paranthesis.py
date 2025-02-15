class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[]
        close=[')',']','}']
        for i in s:
            if len(st) and ((i==')' and st[-1]=='(') or (i=='}' and st[-1]=='{') or (i==']' and st[-1]=='[') ):
                st.pop()
            else:
                st.append(i)
        if len(st):
            return False
        return True