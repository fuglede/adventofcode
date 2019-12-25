from collections import defaultdict, deque
from queue import Queue
import time
from vm import VM, read_program

ns = read_program(23)

class Input:
    def __init__(self, i):
        self.inputs = deque([i])

    def popleft(self):
        return self.inputs.popleft() if self.inputs else -1

    def add(self, val):
        self.inputs.append(val)

vms = []
for i in range(50):
    inputs = Input(i)
    vm = VM(ns, inputs)
    vms.append(vm)
i = 0
idling = set()
NAT = None
last_y = None
while True:
    dst = next(vms[i].it)
    if dst is None:
        if not vms[i].inputs.inputs:
            idling.add(i)
        if len(idling) == 50 and NAT is not None:
            if NAT[1] == last_y:
                # Part two
                print(last_y)
                break
            last_y = NAT[1]
            vms[0].inputs.add(NAT[0])
            vms[0].inputs.add(NAT[1])
            idling.remove(0)
            i = 0
            continue
        i = (i + 1) % 50
        continue
    if i in idling:
        idling.remove(i)
    x, y = next(vms[i]), next(vms[i])
    if dst == 255:
        if NAT is None:
            # Part one
            print(y)
        NAT = (x, y)
        i = (i + 1) % 50
    else:
        vms[dst].inputs.add(x)
        vms[dst].inputs.add(y)
        i = dst
