from rxconfig import config

import reflex as rx
from .components import header, footer
from .pages import home
from .style import style


def build_page(body: rx.Vstack):
    navbar: rx.Hstack = header.Header()
    footer_ui: rx.Hstack = footer.Footer()

    return rx.vstack(
        navbar,
        rx.text(
            "Site still under development. At the moment the only page that can be viewed is the current one (Home)",
            color="gray",
            font_size="0.8rem",
            padding_top="55px",
            padding_left="0.5rem",
            padding_right="0.5rem",
            text_align="center"
        ),
        body,
        footer_ui,
        style=style.get("main")
    )


def home_page() -> rx.Component:
    body: rx.Vstack = home.Home()
    return build_page(body)


# Add state and page to the app.
app = rx.App(style=style.get("app"))
app.add_page(home_page, route="/", title="Davide.dev")
app.compile()
