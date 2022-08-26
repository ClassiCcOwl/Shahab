import os
file_path = os.path.dirname(os.path.abspath(__file__))
req_path = os.path.join(file_path,"req.txt")
os.system("py -m ensurepip --upgrade")
os.system(f"pip install --upgrade --force-reinstall -r {req_path}")