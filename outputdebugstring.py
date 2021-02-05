#! /usr/bin/python

import ctypes

OutputDebugString = ctypes.windll.kernel32.OutputDebugStringW

def olog(msg):
	OutputDebugString(format(msg))
