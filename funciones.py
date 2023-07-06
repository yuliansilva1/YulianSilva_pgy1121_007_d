import os
import time
import msvcrt
import numpy

escenario = numpy.zeros((10,10),int)
lista_numeros = [1,2,3,4,5,6,7,8,9,10,]
lista_ruts = []
lista_fila = []
lista_columna = []
lista_com_ent = []
lista_asiento = []
lista_tipo = []

pre_platinum = 120000 #asiento(1,20)
pre_gold = 80000 #asiento(21,50)
pre_silver = 50000 #demas asientos

acumulador_platinum = 0
acumulador_gold = 0
acumulador_silver = 0
total_acumulador = acumulador_platinum + acumulador_gold + acumulador_silver
total_entrada_platinum = acumulador_platinum * 1200000
total_entrada_gold = acumulador_gold * 80000
total_entrada_silver = acumulador_silver * 50000
total_compra_entrada = total_entrada_platinum + total_entrada_gold + total_entrada_silver
#---------------------
def mensaje_despedida():
    print("yulian,silva,06/07/2023")
    time.sleep(3)

def ver_menu():
    os.system('cls')
    print("""MENÚ
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir""")

def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion in(1,2,3,4,5):
                return opcion
            else:
                print("ERROR! DEBE INGRESAR UNA OPCION VALIDA")
        except:
            print("ERROR! debe ingresar un numero entero")

def compra_entradas():
    while True:
        try:
            entrada = int(input("Ingrese cantidad de entradas: "))
            if entrada >= 1 and entrada <= 3:
                return entrada
            else:
                print("ERROR! el maximo de entradas es de 3")
        except:
            print("ERROR! debe ingresar un numero entero")

def ver_escenario():
    contador = 1
    for x in range(10):
        print(f"\nfila {x+1}", end=" ")
        print("\t")
        for y in range(10):
            print(f" {lista_numeros[y]} {escenario[x][y]} {contador}",end=" ")
            contador += 1
    print("\n")
    time.sleep(3)

def validar_tipo_entrada():
    while True:
        tipo = input("Ingrese tipo de entrada(Platinum: P  Gold: G Silver: S): ")
        if tipo.upper() in("P","G","S"):
            return tipo
        else:
            print("ERROR! DEBE INGRESAR UNA OPCION ENTRE P,G,S")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut(sin puntos ni digito verificador): "))
            if rut >= 10000000 and rut <= 99999999:
                return rut
            else:
                print("ERRO! rut fuera de rango entre 10000000 y 99999999")
        except:
            print("ERROR! debe ingresar un numero entero")
           
def validar_compra_tipo():
    while True:
        try:
            validar_tipo_entrada = int(input("ingrese lugar de asiento"))
            if validar_tipo_entrada in(0,1):
                pre_platinum
            elif validar_tipo_entrada in(2,3,4):
                pre_gold
            elif validar_tipo_entrada in(5,6,7,8,9):
                pre_silver
            else:
                print("ERROR asiento ya ocupado")
        except:
            print("ERROR debe ingresar un numero entero")

def opcion_1():
    com_ent = compra_entradas()
    print("Ingrese asiento")
    ver_escenario()
    time.sleep(3)
    fila = input("ingrese fila: ")
    asiento = input("ingrese numero de asiento: ")
    os.system('cls')
    print("los presios de las entradas son los siguinetes")
    print(f"""
    platinum {pre_platinum}
    gold     {pre_gold}
    silver   {pre_silver}""")
    time.sleep(3)
    tipo = validar_tipo_entrada()
    
    acumulador_gold
    acumulador_platinum
    acumulador_silver
    rut = validar_rut()
    lista_asiento.append(asiento)
    lista_com_ent.append(com_ent)
    lista_tipo.append(tipo)
    lista_ruts.append(rut)
    lista_fila.append(fila)
    print("SU COMPRA A PROCESADO CON EXITO")
    time.sleep(3)

def opcion_2():
    ver_escenario

def opcion_3():
    pass

def opcion_4():
    print("\t""|tipo de entrada |cantidad              |total|")
    print("\t""|----------------|----------------------|-----|")
    print("\t"f"|Platinum        |  {acumulador_platinum}                   ${total_entrada_platinum}        ")
    print("\t""|----------------|----------------------|-----|")
    print("\t"f"|Gold            |  {acumulador_gold}                    ${total_entrada_gold}    ")
    print("\t""|----------------|----------------------|-----|")
    print("\t"f"|Silver          |  {acumulador_silver}                    ${total_entrada_silver}    ")
    print("\t""|----------------| ---------------------|-----|")
    print("\t"f"|total           |  {total_acumulador}                    ${total_compra_entrada}     ")
    print("\t""|----------------|----------------------|-----|")
    time.sleep(4)
