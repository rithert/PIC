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
class pICS(modelo_matematico):
    def __init__(self,Vlambda1,Vmiu1):
        self.__λ = Vlambda1
        self.__μ = Vmiu1
        super().__init__(self.__λ,self.__μ )

    #Probabilidad de hallar el sistema ocupado, utilización del sistema, probabilidad que tienen los usuarios de esperar para ser atendidos   
    def func_ro(self):
            ro = self.__λ/self.__μ
            return(round(ro,4))

    #La probabilidad de hallar el sistema vacío u ocioso, probabilidad que tienen los usuarios de no esperar o ser atendidos sin esperar en cola:
    def func_p0(self,ro):
        P0 = 1-(ro)
        return(round(P0,4))


    


class PIC_prob_num_cliente():
    def __init__(self,RO,P_0):
        self.__ρ  = RO
        self.__p0 = P_0
        self.Pt = 0
    

    #La probabilidad de hallar exactamente n clientes dentro del sistema
    def func_nclientes(self,n):
        Pn = self.__p0 *( self.__ρ**n)
        return (round(Pn,4))

    #La probabilidad de hallar exactamente n clientes dentro del sistema, valores(lista) ingresdos por el cliente
    def func_nclientes_range(self,ro,P0,lista):
        for i in  lista:
            Pn = P0*(ro**i)
            self.Pt += Pn
        return (round(Pn,4))
    
    #La probabilidad de hallar exactamente n clientes dentro del sistema rango[x-n]
    def func_nclientes_range(self,ro,P0,Xinicial,Xfinal):
        lista = list(range(Xinicial,Xfinal))
        for i in  lista:
            Pn = P0*(ro**i)
            self.Pt += Pn
        return (round(Pn,4))

    #La probabilidad de hallar exactamente al menos n clientes dentro del sistema 
    def func_nclientes_range(self,ro,P0,Xinicial):
        lista = list(range(Xinicial,0,-1))
        for i in  lista:
            Pn = P0*(ro**i)
            self.Pt += Pn
        Almenos_nclientes= 1-self.Pt
        return (round(Almenos_nclientes,4))








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



if ObjPICS.condicion_estabilidad():
    valor_ro = ObjPICS.func_ro()
    print ("LA probabilidad de encontar el sistema ocupado es de ro : ", valor_ro)
    valor_inve_ro = ObjPICS.func_p0(valor_ro)
    print("La probabilidad de hallar el sistema vacio ese de: ", valor_inve_ro)




prob_Total = 0

print("""Menu
        1. Probabilidad de usuarios en el sistema
        2. Probabilidad de usuarios en cola 
        """)

opcion = int(input("Ingrese la una opcion "))
if opcion ==1:
    while(True):
        print ("La probabilidad de hallar exactamente n clientes dentro del sistema")
        n_clientes = int(input("Ingrese el numero de clientes EN EL SISTEMA "))
        proba_n_clientes = ObjPICS.func_nclientes(valor_ro,valor_inve_ro,n_clientes)
        print(f"Probabiliad de hallar {n_clientes} clientes: {proba_n_clientes}")
        prob_Total += proba_n_clientes
        seguir = input("Si desea parar ingrese *")
        if seguir == "*":
            break
        else:
            continue
    print("Probilidad total: ", prob_Total)
            
else:
    prob_Total += proba_n_clientes
    print ("Probabilidad total:", prob_Total)