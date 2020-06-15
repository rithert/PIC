#clase padre
class modelo_matematico():
    def __init__(self,Vlambda1,Vmiu1):
        self.__λ = Vlambda1
        self.__μ = Vmiu1
    
#condicion de estabilidad de PICS
    def condicion_estabilidad(self):
        if (self.__λ/self.__μ) < 1:
            print("Si se cumple la condicion de un modelo matematio PICS")
            return True
        else :
            print("No se cumple la condicion de estabilidad del sistema Pics: ")
            return False





#Clase hijo modelo PICS
class PICS(modelo_matematico):
    def __init__(self,Vlambda1,Vmiu1):
        self.__λ = Vlambda1
        self.__μ = Vmiu1
        super().__init__(self.__λ,self.__μ )

#Probabilidad de hallar el sistema ocupado, utilización del sistema, probabilidad que tienen los usuarios de esperar para ser atendidos   
    def func_ro(self):
            ro = self.__λ/self.__μ
            return(ro)
#La probabilidad de hallar el sistema vacío u ocioso, probabilidad que tienen los usuarios de no esperar o ser atendidos sin esperar en cola:
    def func_p0(self,ro):
        P0 = 1-(ro)
        return(P0)




while True:
    try:
        Vlambda = float(input("Ingrese el valor de lambda(taza de llegada λ): "))
        Vmiu = float(input("Ingrese el valor de miu taza de servicio (taza de servicio μ): "))
        if Vlambda > 0 and Vmiu >0: 
            ObjPICS = PICS(Vlambda,Vmiu)
            break
        else :
            continue
    except ValueError:
        print("Ingrese numeros")
        continue

print("mama")
if ObjPICS.condicion_estabilidad():
    valor_ro = ObjPICS.func_ro()
    print ("LA probabilidad de encontar el sistema ocupado es de ro : ", valor_ro)
    valor_inve_ro = ObjPICS.func_p0(valor_ro)
    print("La probabilidad de hallar el sistema vacio ese de: ", valor_inve_ro)
    