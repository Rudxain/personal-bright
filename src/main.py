#!/usr/bin/env python3
from typing import Final
from sys import argv
from time import sleep as zz
from screen_brightness_control import fade_brightness
from numpy import ndarray as nda
import cv2


def u8_to_percent(b: int):
	'''convert a byte into its corresponding ratio, then scale by a factor of a hundred'''
	return b / 0xff * 100


def take_lil_photo() -> nda:
	'''capture 1 frame from main cam with minimum resolution'''
	cam = cv2.VideoCapture(0)

	# set resolution to the min possible (varies with device)
	# for general perfomance (time, energy, and memory)
	cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1)
	cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1)

	_, img = cam.read()
	cam.release()
	return img


def main(*args: str):  # this increases versatility by taking args from either CLI or script
	DEFAULT_T: Final = 3.0

	HELP_TXT: Final = f'usage: {args[0]} [period={DEFAULT_T}]\n`period` is the sample-interval in seconds'

	if '-h' in args or '--help' in args:
		print(HELP_TXT)
		return HELP_TXT

	period = float(args[1]) if len(args) > 1 else DEFAULT_T

	# despite `u8_to_percent` being efficient,
	# the negligible memory use of this `list` is worth the eager-memoization,
	light_map = [u8_to_percent(b) for b in range(0x100)]

	ambient_old = None
	while True:
		ambient_new = take_lil_photo().max()

		# save energy and time
		if ambient_old != ambient_new:
			ambient_old = ambient_new
			fade_brightness(
				finish=light_map[ambient_new], blocking=True, display=0)
		zz(period)


if __name__ == '__main__':
	main(*argv)
