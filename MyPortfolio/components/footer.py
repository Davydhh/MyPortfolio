import os
import reflex as rx
from ..style import style
from ..utilities.yaml_reader import read_yaml


configuration = read_yaml(os.getcwd() + "/configuration.yaml")

class Footer(rx.Hstack):
    def __init__(self):
        super().__init__(style=style.get("footer"))
        self.children = [
            rx.text(
                configuration["footer"]["copyright"],
                font_size="xs",
                _light={"color": "black"},
                _dark={"color": "white"}
            )
        ]
