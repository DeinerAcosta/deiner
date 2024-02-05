import os
import zipfile

os.chdir("C:\Users\laura bornacelli\Desktop\CDE")

with zipfile.ZipFile("comprimir.zip", "w")as fzip:
    fzip.write("there is and there are.pdf")