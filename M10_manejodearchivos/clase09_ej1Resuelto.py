import sys

if len(sys.argv)==4:
    print("Se introdujo en numero de parametros correctos")
    for i in range(1,len(sys.argv)):
     print(i) 

else:
    print("No se introdujo en numero de parametros correctos") 


