import reflex as rx
from ..style import style, wave
from ..utilities.utility import create_badge, create_breadcrumb_item, create_stach_image
from ..states.state import State


class Content(rx.Vstack):
    card_titles: list = ["Software Engineer",
                         "Microservices Developer", "Java Developer"]

    def __init__(self):
        super().__init__(style=style.get("content"))

        self.children = [
            self.landing_block(),
            self.card_block_desktop(),
            self.card_block_mobile(),
            self.breadcrumb_block(),
            self.tech_stack_block(),
            self.tech_stack_mobile(),
            self.about_me_block_desktop(),
            self.about_me_block_mobile()
        ]

    def about_me_block_mobile(self):
        return rx.mobile_only(
                rx.container(
                    rx.vstack(
                        rx.heading(
                            "ABOUT ME",
                            size="xs",
                            font_weight="900",
                            _dark={
                                "background": "linear-gradient(to right, #e1e1e1, #757575)",
                                "background_clip": "text"
                            }
                        ),
                        rx.heading(
                            "A dedicated Back-end Developer based in Milan, Italy 📍",
                            size="md",
                            text_align="center"
                        ),
                        rx.image(
                            src="/pc_desk.jpg",
                            width="330px",
                            height="auto",
                            box_shadow="xl",
                            border_radius="15px 15px"
                        ),
                        rx.text(
                            "I'm a Software Engineer experienced in Java, Microservices, and Cloud Computing. Skilled in building secure, scalable applications with Spring Boot and Docker. Adaptable team player with strong communication, working well in Agile and Waterfall environments.",
                            font_size="0.8rem",
                            text_align="justify",
                            max_w="330px"
                        ),
                        spacing="1.5rem",
                        align_items="center",
                        justify_content="center"
                    ),
                    margin_top="11rem",
                    padding=["0 1.5rem"]
                )
            )

    def about_me_block_desktop(self):
        return rx.tablet_and_desktop(
                rx.hstack(
                    rx.image(
                        src="/pc_desk.jpg",
                        width="250px",
                        height="auto",
                        box_shadow="xl",
                        border_radius="15px 15px"
                    ),
                    rx.box(
                        rx.vstack(
                            rx.heading(
                                "ABOUT ME",
                                size="xs",
                                font_weight="900",
                                _dark={
                                    "background": "linear-gradient(to right, #e1e1e1, #757575)",
                                    "background_clip": "text"
                                }
                            ),
                            rx.heading(
                                "A dedicated Back-end Developer based in Milan, Italy 📍",
                                size="md"
                            ),
                            rx.text(
                                "I'm a Software Engineer experienced in Java, Microservices, and Cloud Computing. Skilled in building secure, scalable applications with Spring Boot and Docker. Adaptable team player with strong communication, working well in Agile and Waterfall environments.",
                                font_size="0.8rem"
                            ),
                            justify_content="left",
                            align_items="start"
                        ),
                        max_w="350px"
                    ),
                    margin_top="11rem",
                    spacing="3rem",
                    align_items="start",
                    padding=["0 1.5rem"]
                )
            )

    def tech_stack_mobile(self):
        return rx.mobile_only(
                rx.hstack(
                    rx.heading(
                        "Tech Stack",
                        size="1rem",
                        transition="all 300ms ease"
                    ),
                    rx.divider(
                        orientation="vertical",
                        height="2em",
                        border_color="rgba(255, 255, 255, 0.7)",
                        _light={"border_color": "black"}
                    ),
                    rx.hstack(
                        rx.foreach(State.images_paths, create_stach_image),
                        spacing="1rem"
                    ),
                    spacing="1rem",
                    margin_top="10rem",
                    padding=["0 1.5rem"]
                )
            )

    def tech_stack_block(self):
        return rx.tablet_and_desktop(
                rx.hstack(
                    rx.heading(
                        "Tech Stack",
                        size="md",
                        transition="all 300ms ease"
                    ),
                    rx.divider(
                        orientation="vertical",
                        height="2em",
                        border_color="rgba(255, 255, 255, 0.7)",
                        _light={"border_color": "black"}
                    ),
                    rx.hstack(
                        rx.foreach(State.images_paths, create_stach_image),
                        spacing="3rem"
                    ),
                    spacing="2rem",
                    margin_top="10rem",
                    padding=["0 1.5rem"]
                )
            )

    def breadcrumb_block(self):
        return rx.breadcrumb(
                create_breadcrumb_item(
                    "/github.png", "GitHub", "https://github.com/Davydhh"),
                create_breadcrumb_item(
                    "/linkedin.png", "Linkedin", "https://www.linkedin.com/in/davide-cazzetta-3a86a9198"),
            )

    def card_block_mobile(self):
        return rx.mobile_only(
                rx.vstack(
                    rx.foreach(self.card_titles, create_badge),
                    spacing="1.25rem",
                    margin_top="1rem",
                    margin_bottom="1rem"
                )
            )

    def card_block_desktop(self):
        return rx.tablet_and_desktop(
                rx.hstack(
                    rx.foreach(self.card_titles, create_badge),
                    spacing="1rem",
                    margin_top="0.5rem",
                    margin_bottom="0.5rem"
                )
            )

    def landing_block(self):
        return rx.hstack(
                rx.heading(
                    "Hi - I'm Davide",
                    size="2xl",
                    transition="all 300ms ease",
                    font_weight="900",
                    _dark={
                        "background": "linear-gradient(to right, #e1e1e1, #757575)",
                        "background_clip": "text"
                    }
                ),
                rx.heading("👋🏼", size="2xl", style=wave),
                spacing="1.75rem"
            )
