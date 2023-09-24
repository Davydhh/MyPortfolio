import reflex as rx

def build():
    return rx.vstack(
        rx.spacer(),
        rx.hstack(
            rx.vstack(
                rx.text(
                    "HELLO, MY NAME IS",
                    color="gray"
                ),
                rx.divider(
                    width="25%"
                )   
            ),
            rx.image(
                src="foto_profilo.jpg",
                width="400px",
                height="400px",
                border_radius="500px 500px",
                box_shadow="base"
                )
        )
    )