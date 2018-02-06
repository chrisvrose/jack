#!/usr/bin/env python3
import messages

def main():
	try:
		messages.main()
	except KeyboardInterrupt:
		print("OOPS")
