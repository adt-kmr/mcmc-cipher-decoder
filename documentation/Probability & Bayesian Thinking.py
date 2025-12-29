
# Toy Example: 

# Our Target: Estimating the probability of a coin being biased towards Heads. 

  # 1. PRIOR: Coin is fair (uniform probability between 0 and 1)
  # 2. OBSERVED DATA: Total coin flips = 10; No. of heads recieved = 7. 


# Prior = Guess before experiment; Likelihood = Check how data fits the guess; Posterior = Updated guess after the experiment.

import numpy as np
theta = np.linspace(0, 1, 11) 
print(theta) 


prior = np.ones_like(theta)/len(theta) 
print(prior) 


from scipy.stats import binom
n=10
k=7
likelihood = binom.pmf(k,n,theta) 
print(np.round(likelihood,3))


unnormalized_posterior = likelihood*prior
posterior = unnormalized_posterior / np.sum(unnormalized_posterior) 
print(np.round(posterior,3))


# Visual Representation 

import matplotlib.pyplot as plt

plt.plot(theta, prior, label="Prior", marker="o")
plt.plot(theta, likelihood/np.max(likelihood), label="Likelihood (scaled)", marker='x')
plt.plot(theta, posterior, label="Posterior", marker='s')
plt.xlabel("Theta (Probability of Heads)")
plt.ylabel("Probability / Score")
plt.title("Bayesian Update Example")
plt.legend()
plt.show()




