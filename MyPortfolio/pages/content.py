import reflex as rx
from ..style import style, wave
from ..utilities.utility import create_badge, create_breadcrumb_item, create_stach_image, create_xs_heading
from ..states.state import State


class Content(rx.Vstack):
    card_titles: list = ["Software Engineer",
                         "Microservices Developer", "Java Developer"]

    workout_project_description: str = "WorkoutTracker is a Fitness App that allows you to stop having to keep track of the repetitions of each exercise since it will do it for you, through the Augmented Reality and Computer Vision. But that's not all it does, as it memorizes the order of the exercises and, as soon as you have finished performing all the repetitions for one exercise, it will remind you which one is next."

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
            self.about_me_block_mobile(),
            self.projects_block_desktop()
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
                    width=["150px", "200px", "250px", "250px", "250px"],
                    height="auto",
                    box_shadow="xl",
                    border_radius="15px 15px",
                    transition="all 300ms ease"
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
                margin_top="15rem",
                spacing="3rem",
                align_items="stretch",
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
                "/linkedin.png", "Linkedin", "https://www.linkedin.com/in/davide-cazzetta-3a86a9198")
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

    def projects_block_desktop(self):
        return rx.tablet_and_desktop(
            rx.vstack(
                rx.vstack(
                    rx.heading(
                        "PROJECTS",
                        size="xs",
                        font_weight="900",
                        _dark={
                            "background": "linear-gradient(to right, #e1e1e1, #757575)",
                            "background_clip": "text"
                        }
                    ),
                    rx.heading(
                        "One personal and one university project 💻",
                        size="md"
                    ),
                    spacing="1.5rem",
                    align_items="left",
                    justify_content="left",
                ),
                rx.hstack(
                    rx.image(
                        src="/workout.jpg",
                        width=["200px", "250px", "350px", "350px", "350px"],
                        height="auto",
                        box_shadow="xl",
                        border_radius="15px 15px",
                        transition="all 300ms ease"
                    ),
                    self.project_description_desktop("WORKOUT TRACKER 🏋🏻", self.workout_project_description, ["iOS", "Swift", "SwiftUI"], "/github.png", "https://github.com/Davydhh/WorkoutTracker", "https://youtube.com/shorts/pQXOGQ_unDc?si=jk1EsxEdMWbwd8kX"),
                    spacing="4rem"
                ),
                margin_top="15rem",
                padding=["0 1.5rem"],
                spacing="3rem",
                align_items="stretch"
            )
        )

    def project_description_desktop(self, title: str, description: str, stack: list, image_path: str, github_link: str, demo_link: str):
        return rx.vstack(
                        rx.heading(
                            title,
                            size="sm"
                        ),
                        rx.text(
                            description,
                            font_size="0.8rem",
                            text_align="center"
                        ),
                        rx.hstack(
                            rx.foreach(stack, create_xs_heading),
                            spacing="2rem"
                        ),
                        rx.hstack(
                            rx.link(
                                rx.image(
                                    src=image_path,
                                    width=["20px", "22px",
                                           "24px", "24px", "24px"],
                                    _dark={"filter": "brightness(0) invert(1)"},
                                    transition="all 300ms ease"
                                ),
                                href=github_link
                            ),
                            rx.link(
                                rx.button(
                                    "Live Demo",
                                    rx.icon(
                                        tag="external_link",
                                        padding_left="0.5rem",
                                        width=["20px", "22px", "24px", "24px", "24px"],
                                        transition="all 300ms ease"
                                    ),
                                    icon_spacing=10,
                                    color_scheme="none",
                                    _dark={"color": "white"},
                                    _light={"color": "black"},
                                    variant="link"
                                ),
                                href=demo_link
                            ),
                            spacing="2rem"
                        ),
                        max_w="350px",
                        spacing="1rem"
                    )
