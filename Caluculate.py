class perimeter:
    def rect(self,l,b):
        print("Area of rectangle "+str(l*b))
        print("Perimeter of Rectangle "+str(2*(l+b)))
    def circle(self,r):
        print("Area of circle "+str(3.14*r*r))
        print("perimeter of circle "+str(2*3.14*r))
    def triangle(self,b,h,s):
        print("Area of Triangle "+str(1/2)*b*h)
        print("Perimeter of Triangle "+str(3*s))
obj=perimeter()
ch=int(input("Select the input"))
if(ch==1):
    obj.rect(int(input("Enter 1st Side:")), int(input("Enter 2nd Side:")))
elif(ch==2):
    obj.circle(int(input("Enter Radius:")))
elif(ch==3):
    obj.triangle(int(input("Enter 1st Side:")), int(input("Enter 2nd Side:")),int(input("Enter 3rd Side:")))