# DISCLAIMER
This doesn't work yet! Please be patient

# personal-bright
This is inspired by Android's "Adaptive Brightness" feature, which learns about the user's preferences at runtime, and adjusts display brightness accordingly based on ambient light.

This script is intended to run on devices with camera but no light sensors, because devices with light sensors will (probably) already have this feature.

It's intended to run on Linux, but it may also work on Windows

# Usage
## Clone the repo
- Using `git`:
```sh
git clone https://github.com/Rudxain/personal-bright.git
```
- Or [download the ZIP](https://github.com/Rudxain/personal-bright/archive/refs/heads/main.zip) from GH

## Run it
- Run from CLI:
```sh
cd personal-bright
./personal-bright.py [period=3]
```
- Or just open the file on Linux, and it will default to `period=3`
- Or import the file into another script, then call `main`

Example. Set sampling interval to 5 seconds:
```sh
personal-bright.py 5
```
