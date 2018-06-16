This folder is for my Summer 2018 project at the University of Pittsburgh Department of Computational and Systems Biology.
This is an attempt at creating a nerual network model using the framework Caffe that can take data representing protein ligand interactions with randomly translated and rotated ligands and output a transformation back to the initial pose. 

xx Download Caffe from the gnina source and figure out how to build it
   xx This was done by cloning the gnina repository and running various make commands to build and install caffe. I now need to figure out how to use the pycaffe interface and run the local caffe binary from a different directory so that I can train models.
   -- Caffe is built and the local binary and pycaffe can both be used by setting the correct paths, which are shown in CaffePathSetup.md . I am pretty sure they can be used from any directory. I should check that rebuilding with altered src works properly with this as well.
-- I now should look through the various layers in the caffe documentation
-- I should also look into the documentation for protocol buffers and figure out the specifics of the caffe protobuf language
-- Read through the documentation and code for molgrid layer
xx Find the PDBBind refined crystal dataset on Apogee or move it over to Apogee
   -- There is a symlink to this in the data directory
-- Read through train.py documentation and code
xx Look into how to use the python tools for caffe to do things like generate an image showing a model's architecture
   --draw_net.py works well enough. I had to edit draw.py so that something with the labels for pooling layers would work. It doesnt seem to effect the output. I should pull the code and fix this because right now it is pretty hacky
-- Design the first architechture that I will be attempting to train
-- Look into how to make the trigonometric function layer in caffe that dkoes mentioned
-- Make scripts that make training on different variations of the models simple
-- Figure out an organizational structure for the directory
-- Make scripts that automatically generate visualizations
   -- Maybe use matplotlib or simpler plotting library in python
   -- This could also be built into jupyter notebooks
-- Look into using the pycaffe library because it will be useful when making scripts 
-- Look into using pymol or another molecular visualizations platform to visualize the results
   -- To do this I could look at the actual crystal poses dataset and look at the pdb codes. After that I could pull them up in Pymol and figure out how to visualize them at the correct orientation. Then I could make visualizations of overlapping molecules with the before and after poses.
