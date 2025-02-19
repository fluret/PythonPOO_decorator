from dataclasses import dataclass

@dataclass
class ThreeDPoint:
    x: int | float
    y = 0.0
    z: int | float = 0.0

    # ...