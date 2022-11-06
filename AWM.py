import platform

b = platform.architecture()[0]
import aw
if b == '64bit':

    import aw

elif b == '32bit':

    print("NOT SUPPORTED")


