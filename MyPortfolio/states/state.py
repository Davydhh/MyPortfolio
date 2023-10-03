import reflex as rx

class State(rx.State):
    is_menu_open: bool = False

    def toggle_menu(self):
        self.is_menu_open = not self.is_menu_open