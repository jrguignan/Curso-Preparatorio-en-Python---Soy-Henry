class Funciones:

    def __init__(self,lista_n):
        self.lista=lista_n

    def primo(self):
        for i in self.lista:
            if (self.__primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')  

    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__factorial(i))  

    def conversor_temperatura(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__conversor_temperatura(i, origen, destino),'grados',destino)    
                            

#Verificar Primo
    def __primo(self,a):
        b=True
        for i in range(2,a):  
            if a%i==0:
               b=False
               break 
          
        return b   

#Valor Modal
    def cuenta_repetidos(self):
        valor=[]
        cuenta=[]
        for i in self.lista:
            valor.append(i)
            cuenta.append(self.lista.count(i))

        moda=valor[cuenta.index(max(cuenta))]   
        repeticiones=max(cuenta) 

        return moda,repeticiones

   

#Factorial
    def __factorial(self,num):
    #Permite guardar una descriptcion de la funcion al usar help()
      ''' 
       Calcula el factorial de un numero
       '''
      if num>1:
          num = num*self.__factorial(num-1)

      return num     

#Conversor de Temperatura
    def __conversor_temperatura(self,v,e,s):
     if e=="Celsius":
        unidad_e="Grados Celsius"
        if s=="Farenheit":
           salida=(v*9/5)+32
           unidad_s="Grados Farenheit"
        elif s=="Kelvin":
           salida=v+273.15
           unidad_s="Grados Kelvin"
        else: 
           salida=v
           unidad_s="Grados Celsius"  



     elif e=="Farenheit":
        unidad_e="Grados Farenheit"
        if s=="Celsius":
            salida=(v-32)*5/9
            unidad_s="Grados Celsius"
        elif s=="Kelvin":
            salida=((v-32)*5/9)+273.15
            unidad_s="Grados Kelvin"
        else: 
            salida=v
            unidad_s="Grados Farenheit"   



     elif e=="Kelvin":
        unidad_e="Grados Kelvin"
        if s=="Celsius":    
            salida=v-273.15
            unidad_s="Grados Celsius"
        elif s=="Farenheit":
            salida=((v-273.15)*9/5)+32
            unidad_s="Grados Farenheit" 
        else:  
            salida=v
            unidad_s="Grados Kelvin"   

     else:
        print("Expresion de Temperatura  No Valida")    

     sal=round(salida,4)        

     return sal