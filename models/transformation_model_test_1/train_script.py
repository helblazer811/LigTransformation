import caffe
caffe.set_mode_gpu()
solver_path = "solver.prototxt"

solver = caffe.SGDSolver(solver_path)

solver.step(1)

#iterations = 1000 # Depending on dataset size, batch size etc. ...
#for iteration in range(iterations):
#    solver.step(1) # We could also do larger steps (i.e. multiple iterations at once).
