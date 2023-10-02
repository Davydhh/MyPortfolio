import reflex as rx
from MyPortfolio.style import style, wave


def create_badge(title):
    return rx.badge(
        title,
        variant="solid",
        padding=[
            "0.15rem 0.35rem",
            "0.15rem 0.35rem",
            "0.15rem 1rem",
            "0.15rem 1rem",
            "0.15rem 1rem"
        ]
    )


def create_breadcrumb_item(path: str, title: str, url: str):
    return rx.breadcrumb_item(
        rx.hstack(
            rx.image(
                src=path,
                html_width="24px",
                html_height="24px",
                _dark={"filter": "brightness(0) invert(1)"},
            ),
            rx.breadcrumb_link(
                title, 
                href=url,
                _dark={"color": "rgba(255, 255, 255, 0.7)"},
                font_size="sm"
            )
        )
    )


class Content(rx.Vstack):
    card_titles: list = ["Software Engineer", "Microservices Developer", "Java Developer"]

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
                create_breadcrumb_item("/github.png", "GitHub", "#"),
                create_breadcrumb_item("/linkedin.png", "Linkedin", "#")
            )
        ]