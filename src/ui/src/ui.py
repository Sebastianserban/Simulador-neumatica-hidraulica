import flet as ft

class SimuladorUI:
    def __init__(self,page):
        self.page = page
        self.sidebar = self._crear_barra_lateral()
        self.canvas = self._crear_canvas()
        self.layout = self._crear_layout()
    
    def _crear_barra_lateral(self):
        sidebar = ft.Sidebar()     
        