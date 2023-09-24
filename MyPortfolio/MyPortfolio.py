from rxconfig import config

import reflex as rx
from .components import navbar
from .pages import home
from .states.state import State

def index() -> rx.Component:
    return rx.vstack(
        navbar.build(),
        home.build(),
        align_items="stretch",
        bg="#F6F8FA"    
    )


# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index)
app.compile()
