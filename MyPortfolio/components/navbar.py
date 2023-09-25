import reflex as rx


def build():
    return rx.flex(
        rx.text(
            "Davide",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
            font_weight="bold",
            font_size="2em",
            margin_left="5em"
        ),
        rx.spacer(),
        rx.hstack(
            rx.button(
                "HOME",
                bg="#F6F8FA",
                _hover={"color": "gray"}
            ),
            rx.button(
                "ABOUT",
                bg="#F6F8FA",
                _hover={"color": "gray"}
            ),
            rx.button(
                "PROJECTS",
                bg="#F6F8FA",
                _hover={"color": "gray"}
            ),
            rx.button(
                "CONTACT",
                bg='#F6F8FA',
                _hover={"color": "gray"}
            ),
            margin_right="5em"
        ),
        width="100%",
        padding="3",
        align_items="center",
        boxShadow="xl",
        backdrop_filter="auto",
        backdrop_blur="lg"
    )
