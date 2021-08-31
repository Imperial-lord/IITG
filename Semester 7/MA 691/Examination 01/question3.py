import random
import math
import matplotlib.pyplot as plt


def generate(t):
    l = []
    for i in range(t):
        u1 = random.uniform(0, 1)
        u2 = random.uniform(0, 1)
        r = -2 * math.log(u1)
        v = 2 * math.pi * u2
        z1 = math.sqrt(r) * math.cos(v)
        z2 = math.sqrt(r) * math.sin(v)
        l.append(z1)
        l.append(z2)
    return l


def mixture(norm_list):
    updated_list = []
    for l in norm_list:
        r = random.uniform(0, 1)
        if r < 0.4:
            updated_list.append(math.sqrt(2) * l + 4)
        else:
            updated_list.append(math.sqrt(3) * l + 11)
    return updated_list


t = 10000
distribution = generate(t)
mixture_distribution = mixture(distribution)


fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(mixture_distribution, bins=100, density=True)
plt.savefig("multiNormal.png")
