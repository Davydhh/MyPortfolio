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
        width=["29px", "32px", "32px", "36px", "36px"],
        height="auto"
    )


def create_xs_heading(title: str):
    return rx.heading(
        title,
        size="xs"
    )


def project_image_desktop(path: str):
    return rx.image(
        src=path,
        width=["200px", "250px", "350px", "350px", "350px"],
        height="auto",
        box_shadow="xl",
        border_radius="15px 15px",
        transition="all 300ms ease"
    )
def project_image_mobile(path: str):
    return rx.image(
        src=path,
        width="340px",
        height="auto",
        box_shadow="xl",
        border_radius="15px 15px",
        transition="all 300ms ease"
    )
