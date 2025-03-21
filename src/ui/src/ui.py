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

        return ft.Column(
            controls=[
                ft.Text("Herramientas"),
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
            width=200,
            alignment=ft.alignment.top_center,
            spacing=10
        )

    def _crear_canvas(self):
        return ft.Container(
            width=1200,
            height=1200,
            expand=True,
            bgcolor=ft.colors.BLUE_GREY_400,
            alignment=ft.alignment.center,
        )

    def _crear_layout(self):
        return ft.Row(controls=[self.sidebar, self.canvas], spacing=10)