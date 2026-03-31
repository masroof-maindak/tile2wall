# Tile2Wall

Quick Python script to convert any\* image into a tiled wallpaper.

<p align="center">
  <img alt="Dragon New Warm Mountain I Believe in You" src="https://github.com/user-attachments/assets/f509d1a7-f47d-491e-9245-4502d1604743" height="254">
  <img alt="out.png" src="https://github.com/user-attachments/assets/bd4afbf5-406a-4459-ac37-02b6442844d3" height="254">
</p>

_\*Given that its dimensions are smaller than those of the output image._

## Installation

```bash
git clone https://github.com/masroof-maindak/tile2wall.git && cd tile2wall
uv tool install .

# Alternatively:

uv tool install https://github.com/masroof-maindak/tile2wall.git
```

## Usage

```bash
tile2wall <img-path> # or `uv run main.py` during dev.

# `-h` to see supported args.
```

## TODO

- [ ] Set user's screen resolution as default output dimensions
