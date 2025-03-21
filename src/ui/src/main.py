import flet as ft

def main(page: ft.Page):
    page.title = "Simulador de Circuitos"
    page.window_width = 800
    page.window_height = 600

    # Área de trabajo (lienzo)
    canvas = ft.Container(
        content=ft.Text("Área de trabajo", size=20, color=ft.colors.BLACK),
        expand=True,  # Ocupa todo el espacio disponible
        bgcolor=ft.Colors.BLUE_GREY_400,  # Color de fondo
        alignment=ft.alignment.center,  # Centrar el contenido
    )

    # Estructura de la app (por ahora solo el lienzo)
    page.add(canvas)

ft.app(target=main)