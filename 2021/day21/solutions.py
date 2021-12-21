from collections import Counter
from functools import cache
from itertools import product

# In both parts, we make the convention that p1 is the player next up.
# Part one
def play(p1pos, p2pos, p1score=0, p2score=0, i=0):
    if p2score >= 1000:
        return i * p1score
    p1pos = (p1pos + 3 * i + 5) % 10 + 1
    return play(p2pos, p1pos, p2score, p1score + p1pos, i + 3)


print(play(8, 7))

# Part two
# As above, we treat the game as a recursive operation on game states,
# the only difference here being that there are multiple follow-up states.
# Since rolls such as (1, 2, 1) and (1, 1, 2) lead to the same state, we
# begin by grouping rolls. Our recursively defined function then returns
# the number of descendant states that lead to wins for player 1 and
# player 2 respectively; the result is represented as a complex number
# whose real and imaginary parts keep track of the number of wins.
roll_counts = Counter(map(sum, product((1, 2, 3), repeat=3)))


@cache
def play(p1pos, p2pos, p1score=0, p2score=0):
    if p2score >= 21:
        return 1
    return sum(count * play(
            p2pos,
            new_p1pos := (p1pos + roll - 1) % 10 + 1,
            p2score,
            p1score + new_p1pos,
        ).conjugate() * 1j
        for roll, count in roll_counts.items()
    )


res = play(8, 7)
print(max(res.real, res.imag))
