class Function:
    def __init__(self,name,a,b):
        self.name=name
        self.a=a
        self.b=b
    
    def printname(self):
        print("Function: ", self.name, "tra [", self.a,",", self.b, "]")
    
    def min_value(self,delta_x=0.5):
        x_start=self.a
        x_end=self.b
        i=0

        f_x=[]

        x=[]

        while(x_start+i*delta_x)<x_end:
            this_x=x_start+i*delta_x
            this_fx=self.eval(this_x)
            x=x+[this_x]
            f_x=f_x+[this_fx]

            i=i+1

class Retta(Function):
    def __init__(self,a,b,m,q):
        super().__init__("Retta",a,b)
        self.m=m
        self.q=q
    
    def eval(self,x):
        return self.m*x+self.q

bisettrice = Retta(-3,3,1,0)

print(bisettrice.min_value(delta_x=1))