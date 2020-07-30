class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.a = []
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.a==[] or x<=self.a[-1]:
          self.a.append(x)
        self.l.append(x)
      

    def pop(self):
        """
        :rtype: None
        """
        y=self.l.pop()
        if y==self.a[-1]:
          self.a.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.l)==0:
          return None
        else:
          return self.l[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        if len(self.a)==0:
            return None
        else:
            return self.a[-1]  
        
# Your MinStack object will be instantiated and called as such:
#  obj = MinStack()
#  obj.push(x)
#  obj.pop()
#  param_3 = obj.top()
#  param_4 = obj.getMin()