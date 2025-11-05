class const_dest:
    x = 0
    def _init_(self,color,type):
        self.color = color
        self.type = type
        print("Constructor called")
    def _init_(self):
        print("Destructor called")
c = const_dest("red", "sedan")
print(c.color)
print(c.type)

c = const_dest("blue","hatchback")
print(c.color)
print(c.type)
c._init_()  # This will not call the destructor as expected, since the method