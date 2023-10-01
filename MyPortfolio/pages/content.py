import reflex as rx
from MyPortfolio.style import style


class Content(rx.Vstack):
    def __init__(self):
        super().__init__(style=style.get("content"))
        self.children = [
            rx.hstack(
                rx.heading(
                    "Hi - I'm Davide",
                    size="2xl",
                    transition="all 300ms ease",
                    font_weight="900",
                    _dark={
                        "background": "linear-gradient(to right, #e1e1e1, #757575)",
                        "background_clip": "text"
                    },
                ),
                rx.heading("👋🏼", size="2xl"),
                spacing="1.75rem"
            )
        ]
