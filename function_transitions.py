import cv2 as cv
import numpy as np

samples = 2

src1 = cv.imread("C:\\Users\\Studium\\Desktop\\LinuxLogo.jpg")
src2 = cv.imread("C:\\Users\\Studium\\Desktop\\WindowsLogo.jpg")

def calc_alpha(samples, current_value):
    start_value = 0.1
    end_value = 1.0
    step_value = (end_value-start_value) / (samples-1)
    return start_value + current_value * step_value 


def transitions(samples):
    i = 0

    while i < samples:
        alpha = calc_alpha(samples, i)
        beta = (1.0-alpha)
        dst = cv.addWeighted(src1, alpha, src2, beta, 0.0)
        cv.imshow('dst', dst)
        cv.waitKey(0)
        alpha += 0.1
        i += 1

transitions(samples)
