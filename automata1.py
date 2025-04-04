#class Automata:
 
#    def consecutivo (self, cadena):
#        if 'aa' in cadena or 'bb' in cadena:
#            print('Estado NO Aceptado')
#        else:
#            print('Estado Aceptado')
#                
#automata = Automata()
#cadena = input("Ingresa una cadena \n")
#automata.consecutivo(cadena)

#AFD en donde no se aceptas a's o b's consecutivas
          
class Automata:
    def procesar_cadena(self, cadena):
        if not cadena:
            estado = 'q0'
            return print('q0 Estado de Aceptación')
        
        anterior = None
        estado = None
        
        for caracter in cadena:
            if anterior == caracter:
                estado = 'q3' 
                return print(f"{estado} Estado de No Aceptación")
            if caracter == 'a':
                estado = 'q1'
            elif caracter == 'b':
                estado = 'q2'
            
            anterior = caracter
        
        if estado == 'q1' or estado == 'q2':
            return print(f"{estado} Estado de Aceptación")

automata = Automata()
cadena = input('Ingresa la cadena: \n')
automata.procesar_cadena(cadena)

         
            