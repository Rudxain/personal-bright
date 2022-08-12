#!/usr/bin/env python3
from typing import Final
import sys
import time
import screen_brightness_control as sbc
import numpy as np
import cv2

def u8_to_percent(b: int) -> float:
	return b / 0xff * 100

def mean_light(img: np.ndarray) -> float:
	return sum(cv2.mean(img)) / 3

def take_photo() -> np.ndarray:
	cam = cv2.VideoCapture(0)

	#set resolution to the min possible (varies with device)
	#for general perfomance (time, energy, and memory)
	cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1)
	cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1)

	_, img = cam.read()
	cam.release()
	return img

#this increases versatility by taking args from either CLI or script
def main(*args: str):
	DEFAULT_T: Final = 3.0

	HELP_TXT: Final = f'usage: {args[0]} [period={DEFAULT_T}]\n`period` is the sample-interval in seconds'

	if '-h' in args or '--help' in args:
		print(HELP_TXT)
		return HELP_TXT

	period = float(args[1]) if len(args) > 1 else DEFAULT_T

	light_map = [u8_to_percent(b) for b in range(0x100)]

	ambient_old = None
	while True:
		ambient_new = round(mean_light(take_photo()))

		#save energy and time
		if ambient_old != ambient_new:
			ambient_old = ambient_new
			sbc.fade_brightness(finish=light_map[ambient_new], blocking=True, display=0)
		time.sleep(period)

if __name__=='__main__':
	main(*sys.argv)
