import os
import reflex as rx

from ..style import style, wave
from ..utilities.utility import create_badge, create_breadcrumb_item, create_stach_image, create_xs_heading, project_image_desktop, project_image_mobile, create_text_with_left_image
from ..utilities.yaml_reader import read_yaml

configuration = read_yaml(os.getcwd() + "/configuration.yaml")


class Home(rx.Vstack):
    page_configuration = configuration["content_page"]
    card_titles: list = page_configuration["card_titles"]
    workout_project = configuration["projects"][0]
    covid_project = configuration["projects"][1]
    location_contact = configuration["contact_block"][0]
    mail_contact = configuration["contact_block"][1]

    images_paths: list = ["/java.png", "/python.png",
                          "/spring-boot.png", "/postgresql.png", "/mongodb.png"]

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
            self.projects_block_desktop(),
            self.projects_block_mobile(),
            self.contact_block_desktop(),
            self.contact_block_mobile()
        ]

    def about_me_block_mobile(self):
        return rx.mobile_only(
            rx.container(
                rx.vstack(
                    rx.heading(
                        self.page_configuration["about_me"],
                        size="sm",
                        font_weight="900",
                        _dark={
                            "background": "linear-gradient(to right, #e1e1e1, #757575)",
                            "background_clip": "text"
                        },
                        _light={
                            "color": "#0277BD"
                        }
                    ),
                    rx.heading(
                        self.page_configuration["short_description"],
                        size="md",
                        text_align="center"
                    ),
                    rx.image(
                        src="/pc_desk.jpg",
                        width="340px",
                        height="auto",
                        box_shadow="xl",
                        border_radius="15px 15px"
                    ),
                    rx.text(
                        self.page_configuration["medium_description"],
                        size="xs",
                        text_align="justify",
                        max_w="330px"
                    ),
                    spacing="1.5rem",
                    align_items="center",
                    justify_content="center"
                ),
                margin_top="11rem",
                padding=["0 1.5rem"]
            ),
            id="about_mobile"
        )

    def about_me_block_desktop(self):
        return rx.tablet_and_desktop(
            rx.hstack(
                rx.image(
                    src="/pc_desk.jpg",
                    width=["200px", "250px", "300px", "300px", "300px"],
                    height="auto",
                    box_shadow="xl",
                    border_radius="15px 15px",
                    transition="all 300ms ease"
                ),
                rx.box(
                    rx.vstack(
                        rx.heading(
                            self.page_configuration["about_me"],
                            size="sm",
                            font_weight="900",
                            _dark={
                                "background": "linear-gradient(to right, #e1e1e1, #757575)",
                                "background_clip": "text"
                            },
                            _light={
                                "color": "#0277BD"
                            }
                        ),
                        rx.heading(
                            self.page_configuration["short_description"],
                            size="md"
                        ),
                        rx.text(
                            self.page_configuration["medium_description"],
                            size="xs"
                        ),
                        justify_content="left",
                        align_items="start"
                    ),
                    max_w="350px"
                ),
                margin_top="13rem",
                spacing="3rem",
                padding=["0 1.5rem"]
            ),
            id="about"
        )

    def tech_stack_mobile(self):
        return rx.mobile_only(
            rx.hstack(
                rx.heading(
                    self.page_configuration["tech_stack"],
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
                    rx.foreach(self.images_paths, create_stach_image),
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
                    self.page_configuration["tech_stack"],
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
                    rx.foreach(self.images_paths, create_stach_image),
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
                self.page_configuration["hello"],
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
                        self.page_configuration["projects"],
                        size="sm",
                        font_weight="900",
                        _dark={
                            "background": "linear-gradient(to right, #e1e1e1, #757575)",
                            "background_clip": "text"
                        },
                        _light={
                            "color": "#0277BD"
                        }
                    ),
                    rx.heading(
                        self.page_configuration["projects_introduction"],
                        size="md"
                    ),
                    spacing="1.5rem",
                    align_items="left",
                    justify_content="left"
                ),
                rx.vstack(
                    self.project_block_desktop(self.workout_project["name"], self.workout_project["description"], self.workout_project["technologies"],
                                               self.workout_project["github"], self.workout_project["live_demo"], self.workout_project["image_path"], self.workout_project["period"]),
                    self.project_block_desktop(self.covid_project["name"], self.covid_project["description"], self.covid_project["technologies"],
                                               self.covid_project["github"], self.covid_project["live_demo"], self.covid_project["image_path"], self.covid_project["period"], image_left=False),
                    spacing="4rem"
                ),
                margin_top="13rem",
                padding=["0 1.5rem"],
                spacing="3rem",
                align_items="stretch"
            ),
            id="projects"
        )

    def project_block_desktop(self, title: str, description: str, stack: list, github_link: str, demo_link: str, image_path: str, period: str, image_left: bool = True):
        if image_left:
            return rx.hstack(
                project_image_desktop(image_path),
                self.project_description_desktop(
                    title, description, stack, github_link, demo_link, period),
                spacing="4rem"
            )
        else:
            return rx.hstack(
                self.project_description_desktop(
                    title, description, stack, github_link, demo_link, period),
                project_image_desktop(image_path),
                spacing="4rem"
            )

    def project_description_desktop(self, title: str, description: str, stack: list, github_link: str, demo_link: str, period: str):
        return rx.vstack(
            rx.vstack(
                rx.heading(
                    title,
                    size="sm"
                ),
                rx.heading(
                    period,
                    size="xs",
                    color="gray"
                ),
                spacing="0.5rem"
            ),
            rx.text(
                description,
                size="xs",
                text_align="center"
            ),
            rx.hstack(
                rx.foreach(stack, create_xs_heading),
                spacing="2rem"
            ),
            rx.hstack(
                rx.link(
                    rx.image(
                        src="/github.png",
                        width=["20px", "22px",
                               "24px", "24px", "24px"],
                        _dark={
                            "filter": "brightness(0) invert(1)"},
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
                            width=["20px", "22px",
                                   "24px", "24px", "24px"],
                            transition="all 300ms ease"
                        ),
                        color_scheme="none",
                        _dark={"color": "white"},
                        _light={"color": "black"},
                        variant="link"
                    ),
                    href=demo_link
                ),
                spacing="2rem"
            ),
            max_w="400px",
            spacing="1rem"
        )

    def projects_block_mobile(self):
        return rx.mobile_only(
            rx.vstack(
                rx.vstack(
                    rx.heading(
                        self.page_configuration["projects"],
                        size="sm",
                        font_weight="900",
                        _dark={
                            "background": "linear-gradient(to right, #e1e1e1, #757575)",
                            "background_clip": "text"
                        },
                        _light={
                            "color": "#0277BD"
                        }
                    ),
                    rx.heading(
                        self.page_configuration["projects_introduction"],
                        size="md"
                    ),
                    spacing="1.5rem",
                    align_items="left",
                    justify_content="left",
                ),
                rx.vstack(
                    self.project_block_mobile(self.workout_project["name"], self.workout_project["description"], self.workout_project["technologies"],
                                              self.workout_project["github"], self.workout_project["live_demo"], self.workout_project["image_path"]),
                    self.project_block_mobile(self.covid_project["name"], self.covid_project["description"], self.covid_project["technologies"],
                                              self.covid_project["github"], self.covid_project["live_demo"], self.covid_project["image_path"]),
                    spacing="4rem"
                ),
                margin_top="11rem",
                padding=["0 1.5rem"],
                spacing="3rem",
                align_items="stretch"
            ),
            id="projects_mobile"
        )

    def project_block_mobile(self, title: str, description: str, stack: list, github_link: str, demo_link: str, image_path: str):
        return rx.vstack(
            rx.heading(
                title,
                size="sm"
            ),
            project_image_mobile(image_path),
            rx.text(
                description,
                size="xs",
                text_align="center"
            ),
            rx.hstack(
                rx.foreach(stack, create_xs_heading),
                spacing="2rem"
            ),
            rx.hstack(
                rx.link(
                    rx.image(
                        src="/github.png",
                        width="20px",
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
                            width="20px",
                            transition="all 300ms ease"
                        ),
                        color_scheme="none",
                        _dark={"color": "white"},
                        _light={"color": "black"},
                        variant="link"
                    ),
                    href=demo_link
                ),
                spacing="2rem"
            ),
            max_w="340px",
            spacing="1rem"
        )

    def contact_block_desktop(self):
        return rx.tablet_and_desktop(
            rx.vstack(
                rx.vstack(
                    rx.heading(
                        self.page_configuration["contact"],
                        size="sm",
                        font_weight="900",
                        _dark={
                            "background": "linear-gradient(to right, #e1e1e1, #757575)",
                            "background_clip": "text"
                        },
                        _light={
                            "color": "#0277BD"
                        }
                    ),
                    rx.heading(
                        self.page_configuration["contact_description"],
                        size="md"
                    ),
                    spacing="1.5rem"
                ),
                rx.hstack(
                    create_text_with_left_image(
                        self.location_contact["link"], self.location_contact["image_path"]),
                    create_text_with_left_image(
                        self.mail_contact["link"], self.mail_contact["image_path"]),
                    spacing="5rem"
                ),
                margin_top="13rem",
                padding=["0 1.5rem"],
                spacing="3rem",
                align_items="stretch"
            ),
            id="contact"
        )

    def contact_block_mobile(self):
        return rx.mobile_only(
            rx.vstack(
                rx.vstack(
                    rx.heading(
                        self.page_configuration["contact"],
                        size="sm",
                        font_weight="900",
                        _dark={
                            "background": "linear-gradient(to right, #e1e1e1, #757575)",
                            "background_clip": "text"
                        },
                        _light={
                            "color": "#0277BD"
                        }
                    ),
                    rx.heading(
                        self.page_configuration["contact_description"],
                        size="md"
                    ),
                    spacing="1.5rem"
                ),
                rx.vstack(
                    create_text_with_left_image(
                        self.location_contact["link"], self.location_contact["image_path"]),
                    create_text_with_left_image(
                        self.mail_contact["link"], self.mail_contact["image_path"]),
                    spacing="3rem"
                ),
                margin_top="13rem",
                padding=["0 1.5rem"],
                spacing="3rem",
                align_items="stretch"
            ),
            id="contact_mobile"
        )
