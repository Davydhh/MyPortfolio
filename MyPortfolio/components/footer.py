import reflex as rx
from MyPortfolio.style import style


class Footer(rx.Hstack):
    def __init__(self):
        super().__init__(style=style.get("footer"))
        self.children = [
            rx.text(
                "Copyright © 2023. All rights reserved",
                font_size="xs",
                _light={"color": "black"},
                _dark={"color": "white"}
            )
        ]
