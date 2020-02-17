#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import cv2 as cv

from cvfpscalc import CvFpsCalc


def main():
    fps = 15
    cap = cv.VideoCapture(0)

    # create CvFpsCalc instance
    cvFpsCalc = CvFpsCalc()

    while True:
        start_time = time.time()

        # calculate fps
        fps_result = cvFpsCalc.get()
        print("fps:" + str(fps_result))

        ret, frame = cap.read()
        if not ret:
            continue

        cv.imshow(' ', frame)
        k = cv.waitKey(1) & 0xff
        if k == 27:  # ESC
            break

        elapsed_time = time.time() - start_time
        sleep_time = max(0, ((1.0 / fps) - elapsed_time))
        time.sleep(sleep_time)

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
