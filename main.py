import argparse
import os
import sys

import cv2
import numpy as np


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="input tile file")
    parser.add_argument(
        "-x", "--width", help="output img width", default=1080, type=int
    )
    parser.add_argument(
        "-y", "--height", help="output img height", default=1920, type=int
    )
    parser.add_argument("-o", "--output", help="output file name", default="out.png")
    args = parser.parse_args()

    if not os.path.isfile(args.image):
        print("[ERR] File doesn't exist.", file=sys.stderr)
        exit(1)

    img = cv2.imread(args.image, cv2.IMREAD_COLOR_BGR)
    if img is None:
        print("[ERR] Failed to read image.")
        exit(1)

    tile_h = img.shape[0]
    tile_w = img.shape[1]

    if args.height <= tile_h or args.width < tile_w:
        print("[ERR] Output dimensions are smaller than tile dimensions")
        exit(1)

    if args.height % tile_h != 0 or args.width % tile_w != 0:
        print("[WARN] Output dimensions aren't perfectly divisible by tile dimensions")

    out_img = cv2.Mat(np.zeros([args.height, args.width, 3], dtype=np.uint8))

    y = 0
    while y < args.height:
        x = 0
        while x < args.width:
            # TODO: copying logic -- cv2.Rect() ?

            x += tile_w
        y += tile_h

    cv2.imwrite(args.output, out_img)
    print("[INFO] Saved", args.output, "w/ shape", out_img.shape)


if __name__ == "__main__":
    main()
