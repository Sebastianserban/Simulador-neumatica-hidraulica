import flet as ft
from components import *

class SimuladorUI:
    def __init__(self, page):
        self.page = page
        self.sidebar = self._crear_barra_lateral()  # Función para crear la barra lateral
        self.canvas = self._crear_canvas()          # Función para crear el canvas
        self.layout = self._crear_layout()          # Función para crear el layout

    # Creación de la barra lateral
    def _crear_barra_lateral(self):
        cilindor_doble_efecto = CilindorDobleEfecto()
        cilindor_simple_efecto = CilindorSimpleEfecto()
        valvula_and = ValvulaAND()
        valvula_or = ValvulaOR()
        valvula3_2_cosa = Valvula3_2Cosa()
        valvula3_2_muelle = Valvula3_2Muelle()
        valvula5_2_cosa = Valvula5_2Cosa()
        valvula5_2_muelle = Valvula5_2Muelle()
        unidad_mantenimiento = UnidadMantenimiento()
        presurizado_neumatico = PresurizadoNeumatico()

        # Crear el Column con los controles
        column = ft.Column(
            controls=[
                cilindor_doble_efecto.imagen,
                cilindor_simple_efecto.imagen,
                valvula_and.imagen,
                valvula_or.imagen,
                valvula3_2_cosa.imagen,
                valvula3_2_muelle.imagen,
                valvula5_2_cosa.imagen,
                valvula5_2_muelle.imagen,
                presurizado_neumatico.imagen
            ],
            alignment=ft.alignment.top_center,
            spacing=7,
            expand=True,  # Asegura que el Column ocupe todo el espacio disponible
        )

        # Envolver el Column en un Container para cambiar el color de fondo
        return ft.Container(
            content=column,
            width=140,  # Ancho de la barra lateral
            bgcolor="#706D54",  # Color de fondo
           # border_radius=10,  # Bordes redondeados
            padding=10,  # Espaciado interno
            margin=0
        )

    def _crear_canvas(self):
        return ft.Container(
            expand=True,
            bgcolor="#A08963",
            alignment=ft.alignment.center,
        )

    def _crear_layout(self):
        return ft.Row(controls=[self.sidebar, self.canvas], spacing=0, expand=True)