import reflex as rx
from ..style import style


def create_menu_item(title: str):
    return rx.menu_item(
        title,
        style=style.get("app")
    )


def create_header_button(title: str):
    return rx.button(
        title,
        color_scheme="none",
        style=style.get("header_buttons")
    )


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
                html_width="20px",
                html_height="20px",
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

def create_stach_image(path: str):
    return rx.image(
        src=path,
        width=["29px", "36px", "36px", "36px", "36px"],
        height="auto"
    )