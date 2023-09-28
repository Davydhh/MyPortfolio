import reflex as rx
from MyPortfolio.style import style


class Footer(rx.Hstack):
    def __init__(self):
        super().__init__(style=style.get("footer"))
        self.children = [
            rx.text(
                "Created with Reflex",
                _light={"color": "black"},
                _dark={"color": "white"}
            ),
            rx.spacer(),
            rx.image(
                src="/github.png",
                html_height="26px",
                html_width="26px",
                filter="brightness(0) invert(1)"
            )
        ]
