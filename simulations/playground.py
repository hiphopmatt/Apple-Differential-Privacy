from simulations.frequency_oracles.NormalDistSimulation import NormalDistSimulation
from simulations.heavy_hitters.ExponentialDistSimulation import ExponentialDistSimulation
import math

# #-------------------- Parameters for simulation --------------------
#
# # Normal Dist Parameters
# N = 10000
# mu = 10
# sd = 3
#
# # CMS/HCMS Parameters
# m = 2048
# k = 1024
# epsilon = 0.1 # 1, 0.1
#
# # PrivCountSketch Parameters
# l = 250
# numBits = int(math.floor(math.log(N, 2)) + 1)
# w = 2 ** numBits
#
# # RAPPOR Parameters
# num_bloombits = 128  # Max size is 256 bits
# num_hashes = 2  # Recommended to use 2 hashes
# num_of_cohorts = 32  # Max cohorts is 64
#
# # Guarantees slightly over epsilon = 1 for privacy
# prob_p = 0.5
# prob_q = 0.75
# prob_f = 0
#
# # Hashtogram Parameters
# R = 100
# T = 100
#
# # -------------------- Simulation Code --------------------
#
# normal_simulation = NormalDistSimulation(N, mu, sd)
#
# cms = {"m": m, "k": k, "epsilon": epsilon}
# priv_count_sketch = {"l": l, "w": w, "epsilon": epsilon}
# explicit_hist = {"epsilon": epsilon}
# hashtogram = {"epsilon": epsilon, "R": R, "T": R}
#
# rappor = {
#     "num_bloombits": num_bloombits,
#     "num_hashes": num_hashes,
#     "num_of_cohorts": num_of_cohorts,
#     "prob_p": prob_p,
#     "prob_q": prob_q,
#     "prob_f": prob_f
# }
#
# normal_simulation.run_and_plot([("cms", cms), ("hcms", cms), ("priv_count_sketch", priv_count_sketch),
#                                 ("priv_count_sketch_median", priv_count_sketch), ("explicit_hist", explicit_hist),
#                                 ("hashtogram", hashtogram), ("hashtogram_median", hashtogram), ("rappor", rappor)])

# normal_simulation.run_and_plot([("rappor", rappor)])

m = 2048
k = 1024  # We use k = k_prime and m = m_prime for our simulation

epsilon = 3
epsilon_prime = 3
threshold = 30

N = 20000
p = 0.3
alphabet = list("abc")
word_length = 6
word_sample_size = 10

sfp = {
    "m": m,
    "k": k,
    "epsilon": epsilon,
    "m_prime": m,
    "k_prime": k,
    "epsilon_prime": epsilon_prime,
    "threshold": threshold,
    "alphabet": alphabet
}

bitstogram = {
    "epsilon": epsilon,
    "R": 5,
    "T": 2000,
    "word_length": word_length
}

succincthist = {
    "epsilon": epsilon,
    "max_length_string": word_length,
    "T": 10,
}

d = word_length * 8
logd = d
w = 32 * logd*math.log(16*logd,2) + ((48/epsilon)*math.sqrt(2*N*logd*math.log(64*logd)))
T = 32*N/w

numBits = int(math.floor(math.log(math.sqrt(N), 2)) + 1)
w = 2**numBits # Sketch size
print(w)
w = 128
assert (int(math.log(w, 2)) <= 254), 'Sketch size (w) too large'

l = 250  # Number of hash function pairs (f,g)

num_n_grams = 3 # Number of N-grams
gram_length = 2  # Gram length
threshold = 3 * int(math.sqrt(N))  # Threshold for discoverability

treehistogram = {
    "epsilon": epsilon,
    "l": l,
    "w": w,
    "num_n_grams": num_n_grams,
    "gram_length": gram_length,
    "threshold": threshold
}

exponential_simulation = ExponentialDistSimulation(N, p, alphabet, word_length, word_sample_size)

exponential_simulation.run_and_plot([("sfp", sfp), ("treehistogram", treehistogram), ("succincthist", succincthist), ("bitstogram", bitstogram)])
