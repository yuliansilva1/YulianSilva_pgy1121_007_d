import funciones as fn

while True:
    fn.ver_menu()
    opcion = fn.validar_opcion()
    if opcion==1:
       fn.opcion_1()
    elif opcion==2:
        fn.ver_escenario()
    elif opcion==3:
        fn.opcion_3()
    elif opcion==4:
        fn.opcion_4()
    else:
        fn.mensaje_despedida()
