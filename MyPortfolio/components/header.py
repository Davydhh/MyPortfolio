import reflex as rx
from ..style import style
from ..states.state import State
from ..utilities.utility import create_menu_item, create_header_button

class Header(rx.Hstack):
    menu_titles = ["Home", "About", "Projects", "Contact"]

    def __init__(self):
        super().__init__(style=style.get("header"))
        self.children = [
            rx.heading("Davide.dev", size="md"),
            rx.spacer(),
            rx.tablet_and_desktop(
                rx.foreach(self.menu_titles, create_header_button)
            ),
            rx.color_mode_button(
                rx.color_mode_icon(),
                color_scheme="none",
                _dark={"color": "white"},
                _light={"color": "black"},
            ),
            rx.mobile_only(
                rx.menu(
                    rx.menu_button(
                        rx.cond(
                            State.is_menu_open,
                            rx.icon(tag="close"),
                            rx.icon(tag="hamburger")
                        ),
                        color_scheme="none",
                        _dark={"filter": "brightness(0) invert(1)"}
                    ),
                    rx.menu_list(
                        rx.foreach(self.menu_titles, create_menu_item),
                        style=style.get("app")
                    ),
                    auto_select=False,
                    on_close=State.toggle_menu,
                    on_open=State.toggle_menu
                )
            )
        ]
