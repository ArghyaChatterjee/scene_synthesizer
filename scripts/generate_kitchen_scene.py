from scene_synthesizer import procedural_scenes as ps
import numpy as np

kitchen = ps.kitchen_island()
kitchen.label_support(
    label="support",
    min_area=0.05,
    gravity=np.array([0, 0, -1]),
)

kitchen.show_supports()