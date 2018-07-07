
def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("True") 
    else:
        print("False")         
s1 ="listen"
s2 ="silent"
s1.replace(" ","")
s2.replace(" ","")

check(s1, s2)