import flet as ft

# Clases de los componentes
class CilindorDobleEfecto:
    def __init__(self, size=60):
        self.imagen = ft.Image(
            src="src/ui/src/assets/Simbolos neumatica/cilindros/Cilindro de doble efecto.png",
            width=100,
            height=100
        )

class CilindorSimpleEfecto:
    def __init__(self, size=60):
        self.imagen = ft.Image(
            src="src/ui/src/assets/Simbolos neumatica/cilindros/Cilindro de simple efecto.png",
            width=100,
            height=100
        )

class ValvulaAND:
    def __init__(self, size=60):
        self.imagen = ft.Image(
            src="src/ui/src/assets/Simbolos neumatica/valvulas/Valvula AND.png",
            width=80,
            height=80
        )

class ValvulaOR:
    def __init__(self, size=60):
        self.imagen = ft.Image(
            src="src/ui/src/assets/Simbolos neumatica/valvulas/Valvula OR.png",
            width=100,
            height=100
        )

class Valvula3_2Cosa:
    def __init__(self, size=60):
        self.imagen = ft.Image(
            src="src/ui/src/assets/Simbolos neumatica/valvulas/valvuala 3-2/Valvula 3-2 con cosa rara.png",
            width=100,
            height=100
        )

class Valvula3_2Muelle:   
    def __init__(self, size=60):
        self.imagen = ft.Image(
            src="src/ui/src/assets/Simbolos neumatica/valvulas/valvuala 3-2/Valvula 3-2 con muelle.png",
            width=100,
            height=100
        )

class Valvula5_2Cosa:
    def __init__(self, size=60):
        self.imagen = ft.Image(
            src="src/ui/src/assets/Simbolos neumatica/valvulas/valvula 5-2/valvula5-2 con cosa rara.png",
            width=100,
            height=100
        )

class Valvula5_2Muelle:
    def __init__(self, size=60):
        self.imagen = ft.Image(
            src="src/ui/src/assets/Simbolos neumatica/valvulas/valvula 5-2/Valvula 5-2 con muelle.png",
            width=100,
            height=100
        )

class UnidadMantenimiento:
    def __init__(self, size=60):
        self.imagen = ft.Image(
            src="src/ui/src/assets/Simbolos neumatica/miscelanea/unidad de mantenimiento.png",
            width=120,
            height=120 
        )

class PresurizadoNeumatico:
    def __init__(self, size=60):
        self.imagen = ft.Image(
            src="src/ui/src/assets/Simbolos neumatica/miscelanea/Presurizado neumático.png",
            width=100,
            height=100
        )



        