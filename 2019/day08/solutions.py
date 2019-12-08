import numpy as np


with open('input') as f:
    layers = np.array(list(f.read().strip())).reshape(-1, 6*25)

# Part one
layer = layers[(layers == '0').sum(1).argmin()]
print((layer == '1').sum() * (layer == '2').sum())

# Part two
visible = np.argmax(layers != '2', 0)
image = layers[(visible, range(len(visible)))].reshape(6, 25)
print('\n'.join(''.join(x).replace('0', ' ') for x in image))
