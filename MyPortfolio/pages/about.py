import os
import reflex as rx
from ..style import style
from ..utilities.yaml_reader import read_yaml

configuration = read_yaml(os.getcwd() + "/configuration.yaml")


class About(rx.Vstack):
    def __init__(self):
        super().__init__(style=style.get("about"))

        self.children = [
            self.block_desktop()
        ]

    def block_desktop(self):
        return rx.tablet_and_desktop(
            rx.vstack(
                rx.heading(
                    configuration["content_page"]["about_me"],
                    size="3xl",
                    transition="all 300ms ease",
                    font_weight="900",
                    _dark={
                        "background": "linear-gradient(to right, #e1e1e1, #757575)",
                        "background_clip": "text"
                    }
                ),
                rx.hstack(
                    rx.image(
                        src="/me.jpg",
                        width=["180px", "200px", "220px", "250px", "250px"],
                        height="auto",
                        box_shadow="xl",
                        border_radius="10px 10px",
                        transition="all 300ms ease"
                    ),
                    rx.vstack(
                        rx.tabs(
                            rx.tab_list(
                                rx.tab(
                                    "MY STORY",
                                    _selected={"_dark": {"color": "white"}, "_light": {
                                        "color": "black"}},
                                    color="gray",
                                    mr="10"),
                                rx.tab("EXPERIENCE",
                                       _selected={"_dark": {"color": "white"}, "_light": {
                                           "color": "black"}},
                                       color="gray",
                                       mr="10"),
                                rx.tab("EDUCATION",
                                       _selected={"_dark": {"color": "white"}, "_light": {
                                           "color": "black"}},
                                       color="gray")
                            ),
                            rx.tab_panels(
                                rx.tab_panel(
                                    rx.text("My Story")
                                ),
                                rx.tab_panel(
                                    rx.text("Experience")
                                ),
                                rx.tab_panel(
                                    rx.text("Education")
                                )
                            ),
                            variant="unstyled",
                            size="lg"
                        ),
                        spacing="2.5rem",
                    ),
                    spacing="2.5rem",
                    align_items="stretch"
                ),
                spacing="3rem",
                justify_content="center"
            )
        )
