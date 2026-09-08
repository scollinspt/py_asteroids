# Py Asteroids

A retro Asteroids game built with Python and Pygame. This project began as the
Asteroids guided project on [Boot.dev](https://www.boot.dev/) and is being
extended beyond the course requirements.

## Extensions

The current version adds:

- A score display that awards points for destroying asteroids
- Level progression based on score
- Asteroids that move faster as the level increases
- Immediate speed increases for asteroids already on screen
- An HTML5 build that runs in a web browser and can be published on itch.io

## Controls

| Key | Action |
| --- | --- |
| `W` | Move forward |
| `S` | Move backward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Space` | Shoot |

## Setup

Requirements:

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/)

Clone the repository and install the locked dependencies:

```sh
git clone https://github.com/scollinspt/py_asteroids.git
cd py_asteroids
uv sync
```

## Run Locally

```sh
uv run main.py
```

## Build for Itch.io

Create a fresh HTML5 archive after changing the game:

```sh
uv run python -m pygbag --archive main.py
```

The upload-ready file is `build/web.zip`. On itch.io, create an HTML project,
upload that ZIP, and select **This file will be played in the browser**. Replace
the uploaded ZIP with a newly generated one whenever the game is updated.

## Roadmap

- Add sound effects and music
- Add momentum-based spacecraft physics so acceleration changes velocity and
	the craft continues drifting after the thrust key is released
