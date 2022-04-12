[![GitHub release](https://img.shields.io/github/v/release/sansanlatulipe/script.service.hyperion-instance.svg)](https://github.com/sansanlatulipe/script.service.hyperion-instance/releases)
[![Integration](https://github.com/sansanlatulipe/script.service.hyperion-instance/workflows/Integration/badge.svg)](https://github.com/sansanlatulipe/script.service.hyperion-instance/actions/workflows/integration.yml)
[![Codecov status](https://img.shields.io/codecov/c/github/sansanlatulipe/script.service.hyperion-instance/main)](https://codecov.io/gh/sansanlatulipe/script.service.hyperion-instance/branch/main)

# Hyperion instance switcher

This project is a service addon for Kodi media center.
It automatically turns a Hyperion LED instance on when a video is playing and turn it off otherwise.

## Features

* Automatically switch the LED instance while playing a video
* Manually switch the managed LED instance
* Handle local or distant hosted Hyperion
* Authentication through access token

### To do

* Select the Hyperion LED instance to manage

## How it works

### Business logic

Monitor the Kodi player.
When it starts playing a medium, if it is a video then asks Hyperion to turn on the managed LED instance on.
When it stops playing the medium, asks Hyperion to turn the managed LED instance off.

The Hyperion managed LED instance can be selected from the add-on settings.

### Technical logic

The add-on is launched from `service.py`.

Except for the entry point, all code can be found in the directory `resources/lib/`:
* `launcher.py`: launcher functions
* `util/`: some helper classes and functions
* `service/`: business logic
* `infra/`: technical logic, like connection to API or backward compatibily
* `adapter/`: glue between `service/` and `infra/`
