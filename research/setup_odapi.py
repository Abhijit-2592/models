"""python-3
place this code in a file named: 'setup_TF_ODAPI.py' and put this file inside the parent directory
containing the object_detection directory i.e place it in your_path/models/research

Usage:
$python setup_TF_ODAPI.py

follow the instructions on the screen
"""
import os
import subprocess

print("Checking if the environment is already setup ...")
c = subprocess.call(["python", "object_detection/builders/model_builder_test.py"],
                    stdout=open(os.devnull, 'wb')  # make it quiet
                    )
if c == 0:
    print("environment is already setup")
    print("The Tensorflow Object detection API is ready to use!")

else:
    print('Environment is not setup already. Setting up a fresh environment...')
    curr_work_dir = os.getcwd()
    # compile the protobuf files
    cmd = "protoc object_detection/protos/*.proto --python_out=."
    os.system(cmd)
    print("Protobuf files are compiled")
    # adding environment variable to ~/.bashrc file
    home = os.path.expanduser("~")
    with open(os.path.join(home, ".bashrc"), "a") as f:
        f.write("\n")
        f.write("# For Tensorflow object detection API")
        f.write("\n")
        f.write("export PYTHONPATH=$PYTHONPATH:{}:{}/slim".format(curr_work_dir, curr_work_dir))
    print("Python path added to ./bashrc file")

    print("The environment is setup. From a new terminal try running the same script to verify")
