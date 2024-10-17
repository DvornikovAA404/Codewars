# In a small town the population is p0 = 1000 at the beginning of a year.
# The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come
# to live in the town.
# How many years does the town need to see its population greater than or equal to p = 1200 inhabitants?
from math import *
def nb_year(p0: int, percent: int, aug: int, p: int):
    k = 0
    while p0 < p:
        p0 = floor(p0 + p0 * (percent / 100) + aug)
        k += 1
        print(k)

print(nb_year(1500, 5, 100, 5000))