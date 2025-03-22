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
        # Crear una instancia de UnidadMantenimiento
        unidad_mantenimiento = UnidadMantenimiento()

        # Envolver la imagen en un Container para agregar margen
        imagen_con_margen = ft.Container(
            content=unidad_mantenimiento.imagen,  # Agregar la imagen de la Unidad de Mantenimiento
            margin=60  # Agregar un margen de 10 píxeles alrededor de la imagen
        )

    # Crear un Column para organizar los controles en el canvas
        colm = ft.Column(
            controls=[
                imagen_con_margen  # Usar el Container con margen
            ],
            alignment=ft.MainAxisAlignment.END,  # Alinear el contenido al final (abajo)
            horizontal_alignment=ft.CrossAxisAlignment.START,  # Alinear a la izquierda
            expand=True  # Expandir el Column para ocupar todo el espacio disponible
        )

        boton_reanudar = ft.ElevatedButton(
            text="▶️",  # Emoji de Play
            #on_click=self._reanudar_simulacion,  # Función para manejar el evento
            bgcolor="#4CAF50",  # Color de fondo verde
            color="white"  # Color del texto
        ) 

        boton_quitar = ft.ElevatedButton(
            text="🗑️",  # Emoji de Papelera
            #on_click=self._quitar_elementos,  # Función para manejar el evento
            bgcolor="#F44336",  # Color de fondo rojo
            color="white"  # Color del texto
        )

        botones = ft.Row(
            controls=[boton_reanudar, boton_quitar],  # Agregar los botones al Row
            alignment=ft.MainAxisAlignment.CENTER,  # Alinear los botones al centro
            spacing=10  # Espaciado entre los botones
        )

        
    # Devolver un Container que contiene el Column
        return ft.Container(
            content=ft.Stack(
                controls=[
                    colm,
                    ft.Container(
                        content=botones,
                        alignment=ft.alignment.top_right,
                        margin=10
                    )
                ],
                expand=True         
            ),  # Agregar el Column como contenido del Container
            expand=True,  # Expandir el Container para ocupar todo el espacio disponible
            bgcolor="#A08963",  # Color de fondo del canvas
            alignment=ft.Alignment(-1,1)  # Alinear el contenido en la esquina inferior izquierda
        )

    def _crear_layout(self):
        return ft.Row(controls=[self.sidebar, self.canvas], spacing=0, expand=True)