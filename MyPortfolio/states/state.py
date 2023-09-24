import reflex as rx

class State(rx.State):
    drawer_open: bool = False

    modal_open: bool = False

    def toggle_drawer(self):
        """Toggle the drawer."""
        self.drawer_open = not self.drawer_open

    def toggle_modal(self):
        """Toggle the new chat modal."""
        self.modal_open = not self.modal_open