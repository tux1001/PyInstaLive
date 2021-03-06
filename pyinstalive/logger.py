import os
import sys
import re
from .settings import settings

sep = "-" * 70

def supports_color():
	try:
		"""
		from https://github.com/django/django/blob/master/django/core/management/color.py
		Return True if the running system's terminal supports color,
		and False otherwise.
		"""

		plat = sys.platform
		supported_platform = plat != 'Pocket PC' and (plat != 'win32' or 'ANSICON' in os.environ)

		# isatty is not always implemented, #6223.
		is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
		if not supported_platform or not is_a_tty:
			return "No", False
		return "Yes", True
	except Exception as e:
		print("Error while logging: {}" + str(e))



def log_seperator():
	try:
		print(sep)
		if settings.log_to_file == 'True':
			try:
				with open("pyinstalive{:s}.log".format("_" + settings.user_to_download if len(settings.user_to_download) > 0 else ".default"),"a+") as f:
					f.write(sep + '\n')
					f.close()
			except:
				pass
		sys.stdout.flush()
	except Exception as e:
		print("Error while logging: {}" + str(e))


def log_info_green(string):
	try:
		if supports_color()[1] == False:
			print(string)
		else:
			print('[\x1B[1;32;40mI\x1B[0m] {:s}\x1B[0m'.format(string))
		if settings.log_to_file == 'True':
			try:
				with open("pyinstalive{:s}.log".format("_" + settings.user_to_download if len(settings.user_to_download) > 0 else ".default"),"a+") as f:
					f.write("[I] {:s}\n".format(string))
					f.close()
			except:
				pass
		sys.stdout.flush()
	except Exception as e:
		print("Error while logging: {}" + str(e))


def log_info_blue(string):
	try:
		if supports_color()[1] == False:
			print(string)
		else:
			print('[\x1B[1;34;40mI\x1B[0m] {:s}\x1B[0m'.format(string))
		if settings.log_to_file == 'True':
			try:
				with open("pyinstalive{:s}.log".format("_" + settings.user_to_download if len(settings.user_to_download) > 0 else ".default"),"a+") as f:
					f.write("[I] {:s}\n".format(string))
					f.close()
			except:
				pass
		sys.stdout.flush()
	except Exception as e:
		print("Error while logging: {}" + str(e))


def log_warn(string):
	try:
		if supports_color()[1] == False:
			print(string)
		else:
			print('[\x1B[1;33;40mW\x1B[0m] {:s}\x1B[0m'.format(string))
		if settings.log_to_file == 'True':
			try:
				with open("pyinstalive{:s}.log".format("_" + settings.user_to_download if len(settings.user_to_download) > 0 else ".default"),"a+") as f:
					f.write("[W] {:s}\n".format(string))
					f.close()
			except:
				pass
		sys.stdout.flush()
	except Exception as e:
		print("Error while logging: {}" + str(e))


def log_error(string):
	try:
		if supports_color()[1] == False:
			print(string)
		else:
			print('[\x1B[1;31;40mE\x1B[0m] {:s}\x1B[0m'.format(string))
		if settings.log_to_file == 'True':
			try:
				with open("pyinstalive{:s}.log".format("_" + settings.user_to_download if len(settings.user_to_download) > 0 else ".default"),"a+") as f:
					f.write("[E] {:s}\n".format(string))
					f.close()
			except:
				pass
		sys.stdout.flush()
	except Exception as e:
		print("Error while logging: {}" + str(e))


def log_whiteline():
	try:
		print("")
		if settings.log_to_file == 'True':
			try:
				with open("pyinstalive{:s}.log".format("_" + settings.user_to_download if len(settings.user_to_download) > 0 else ".default"),"a+") as f:
					f.write("\n")
					f.close()
			except:
				pass
		sys.stdout.flush()
	except Exception as e:
		print("Error while logging: {}" + str(e))


def log_plain(string):
	try:
		print(string)
		if settings.log_to_file == 'True':
			try:
				with open("pyinstalive{:s}.log".format("_" + settings.user_to_download if len(settings.user_to_download) > 0 else ".default"),"a+") as f:
					f.write("{:s}\n".format(string))
					f.close()
			except:
				pass
		sys.stdout.flush()
	except Exception as e:
		print("Error while logging: {}" + str(e))