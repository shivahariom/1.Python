# This library has multiple classes which are used in A1-Class.jpynb
class SubfieldsInAI():
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
class OddEven():
    def OddEven():
        num=int(input("Enter a number:"))
        if((num%2)==0):
            print(num, "is Even number")
        else:
            print(num, "is Odd number")
class ElegiblityForMarriage():
    def Elegible():
        gender=str(input("Your Gender:"))
        age=int(input("Your Age:"))
        if((gender.lower()=="male" and age>=21) or (gender.lower()=="female" and age>=18)):
            print("ELIGIBLE")
        else:
            print("NOT ELIGIBLE")
class FindPercent():
    def percentage():
        s1=int(input("Subject1="))
        s2=int(input("Subject2="))
        s3=int(input("Subject3="))
        s4=int(input("Subject4="))
        s5=int(input("Subject5="))
        total=s1+s2+s3+s4+s5
        print("Total :",total)
        print("Percentage :",(total/500)*100)
class triangle():
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:",(height*breadth)/2)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",height1+height2+breadth)