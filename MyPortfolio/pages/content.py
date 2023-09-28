import reflex as rx
from MyPortfolio.style import style

class Content(rx.Vstack):
    def __init__(self):
        super().__init__(style=style.get("content"))
        self.children = [
            rx.heading(
                "Static Site Content Area",
                size="2xl",
                transition="all 300ms ease"
            )
        ]