import reflex as rx


def introduction_block():
    return rx.hstack(
        rx.vstack(
            rx.text(
                "HELLO, MY NAME IS",
                color="gray"
            ),
            rx.divider(
                width="30%",
                border_color="gray",
                border_width="1.5px"
            ),
            rx.heading(
                "Davide Cazzetta",
                margin_top="70px",
                color="black",
                size="3xl"
            ),
            rx.heading(
                "Backend Software Engineer",
                size="lg",
                margin_top="10px"
            ),
            rx.hstack(
                rx.icon(tag="email"),
                rx.text("davidepro@hotmail.it"),
                align_items="center",
                spacing="3",
                margin_top="70px"
            ),
            align_items="left"
        ),
        rx.image(
            src="foto_profilo.jpg",
            width="500px",
            height="auto",
            border_radius="500px 500px",
            box_shadow="base"
        ),
        spacing="10em"
    )


def build():
    return rx.vstack(
        introduction_block(),
        h="100vh",
        margin_top="200px"
    )
