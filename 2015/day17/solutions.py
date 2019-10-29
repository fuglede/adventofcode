from collections import defaultdict


with open('input') as f:
    all_containers = list(int(x.strip()) for x in f.readlines())


def hash_avail(containers):
    return sum(2**i for i in containers)


done = set()
ways = defaultdict(set)


def count(to_store, containers):
    if to_store == 0:
        ways[len(containers)].add(hash_avail(containers))
        return
    if to_store < min(all_containers) or (to_store, hash_avail(containers)) in done:
        return
    for i in containers:
        count(to_store - all_containers[i], containers - {i})
    done.add((to_store, hash_avail(containers)))


count(150, set(range(len(all_containers))))

print(sum(len(x) for x in ways.values()))
print(len(ways[max(ways.keys())]))
