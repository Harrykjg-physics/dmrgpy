import sys
import os
import numpy as np
sys.path.append(os.environ["DMRGROOT"]) # root for dmrg
import spinchain

n = 10
spins = [2 for i in range(n)] # spin 1/2 heisenberg chain
sc = spinchain.Spin_Hamiltonian(spins) # create the spin chain

def fj(i,j):
  if j==(i+1): return 1.0
  else: return 0.0
#sc.set_exchange(fj)
#sc.set_fields(lambda x: np.random.random(3))

#sc.kpmmaxm = 20 # KPM maxm
import time

sc.kpmmaxm = 40
t1 = time.time()
(x2,y2) = sc.get_dynamical_correlator(n=600,mode="DMRG",i=5,j=5,delta=0.02)
import entropy

s = entropy.dynamical_correlator_kpm(sc)

import matplotlib.pyplot as plt

plt.plot(range(len(s)),s,c="blue",label="DMRG")

plt.show()

