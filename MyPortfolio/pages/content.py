import reflex as rx
from MyPortfolio.style import style, wave

def create_badge(title):
        return rx.badge(
            title,
            variant="solid",
            padding=[
                "0.2rem 0.35rem",
                "0.2rem 0.35rem",
                "0.2rem 1rem",
                "0.2rem 1rem",
                "0.2rem 1rem"
            ]
        )

class Content(rx.Vstack):
    card_titles = ["Software Engineer", "Microservices Developer", "Java Developer"]

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
                rx.heading("👋🏼", size="2xl", style=wave),
                spacing="1.75rem"
            ),
            rx.tablet_and_desktop(
                rx.hstack(
                    rx.foreach(self.card_titles, create_badge),
                    spacing="1rem"
                )
            ),
            rx.mobile_only(
                rx.vstack(
                    rx.foreach(self.card_titles, create_badge),
                    spacing="1.25rem"
                )
            )
        ]
