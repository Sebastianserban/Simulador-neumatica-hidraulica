import flet as ft
from components import *

class Draggable(ft.Container):
    def __init__(self, content, top=50, left=50):
        super().__init__(
            content=ft.GestureDetector(
                content=content,
                drag_interval=10,
                on_pan_update=self.drag
            ),
            left=left,
            top=top,
            bgcolor=ft.Colors.TRANSPARENT
        )

    def drag(self, e: ft.DragUpdateEvent):
        self.left = max(0, self.left + e.delta_x)
        self.top = max(0, self.top + e.delta_y)
        self.update()

class SimulatorUI:
    def __init__(self, page):
        self.page = page
        self.page.title = "Simulador Neumático"
        self.setup_ui()

    def setup_ui(self):
        # Tamaños personalizados para cada componente
        self.sizes = {
            "sidebar": {
                "default": 60,
                "Presurizador": 40,  # Más pequeño en sidebar
                "Valvula AND": 50,   # Más pequeña en sidebar
                "Unidad de Mantenimiento": 70  # Más grande en sidebar
            },
            "canvas": {
                "default": 90,
                "Presurizador": 60,  # Más pequeño en canvas
                "Valvula AND": 70,   # Más pequeña en canvas
                "Unidad de Mantenimiento": 150  # Mucho más grande en canvas
            }
        }

        # Componentes disponibles con tamaños personalizados
        self.components = {
            "Cilindro Doble efectos": CilindorDobleEfecto(size=self.sizes["sidebar"]["default"]),
            "Cilindro Simple": CilindorSimpleEfecto(size=self.sizes["sidebar"]["default"]),
            "Valvula AND": ValvulaAND(size=self.sizes["sidebar"]["Valvula AND"]),
            "Valvula OR": ValvulaOR(size=self.sizes["sidebar"]["default"]),
            "Valvula 3/2 con Rodillo": Valvula3_2Cosa(size=self.sizes["sidebar"]["default"]),
            "Valvula 3-2 con Muelle": Valvula3_2Muelle(size=self.sizes["sidebar"]["default"]),
            "Valvula 5-2 con Rodillo": Valvula5_2Cosa(size=self.sizes["sidebar"]["default"]),
            "Valvula 5-2 con Muelle": Valvula5_2Muelle(size=self.sizes["sidebar"]["default"]),
            "Presurizador": PresurizadoNeumatico(size=self.sizes["sidebar"]["Presurizador"]),
            #"Unidad de Mantenimiento": UnidadMantenimiento(size=self.sizes["sidebar"]["Unidad de Mantenimiento"])
        }

        # Barra lateral con botones
        sidebar = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Column([
                            comp.imagen,
                            ft.ElevatedButton(
                                text=name,
                                on_click=lambda e, c=comp: self.add_to_canvas(c),
                                width=140,
                                height=40
                            )
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        padding=5,
                    ) for name, comp in self.components.items()
                ],
                spacing=10,
                scroll=ft.ScrollMode.AUTO
            ),
            width=180,
            bgcolor=ft.Colors.BROWN_700,
            padding=10
        )

        # Área de trabajo con Stack
        self.canvas_stack = ft.Stack([])
        
        # Añadir unidad de mantenimiento fija en esquina inferior izquierda
        unidad_mantenimiento = UnidadMantenimiento(size=self.sizes["canvas"]["Unidad de Mantenimiento"])
        self.fixed_unit = ft.Container(
            content=unidad_mantenimiento.imagen,
            left=20,
            bottom=20,  # Fija en la esquina inferior izquierda
            width=self.sizes["canvas"]["Unidad de Mantenimiento"],
            height=self.sizes["canvas"]["Unidad de Mantenimiento"]
        )
        self.canvas_stack.controls.append(self.fixed_unit)
        
        canvas_container = ft.Container(
            content=self.canvas_stack,
            expand=True,
            bgcolor=ft.Colors.AMBER_100,
            padding=10
        )

        # Botones de control en la parte inferior
        control_buttons = ft.Row([
            ft.ElevatedButton("Iniciar Simulación", icon=ft.icons.PLAY_ARROW),
            ft.ElevatedButton("Detener", icon=ft.icons.STOP),
            ft.ElevatedButton("Limpiar Canvas", icon=ft.icons.CLEAR),
            ft.ElevatedButton("Guardar", icon=ft.icons.SAVE),
            ft.ElevatedButton("Cargar", icon=ft.icons.UPLOAD_FILE),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

        # Layout principal
        self.page.add(
            ft.Column([
                ft.Row([sidebar, canvas_container], expand=True),
                ft.Divider(),
                control_buttons
            ], expand=True)
        )

    def add_to_canvas(self, component):
        # No añadir más unidades de mantenimiento (ya hay una fija)
        if isinstance(component, UnidadMantenimiento):
            return
            
        # Determinar el tamaño adecuado para cada componente
        if isinstance(component, PresurizadoNeumatico):
            component_size = self.sizes["canvas"]["Presurizador"]
        elif isinstance(component, ValvulaAND):
            component_size = self.sizes["canvas"]["Valvula AND"]
        else:
            component_size = self.sizes["canvas"]["default"]
            
        # Creamos una nueva imagen con el tamaño adecuado
        canvas_image = ft.Image(
            src=component.imagen.src,
            width=component_size,
            height=component_size
        )
        
        draggable = Draggable(canvas_image)
        self.canvas_stack.controls.append(draggable)
        self.page.update()

def main(page: ft.Page):
    SimulatorUI(page)

ft.app(target=main)