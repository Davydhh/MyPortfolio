import reflex as rx

class State(rx.State):
    is_menu_open: bool = False

    images_paths: list = ["/java.png", "/python.png",
                          "/spring-boot.png", "/postgresql.png", "/mongodb.png"]

    def toggle_menu(self):
        self.is_menu_open = not self.is_menu_open