import math

# Part 1
print(
    math.prod(
        sum(i * (limit - i) > dist for i in range(dist))
        for limit, dist in zip([46, 68, 98, 66], [358, 1054, 1807, 1080])
    )
)

# Part 2
limit, dist = 46689866, 358105418071080
print(sum(i * (limit - i) > dist for i in range(limit)))
