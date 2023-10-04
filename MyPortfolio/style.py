style: dict = {
    "app": {
        "_dark": {
            "bg": "#1f2028",
        },
        "_light": {
            "bg": "#fafafa",
        }
    },
    "main": {
        "width": "100%",
        "height": "100vh",
        "_dark": {
            "background": "radial-gradient(circle, rgba(255, 255, 255, 0.09) 1px, transparent 1px)",
            "background_size": "25px 25px"
        },
        "_light": {
            "background": "radial-gradient(circle, rgba(0, 0, 0, 0.35) 1px, transparent 1px)",
            "background_size": "25px 25px"
        },
        "@keyframes dots": {
            "0%": {"background_position": "0 0"},
            "100%": {"background_position": "40px 40px"}
        },
        "animation": "dots 4s linear infinite alternate-reverse both"

    },
    "header": {
        "_dark": {"bg": "#141518"},
        "_light": {"bg": "#ffffff"},
        "width": "100%",
        "height": "50px",
        "padding": [
            "0 1rem",
            "0 1rem",
            "0 1rem",
            "0 4em",
            "0 10rem"
        ],
        "transition": "all 400ms ease",
        "box_shadow": "0px 8px 16px 0px rgba(0,0,0,0.25)",
    },
    "header_buttons": {
        "_dark": {"color": "white"},
        "_light": {"color": "black"}
    },
    "content": {
        "width": "100%",
        "height": "inherit",
        "padding": "15rem 0rem",
        "align_items": "center",
        "justify_content": "start"
    },
    "footer": {
        "width": "100%",
        "height": "60px",
        "_dark": {"bg": "#141518"},
        "_light": {"bg": "#ffffff"},
        "box_shadow": "0px 8px 16px 0px rgba(0,0,0,0.25)",
        "justify_content": "center",
        "padding": [
            "0 1rem",
            "0 1rem",
            "0 1rem",
            "0 4em",
            "0 10rem"
        ]
    }
}

wave: dict = {
    "@keyframes wave": {
        "0%": {"transform": "rotate(25deg)"},
        "100%": {"transform": "rotate(-15deg)"}
    },
    "animation": "wave 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) infinite alternate-reverse both"
}
