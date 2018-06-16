The way that I set up the paths was by setting PATH and PYTHONPATH to the respective binary paths and this allows me to use the local caffe repository that I setup. I can now run make in that repo using the general instructions on slack under help in order to make stuff. Now i need to figure out how to modify the src layer files and make my own. The commands for the paths are bellow

PATH=/home/alec/Summer2018/gnina/build/caffe/tools:$PATH
PYTHONPATH=/home/alec/Summer2018/gnina/caffe/python:$PYTHONPATH

