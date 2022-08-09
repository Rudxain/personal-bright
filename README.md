# DISCLAIMER
This doesn't work yet! Please be patient.

BTW, this repo may **stop using Python at any time.** It may switch to Rust, or any other lang appropiate for the task.

# personal-bright
This is inspired by Android's "Adaptive Brightness" feature, which learns about the user's preferences at runtime, and adjusts display brightness accordingly based on ambient light.

This script is intended to run on devices with camera but no light sensors, because devices with light sensors will (probably) already have this feature.

It's intended to run on Linux, but it may also work on Windows.

This is an example of machine learning without artificial intelligence, because the script is a simple algorithm, not a neural net

# Usage
## Clone
- Using `git`:
```sh
git clone https://github.com/Rudxain/personal-bright.git
```
- Or [download the ZIP](https://github.com/Rudxain/personal-bright/archive/refs/heads/main.zip) from GH

## Run
- From CLI:
```sh
cd personal-bright/src/
./main.py [period=3]
```
- Or just open the file on Linux, and it will default to `period=3`
- Or import the file into another script, then call `main`

## Example
Set sampling interval to 5 seconds:
```sh
./main.py 5
```
