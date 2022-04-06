import subprocess
import sys
import pip


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

#canvas1 = tk.Canvas(root, width = 300, height = 300)
#canvas1.pack()
install('keytotext==1.5.2')
install('pandas==0.25.3')


