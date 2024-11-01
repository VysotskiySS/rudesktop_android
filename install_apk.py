import uiautomator2 as u2
from config import *

d = u2.connect('emulator-5554')

d.app_install(app_link)