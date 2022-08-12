# personal-bright
This is inspired by Android's "Adaptive Brightness" feature, which learns about the user's preferences at runtime, and adjusts display brightness accordingly based on ambient light.

This is an example of machine learning without artificial intelligence, because the script is a simple algorithm, not a neural network.

# DISCLAIMER
This doesn't work as intended yet! Currently, it uses a hardcoded light-map, instead of learning user preferences. Please be patient.

BTW, this repo may **stop using Python at any time.** It may switch to Rust, or any other lang appropiate for the task.

# System requirements
## Hardware
- Camera. (no light-sensors required). Devices with light-sensors will (probably) already have a similar feature built-in.
- Display/screen. Read [SBC docs](https://crozzers.github.io/screen_brightness_control/extras/Installing%20On%20Linux.html) for more info.
## Software
- Any Debian-based GNU-Linux distro. It may work on Windows (not guaranteed).

# Usage
## Clone
- Using `git`:
```sh
git clone https://github.com/Rudxain/personal-bright.git
```
- Or [download the ZIP](https://github.com/Rudxain/personal-bright/archive/refs/heads/main.zip) from GH

> Installation instructions will be available in the future. This repo is not a valid Python package, it cannot be installed with PiP

## Run
- From CLI:
```sh
cd personal-bright/src/
./main.py [period=3]
```
- Or just open the file on Linux, and it will default to `period=3`
- Or import the file into another script, then call `main`

## Example
Run with a sampling interval of 5 seconds:
```sh
./main.py 5
```

# Privacy
As you can see in the source code, captured photos are not shared with 3rd-parties, and are taken with the lowest resolution that the driver accepts. No network access is performed. No storage access is performed. No environment variables are read/written. Photos are not accumulated, they are discarded immediately after calculating the average.

This means that memory-dumps are unlikely to contain sensitive data
