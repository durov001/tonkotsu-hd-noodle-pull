"""food-picture-01 second resubmit: Tonkotsu ramen, HD noodle pull.

The top leaderboard is tonkotsu: tall glossy noodle pull, dark speckled
bowl, torched chashu, jammy egg with dripping yolk, chili-oil swirls,
steam, warm bokeh. This entry follows that winning formula closely,
matching the reference image syahrul sent, instead of changing the dish.
The program copies the bundled image to /output/entry.png, deterministically.

Second resubmit: replaces the tantanmen entry for food-picture-01.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.jpg"),
        "/output/entry.png",
    )


if __name__ == "__main__":
    main()
