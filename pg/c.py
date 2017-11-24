from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

ds = SupervisedDataSet(3, 1)
ds.addSample((0, 0, 1), (0))
ds.addSample((1, 1, 1), (1))
ds.addSample((1, 0, 1), (1))
ds.addSample((0, 1, 1), (0))

net = buildNetwork(3, 3, 1)

trainer = BackpropTrainer(net, ds)
trainer.train()

for input, target in ds:
    print (input, target, net.activate(input))

