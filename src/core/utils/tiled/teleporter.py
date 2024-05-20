from dataclasses import dataclass


@dataclass
class Teleporter:

    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str
