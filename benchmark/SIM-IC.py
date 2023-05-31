import networkx as nx
from time import time

from graphGeneration import Cora, CiteSeer, PubMed, connSW, ER, coms, photo
from baselines import eigen, degree, pi, sigma, greedy, celf, celfpp, IMRank, RIS
from score import effectIC

g, config = Cora()

print("Cora graph is on.")
# print(nx.info(g))

# print('------------------------------------------------')
# print('degreeDiscount')
# start = time()
# set = degreeDis(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('Soboldd')
# start = time()
# set = SoboldegreeDis(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('pi')
# start = time()
# set = pi(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolpi')
# start = time()
# set = SobolPi(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)


# print('------------------------------------------------')
# print('sigma')
# start = time()
# set = sigma(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolsigma')
# start = time()
# set = SobolSigma(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('NetShield')
# start = time()
# set = Netshield(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolNS')
# start = time()
# set = SobolNS(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('IMRank')
# start = time()
# set = IMRank(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('RIS')
# start = time()
# set = RIS(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('degree')
# start = time()
# set = degree(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('eigen-centrality')
# start = time()
# set = eigen(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)


# print('------------------------------------------------')
# print('celf')
# start = time()
# set = celf(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('celfpp')
# start = time()
# set = celfpp(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('greedy')
# start = time()
# set = greedy(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('soboldegree')
# start = time()
# set = Soboldeg(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('soboleigen')
# start = time()
# set = Soboleigen(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)


# print('-------------------------------------------------------------------------------')
# g, config = CiteSeer()
# print("CiteSeer graph is on.")
# print(nx.info(g))

# print('------------------------------------------------')
# print('dd')
# start = time()
# set = degreeDis(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('Soboldd')
# start = time()
# set = SoboldegreeDis(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('pi')
# start = time()
# set = pi(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolpi')
# start = time()
# set = SobolPi(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)


# print('------------------------------------------------')
# print('sigma')
# start = time()
# set = sigma(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolsigma')
# start = time()
# set = SobolSigma(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('NetShield')
# start = time()
# set = Netshield(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolNS')
# start = time()
# set = SobolNS(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('degree')
# start = time()
# set = degree(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('soboldegree')
# start = time()
# set = Soboldeg(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('eigen-centrality')
# start = time()
# set = eigen(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('soboleigen')
# start = time()
# set = Soboleigen(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)


# print('-------------------------------------------------------------------------------')
# g, config = PubMed()
# print("PubMed graph is on.")
# print(nx.info(g))

# print('------------------------------------------------')
# print('dd')
# start = time()
# set = degreeDis(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('Soboldd')
# start = time()
# set = SoboldegreeDis(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('pi')
# start = time()
# set = pi(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolpi')
# start = time()
# set = SobolPi(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)


# print('------------------------------------------------')
# print('sigma')
# start = time()
# set = sigma(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolsigma')
# start = time()
# set = SobolSigma(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('NetShield')
# start = time()
# set = Netshield(g,config,5)
# end = time()
# print("time: ", end-start)
# ie = effectIC(g, config, set)
# print('IE:', ie)

# print('------------------------------------------------')
# print('sobolNS')
# start = time()
# set = SobolNS(g,config,5)
# end = time()
# print("time: ", end-start)
# ie = effectIC(g, config, set)
# print('IE:', ie)

# print('------------------------------------------------')
# print('degree')
# start = time()
# set = degree(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('soboldegree')
# start = time()
# set = Soboldeg(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('eigen-centrality')
# start = time()
# set = eigen(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('soboleigen')
# start = time()
# set = Soboleigen(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('-------------------------------------------------------------------------------')
# g, config = ER()
# print("ER graph is on.")
# print(nx.info(g))

# print('------------------------------------------------')
# print('dd')
# start = time()
# set = degreeDis(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('Soboldd')
# start = time()
# set = SoboldegreeDis(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('pi')
# start = time()
# set = pi(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolpi')
# start = time()
# set = SobolPi(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)


# print('------------------------------------------------')
# print('sigma')
# start = time()
# set = sigma(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolsigma')
# start = time()
# set = SobolSigma(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('NetShield')
# start = time()
# set = Netshield(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolNS')
# start = time()
# set = SobolNS(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('degree')
# start = time()
# set = degree(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('soboldegree')
# start = time()
# set = Soboldeg(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('eigen-centrality')
# start = time()
# set = eigen(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('soboleigen')
# start = time()
# set = Soboleigen(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('-------------------------------------------------------------------------------')
# g, config = connSW()
# print("SW graph is on.")
# print(nx.info(g))

# print('------------------------------------------------')
# print('dd')
# start = time()
# set = degreeDis(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('Soboldd')
# start = time()
# set = SoboldegreeDis(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('pi')
# start = time()
# set = pi(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolpi')
# start = time()
# set = SobolPi(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)


# print('------------------------------------------------')
# print('sigma')
# start = time()
# set = sigma(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolsigma')
# start = time()
# set = SobolSigma(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('NetShield')
# start = time()
# set = Netshield(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolNS')
# start = time()
# set = SobolNS(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('degree')
# start = time()
# set = degree(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('soboldegree')
# start = time()
# set = Soboldeg(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('eigen-centrality')
# start = time()
# set = eigen(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('soboleigen')
# start = time()
# set = Soboleigen(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('-------------------------------------------------------------------------------')
# g, config = coms()
# print("Computer graph is on.")
# print(nx.info(g))

# print('------------------------------------------------')
# print('dd')
# start = time()
# set = degreeDis(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('Soboldd')
# start = time()
# set = SoboldegreeDis(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('pi')
# start = time()
# set = pi(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolpi')
# start = time()
# set = SobolPi(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)


# print('------------------------------------------------')
# print('sigma')
# start = time()
# set = sigma(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolsigma')
# start = time()
# set = SobolSigma(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('NetShield')
# start = time()
# set = Netshield(g,config,5)
# end = time()
# print("time: ", end-start)
# ie = effectIC(g, config, set)
# print('IE:', ie)

# print('------------------------------------------------')
# print('sobolNS')
# start = time()
# set = SobolNS(g,config,5)
# end = time()
# print("time: ", end-start)
# ie = effectIC(g, config, set)
# print('IE:', ie)

# print('------------------------------------------------')
# print('degree')
# start = time()
# set = degree(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('soboldegree')
# start = time()
# set = Soboldeg(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('eigen-centrality')
# start = time()
# set = eigen(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('soboleigen')
# start = time()
# set = Soboleigen(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('-------------------------------------------------------------------------------')
# g, config = photo()
# print("Photo graph is on.")
# print(nx.info(g))

# print('------------------------------------------------')
# print('dd')
# start = time()
# set = degreeDis(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('Soboldd')
# start = time()
# set = SoboldegreeDis(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('pi')
# start = time()
# set = pi(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolpi')
# start = time()
# set = SobolPi(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)


# print('------------------------------------------------')
# print('sigma')
# start = time()
# set = sigma(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('sobolsigma')
# start = time()
# set = SobolSigma(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('NetShield')
# start = time()
# set = Netshield(g,config,5)
# end = time()
# print("time: ", end-start)
# ie = effectIC(g, config, set)
# print('IE:', ie)

# print('------------------------------------------------')
# print('sobolNS')
# start = time()
# set = SobolNS(g,config,5)
# end = time()
# print("time: ", end-start)
# ie = effectIC(g, config, set)
# print('IE:', ie)

# print('------------------------------------------------')
# print('degree')
# start = time()
# set = degree(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('soboldegree')
# start = time()
# set = Soboldeg(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('eigen-centrality')
# start = time()
# set = eigen(g,config,5)
# end = time()
# print('time: ', end - start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)

# print('------------------------------------------------')
# print('soboleigen')
# start = time()
# set = Soboleigen(g,config,5)
# end = time()
# print("time: ", end-start)
# ie,var = effectIC(g, config, set)
# print('IE:', ie, " +_ ", var)
