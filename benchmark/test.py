import networkx as nx
from time import time

from graphGeneration import Cora, CiteSeer, PubMed, connSW, ER, coms, photo
from baselines import pi, eigen, degree, celfpp, celf, greedy,IMRank,RIS
from score import effectIC, effectLT

print('round A: budget = 5')
g, config = Cora()

print("Cora graph is on.")

# print('Simulation greedy IC')
# start = time()
# set = greedy(g, config, budget=5, model='IC')
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('Simulation CELF++ IC')
# start = time()
# set = celfpp(g, config, budget=5, model='IC')
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('Simulation CELF IC')
# start = time()
# set = celf(g, config, budget=5, model='IC')
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('Simulation greedy LT')
# start = time()
# set = greedy(g, config, budget=5, model='LT')
# end = time()
# print("time: ", end-start)
# ie,var = effectLT(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('Simulation CELF++ LT')
# start = time()
# set = celfpp(g, config, budget=5, model='LT')
# end = time()
# print("time: ", end-start)
# ie,var = effectLT(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('Simulation CELF LT')
# start = time()
# set = celf(g, config, budget=5, model='LT')
# end = time()
# print("time: ", end-start)
# ie,var = effectLT(g, config, set)
# print('IE:', ie, " +_ ", var)

g, config = CiteSeer()

print("CiteSeer graph is on.")
print('budget = 5')

print('Simulation greedy IC')
start = time()
set = greedy(g, config, budget=5, model='IC')
end = time()
print("time: ", end-start)
ie,var = effectIC(g, config, set)
print('IE:', ie, " +_ ", var)

print('Simulation CELF++ IC')
start = time()
set = celfpp(g, config, budget=5, model='IC')
end = time()
print("time: ", end-start)
ie,var = effectIC(g, config, set)
print('IE:', ie, " +_ ", var)

print('Simulation CELF IC')
start = time()
set = celf(g, config, budget=5, model='IC')
end = time()
print("time: ", end-start)
ie,var = effectIC(g, config, set)
print('IE:', ie, " +_ ", var)

print('Simulation greedy LT')
start = time()
set = greedy(g, config, budget=5, model='LT')
end = time()
print("time: ", end-start)
ie,var = effectLT(g, config, set)
print('IE:', ie, " +_ ", var)

print('Simulation CELF++ LT')
start = time()
set = celfpp(g, config, budget=5, model='LT')
end = time()
print("time: ", end-start)
ie,var = effectLT(g, config, set)
print('IE:', ie, " +_ ", var)

print('Simulation CELF LT')
start = time()
set = celf(g, config, budget=5, model='LT')
end = time()
print("time: ", end-start)
ie,var = effectLT(g, config, set)
print('IE:', ie, " +_ ", var)


print('round B: budget = 50')

g, config = Cora()

print("Cora graph is on.")

print('Simulation greedy IC')
start = time()
set = greedy(g, config, budget=50, model='IC')
end = time()
print("time: ", end-start)
ie,var = effectIC(g, config, set)
print('IE:', ie, " +_ ", var)

print('Simulation CELF++ IC')
start = time()
set = celfpp(g, config, budget=50, model='IC')
end = time()
print("time: ", end-start)
ie,var = effectIC(g, config, set)
print('IE:', ie, " +_ ", var)

print('Simulation CELF IC')
start = time()
set = celf(g, config, budget=50, model='IC')
end = time()
print("time: ", end-start)
ie,var = effectIC(g, config, set)
print('IE:', ie, " +_ ", var)

print('Simulation greedy LT')
start = time()
set = greedy(g, config, budget=50, model='LT')
end = time()
print("time: ", end-start)
ie,var = effectLT(g, config, set)
print('IE:', ie, " +_ ", var)

print('Simulation CELF++ LT')
start = time()
set = celfpp(g, config, budget=50, model='LT')
end = time()
print("time: ", end-start)
ie,var = effectLT(g, config, set)
print('IE:', ie, " +_ ", var)

print('Simulation CELF LT')
start = time()
set = celf(g, config, budget=50, model='LT')
end = time()
print("time: ", end-start)
ie,var = effectLT(g, config, set)
print('IE:', ie, " +_ ", var)

g, config = CiteSeer()

print("CiteSeer graph is on.")

print('Simulation greedy IC')
start = time()
set = greedy(g, config, budget=50, model='IC')
end = time()
print("time: ", end-start)
ie,var = effectIC(g, config, set)
print('IE:', ie, " +_ ", var)

print('Simulation CELF++ IC')
start = time()
set = celfpp(g, config, budget=50, model='IC')
end = time()
print("time: ", end-start)
ie,var = effectIC(g, config, set)
print('IE:', ie, " +_ ", var)

print('Simulation CELF IC')
start = time()
set = celf(g, config, budget=50, model='IC')
end = time()
print("time: ", end-start)
ie,var = effectIC(g, config, set)
print('IE:', ie, " +_ ", var)

print('Simulation greedy LT')
start = time()
set = greedy(g, config, budget=50, model='LT')
end = time()
print("time: ", end-start)
ie,var = effectLT(g, config, set)
print('IE:', ie, " +_ ", var)

print('Simulation CELF++ LT')
start = time()
set = celfpp(g, config, budget=50, model='LT')
end = time()
print("time: ", end-start)
ie,var = effectLT(g, config, set)
print('IE:', ie, " +_ ", var)

print('Simulation CELF LT')
start = time()
set = celf(g, config, budget=50, model='LT')
end = time()
print("time: ", end-start)
ie,var = effectLT(g, config, set)
print('IE:', ie, " +_ ", var)