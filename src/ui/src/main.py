import flet as ft
from ui import SimuladorUI

def main(page: ft.Page):
    page.window_height = 1024
    page.window_width = 768
    #page.theme_mode = ft.ThemeMode.LIGHT

    simulador = SimuladorUI(page)
    page.add(simulador.layout)


ft.app(target=main)