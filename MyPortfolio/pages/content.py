import reflex as rx
from ..style import style, wave
from ..utilities.utility import create_badge, create_breadcrumb_item


class Content(rx.Vstack):
    card_titles: list = ["Software Engineer",
                         "Microservices Developer", "Java Developer"]

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
                    }
                ),
                rx.heading("👋🏼", size="2xl", style=wave),
                spacing="1.75rem"
            ),
            rx.tablet_and_desktop(
                rx.hstack(
                    rx.foreach(self.card_titles, create_badge),
                    spacing="1rem",
                    margin_top="0.5rem",
                    margin_bottom="0.5rem"
                )
            ),
            rx.mobile_only(
                rx.vstack(
                    rx.foreach(self.card_titles, create_badge),
                    spacing="1.25rem",
                    margin_top="1rem",
                    margin_bottom="1rem"
                )
            ),
            rx.breadcrumb(
                create_breadcrumb_item(
                    "/github.png", "GitHub", "https://github.com/Davydhh"),
                create_breadcrumb_item(
                    "/linkedin.png", "Linkedin", "https://www.linkedin.com/in/davide-cazzetta-3a86a9198"),
            ),
            rx.hstack(
                rx.heading(
                    "Tech Stack",
                    font_size=["1rem", "md", "md", "md", "md"],
                    transition="all 300ms ease"
                ),
                rx.divider(
                    orientation="vertical",
                    border_color="rgba(255, 255, 255, 0.7)",
                    _light={"border_color": "black"}
                ),
                rx.hstack(
                    rx.image(
                        src="/java.png",
                        width=["30px", "36px", "36px", "36px", "36px"],
                        height="auto"
                    ),
                    rx.image(
                        src="/python.png",
                        width=["30px", "36px", "36px", "36px", "36px"],
                        height="auto"
                    ),
                    rx.image(
                        src="/spring-boot.png",
                        width=["30px", "36px", "36px", "36px", "36px"],
                        height="auto"
                    ),
                    rx.image(
                        src="/postgresql.png",
                        width=["30px", "36px", "36px", "36px", "36px"],
                        height="auto"
                    ),
                    rx.image(
                        src="/mongodb.png",
                        width=["30px", "36px", "36px", "36px", "36px"],
                        height="auto"
                    ),
                    spacing="6vw"
                ),
                spacing="4vw"
            )
        ]
