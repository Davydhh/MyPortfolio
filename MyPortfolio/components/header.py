import reflex as rx
from MyPortfolio.style import style


class Header(rx.Hstack):
    def __init__(self):
        super().__init__(style=style.get("header"))
        self.children = [
            rx.heading("Davide.dev", size="md"),
            rx.spacer(),
            rx.color_mode_button(
                rx.color_mode_icon(),
                color_scheme="none",
                _dark= {"color": "white"},
                _light= {"color": "black"},
            )
        ]
