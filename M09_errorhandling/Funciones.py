class Funciones:

    def __init__(self,lista_n):
        if (type(lista_n) != list):
            self.lista = []
            raise ValueError('Se ha creado una lista vacía. Se esperaba una lista de números enteros')  
        else:
            self.lista = lista_n

    def primo(self):
        lista_primos = []
        for i in self.lista:
            if (self.__primo(i)):
                lista_primos.append(True)
            else:
                lista_primos.append(False)
        return lista_primos

    def factorial(self):
        lista_factorial = []
        for i in self.lista:
            lista_factorial.append(self.__factorial(i))
        return lista_factorial

    def conversor_temperatura(self, origen, destino):
        parametros_esperados = ['Celsius','Kelvin','Farenheit']
        lista_conversion = []
        if str(origen) not in parametros_esperados:
            print('Los parametros esperados son:', parametros_esperados)
            return lista_conversion
        if str(destino) not in parametros_esperados:
            print('Los parametros esperados son:', parametros_esperados)
            return lista_conversion
        for i in self.lista:
            lista_conversion.append(self.__conversor_temperatura(i, origen, destino))
        return lista_conversion
                            

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