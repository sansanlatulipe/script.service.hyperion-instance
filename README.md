# Hyperion instance switcher

[![GitHub release](https://img.shields.io/github/v/release/sansanlatulipe/script.service.hyperion-instance.svg)](https://github.com/sansanlatulipe/script.service.hyperion-instance/releases)
[![Integration](https://github.com/sansanlatulipe/script.service.hyperion-instance/workflows/Integration/badge.svg)](https://github.com/sansanlatulipe/script.service.hyperion-instance/actions/workflows/integration.yml)
[![Codecov status](https://img.shields.io/codecov/c/github/sansanlatulipe/script.service.hyperion-instance/main)](https://codecov.io/gh/sansanlatulipe/script.service.hyperion-instance/branch/main)

This project is a service addon for Kodi media center.
It automatically turns a Hyperion LED instance on when a video is playing and turn it off otherwise.

## Features

- Automatically switch the LED instance while playing a video
- Select the Hyperion LED instance to manage
- Manually switch the managed LED instance
- Handle local or distant hosted Hyperion
- Authentication through access token

## How it works

### Quick start

You need a Hyperion instance, with HTTP reachable from Kodi

1. Create authentication token on Hyperion
    a. Create a LED instance if it does not exist yet
        The default one cannot be switched off
    b. Enable "API Authentication" and "Local Admin API Authentication" from Network Services
    c. Save the changes
    d. Create a token from Token Management and copy the secret
        Be careful, you will not be able to retrieve it later
2. Connect to Hyperion
    a. Fill in the IP address and port in the addon settings
    b. Paste your token secret generated in the previous step
    c. Save the changes
3. Select the LED instance to manage
    a. Click the "Select" action from the addon settings
    b. Choose the LED instance you want to manage from the list
    c. Save the changes
    d. Test your configuration by clicking the "Switch" action from the addon settings

### Data protection

Your authentication token is store locally (in Kodi's addon data).

There is no third-party component (like a server) between your Kodi and Hyperion.

## How to contribute

### Technical logic

The add-on is launched from `service.py`.

Except for the entry point, all code can be found in the directory `resources/lib/`:
- `launcher.py`: launcher functions
- `util/`: some helper classes and functions
- `service/`: business logic
- `infra/`: technical logic, like connection to API or backward compatibily
- `adapter/`: glue between `service/` and `infra/`
