"""
Icons for mermaid diagrams
"""


class Icons:
    """
    Icons for IDAES flowsheet nodes.
    """

    # Map of class suffixes to idaes icons
    suffix_map = {
        "Feed": "feed",
        "Flash": "flash",
        "Heater": "heater",
        "Mixer": "mixer",
        "HeatExchanger": "heat-exchanger-1",
    }

    def __init__(self):
        self._smap = self.suffix_map

    def get_icon_for_class(self, class_name: str) -> str | None:
        """Get name of the IDAES icon for a given component class
        name.

        Returns: name, or None if no match is found
        """
        for k, v in self._smap.items():
            if class_name.endswith(k):
                return v
        return None
