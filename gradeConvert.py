 
#grade โปรแกรมแปลงเกรดที่อยู่ในรูปตัวอักษรเป็นตัวเลข     cr : Benjaporn Kittivichainchai 61172310280-8 CPE.61231

grade = input("Your score = ")
def grade1(grade):
   
    if grade == "A" :
        print ("80-100")
    elif grade == "B" :
        print ("70-79")
    elif grade == "C" :
        print ("60-69")
    elif grade == "D" :
        print ("50-159")
    elif grade == "F" :
        print ("0-49")
    else:
        print("ERROR")

grade1(grade)


