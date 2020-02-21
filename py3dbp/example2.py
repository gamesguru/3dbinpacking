import json
from main import Packer, Bin, Item

packer = Packer()


packer.add_bin(Bin('small-envelope', 11.5, 6.125, 0.25, 0.8125))
packer.add_bin(Bin('large-envelope', 15.0, 12.0, 0.75, 0.8125))
packer.add_bin(Bin('small-box', 8.625, 5.375, 1.625, 70.0))
packer.add_bin(Bin('medium-box', 11.0, 8.5, 5.5, 70.0))
packer.add_bin(Bin('medium-box', 13.625, 11.875, 3.375, 70.0))
packer.add_bin(Bin('large-box', 12.0, 12.0, 5.5, 70.0))
packer.add_bin(Bin('large-box', 23.6875, 11.75, 3.0, 70.0))

packer.add_item(Item('50g [powder]', 3.9370, 1.9685, 1.9685, 50))
packer.add_item(Item('50g [powder]', 3.9370, 1.9685, 1.9685, 50))
packer.add_item(Item('50g [powder]', 3.9370, 1.9685, 1.9685, 50))
packer.add_item(Item('250g [powder]', 7.8740, 3.9370, 1.9685, 250))
packer.add_item(Item('250g [powder]', 7.8740, 3.9370, 1.9685, 250))
packer.add_item(Item('250g [powder]', 7.8740, 3.9370, 1.9685, 250))
packer.add_item(Item('250g [powder]', 7.8740, 3.9370, 1.9685, 250))
packer.add_item(Item('250g [powder]', 7.8740, 3.9370, 1.9685, 250))
packer.add_item(Item('250g [powder]', 7.8740, 3.9370, 1.9685, 250))

packer.pack()

for bin in packer.bins:
    if bin.items:
        print(json.dumps(bin, default=lambda x: x.__dict__))
        print(len(bin.items))
