import os
import reflex as rx
from MyPortfolio.style import style
from MyPortfolio.utilities.utility import create_menu_item, create_header_button
from MyPortfolio.utilities.yaml_reader import read_yaml

configuration = read_yaml(os.getcwd() + "/configuration.yaml")


class Header(rx.Hstack):

    def __init__(self):
        super().__init__(style=style.get("header"))
        self.children = [
            rx.heading(configuration["header"]["title"], size="md"),
            rx.spacer(),
            rx.tablet_and_desktop(
                create_header_button("Home", "/"),
                create_header_button("About", "#about"),
                create_header_button("Projects", "#projects"),
                create_header_button("Contact", "#contact")
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
                        rx.icon(tag="hamburger"),
                        color_scheme="none",
                        _dark={"filter": "brightness(0) invert(1)"},
                        padding_left="0.8rem"
                    ),
                    rx.menu_list(
                        create_menu_item("Home", "#landing"),
                        create_menu_item("About", "#about"),
                        create_menu_item("Projects", "#projects"),
                        create_menu_item("Contact", "/contact"),
                        style=style.get("app")
                    ),
                    auto_select=False
                )
            )
        ]
