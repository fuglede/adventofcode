from functools import cache

with open("input") as f:
    ls = [l.split() for l in f.read().splitlines()]

succ = {start[:-1]: to for start, *to in ls}


@cache
def paths_from(node, dac_seen=True, fft_seen=True):
    dac_seen = dac_seen or node == "dac"
    fft_seen = fft_seen or node == "fft"
    if node == "out":
        return dac_seen and fft_seen
    return sum(paths_from(to_node, dac_seen, fft_seen) for to_node in succ[node])


# Part 1
print(paths_from("you"))

# Part 2
print(paths_from("svr", False, False))
