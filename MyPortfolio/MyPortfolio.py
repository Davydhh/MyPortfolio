from rxconfig import config

import reflex as rx
from .components import header, footer
from .pages import content
from .states.state import State
from .style import style

def index() -> rx.Component:
    navbar: rx.Hstack = header.Header()
    body: rx.Vstack = content.Content()
    footer_ui: rx.Hstack = footer.Footer()

    return rx.vstack(
        navbar,
        body,
        footer_ui,
        style=style.get("main")
    )


# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index)
app.compile()
