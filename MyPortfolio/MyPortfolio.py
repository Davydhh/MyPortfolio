from rxconfig import config

import reflex as rx
from .components import header, footer
from .pages import home
from .states.state import State
from .style import style
from .states.state import AlertDialogState


def show_alert():
    return rx.alert_dialog(
            rx.alert_dialog_overlay(
                rx.alert_dialog_content(
                    rx.alert_dialog_header("Attention"),
                    rx.alert_dialog_body(
                        "Site still under development. At the moment the only page that can be viewed is the current one (Home)"
                    ),
                    rx.alert_dialog_footer(
                        rx.button(
                            "Ok",
                            on_click=AlertDialogState.change,
                        )
                    )
                )
            ),
            is_open=AlertDialogState.is_alert_open
        )
    


def build_page(body: rx.Vstack):
    navbar: rx.Hstack = header.Header()
    footer_ui: rx.Hstack = footer.Footer()

    return rx.vstack(
        navbar,
        show_alert(),
        body,
        footer_ui,
        style=style.get("main")
    )


def home_page() -> rx.Component:
    body: rx.Vstack = home.Home()
    return build_page(body)


# Add state and page to the app.
app = rx.App(style=style.get("app"), state=State)
app.add_page(home_page, route="/", title="Davide.dev", on_load=AlertDialogState.change)
app.compile()