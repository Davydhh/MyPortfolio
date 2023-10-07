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
            rx.hstack(
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
            ),
            rx.tablet_and_desktop(
                rx.hstack(
                    rx.foreach(self.card_titles, create_badge),
                    spacing="1rem",
                    margin_top="0.5rem",
                    margin_bottom="0.5rem"
                )
            ),
            rx.mobile_only(
                rx.vstack(
                    rx.foreach(self.card_titles, create_badge),
                    spacing="1.25rem",
                    margin_top="1rem",
                    margin_bottom="1rem"
                )
            ),
            rx.breadcrumb(
                create_breadcrumb_item(
                    "/github.png", "GitHub", "https://github.com/Davydhh"),
                create_breadcrumb_item(
                    "/linkedin.png", "Linkedin", "https://www.linkedin.com/in/davide-cazzetta-3a86a9198"),
            ),
            rx.tablet_and_desktop(
                rx.hstack(
                    rx.heading(
                        "Tech Stack",
                        font_size=["1rem", "md", "xl", "xl", "xl"],
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
                    margin_top="10rem"
                )
            ),
            rx.mobile_only(
                rx.hstack(
                    rx.heading(
                        "Tech Stack",
                        font_size=["1rem", "md", "xl", "xl", "xl"],
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
                        spacing="1.5rem"
                    ),
                    spacing="1rem",
                    margin_top="10rem"
                )
            ),
            rx.tablet_and_desktop(
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
                                font_weight="700",
                            ),
                            rx.heading(
                                "A dedicated Back-end Developer based in Milan, Italy 📍",
                                size="md"
                            ),
                            rx.text(
                                "I'm a Software Engineer with expertise in Java, Microservices, Cloud Computing, and Edge Computing. I specialize in building secure, scalable, and cloud-native applications with Spring Boot and Docker. My experience with asynchronous technologies like RabbitMQ and Apache Kafka enables me to create resilient systems. I'm a collaborative team player known for my effective communication, adapting seamlessly to both Agile and Waterfall environments. My commitment to continuous learning ensures I deliver top-notch results for clients and stakeholders.",
                                font_size="0.8rem"
                            ),
                            justify_content="left",
                            align_items="start"
                        ),
                        max_w="350px"
                    ),
                    margin_top="11rem",
                    spacing="3rem",
                    align_items="start"
                )
            )
        ]
