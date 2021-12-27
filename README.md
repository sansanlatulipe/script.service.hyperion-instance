Introduction
============

This service automatically turn on a Hyperion instance when a video is playing and turn it off otherwise

Features
========

* Local or distant Hyperion
* Authentication through access token (optional)
* Select an instance to control
* Manually switch the instance
* Automatically switch the instance while playing a movie

How it works
============

Business logic
--------------

### Movie synchronization

#### First scan or full rescan

For each movie stored in the Kodi library, if it is flagged as watched on either side (Kodi or Betaseries), ensure it is true on the other as well.

#### Complementary scans

Firstly, for each updates registered in Kodi (watched or unwatched), duplicate it on Betaseries.
Secondly, for each updates in Betaseries timeline (watched or unwatched), duplicate it on Kodi.

Technical logic
---------------

### Entry point

The add-on is launched from `service.py`.

### Structure

Except for the entry points, all code can be found in the directory `resources/lib/`:
* `launcher.py`: launcher functions
* `util/`: some helper classes and functions
* `service/`: business logic
* `infra/`: technical logic, like connection to API or backward compatibily
* `adapter/`: glue between `service/` and `infra/`
