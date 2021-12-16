import math

with open("input") as f:
    data = f.read().strip()


total_version = 0
ops = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    5: lambda l: int(l[0] > l[1]),
    6: lambda l: int(l[0] < l[1]),
    7: lambda l: int(l[0] == l[1]),
}


def parse(packet):
    version = int(packet[0:3], 2)
    global total_version
    total_version += version
    packet_type = int(packet[3:6], 2)
    if packet_type == 4:
        i = 6
        s = ""
        while True:
            s += packet[i + 1 : i + 5]
            if packet[i] == "0":
                return int(s, 2), i + 5
            i += 5
    length_type = packet[6]
    op = ops[packet_type]
    if length_type == "0":
        length = int(packet[7 : 7 + 15], 2)
        inner = packet[7 + 15 :]
        index_sum = 0
        ls = []
        while index_sum < length:
            result, index = parse(inner[index_sum:])
            ls.append(result)
            index_sum += index
        return op(ls), 7 + 15 + index_sum
    else:
        num_packets = int(packet[7 : 7 + 11], 2)
        inner = packet[7 + 11 :]
        index_sum = 0
        ls = []
        for i in range(num_packets):
            result, index = parse(inner[index_sum:])
            ls.append(result)
            index_sum += index
        return op(ls), 7 + 11 + index_sum


total_version = 0
packet = "".join(bin(int(d, 16))[2:].zfill(4) for d in data)
result, _ = parse(packet)

# Part one
print(total_version)

# Part two
print(result)
