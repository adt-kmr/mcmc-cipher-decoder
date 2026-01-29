
Metropolis Hastings is a foundational Markov Chain Monte Carlo (MCMC) algorithm, which is used to sample from complex probability distibutions when direct sampling is not feaasible. 

The implementation is designed to be:

1. Distribution agnostic
2. Normalization free
3. Conceptually transparent
4. Extensible to higher dimensions and Bayesian inference



Metropolis–Hastings constructs a biased random walk that:

1. Moves freely in high probability regions
2. Occasionally explores low probability regions
3. Avoids getting trapped in local modes


Algorithm Pseudocode: 

initialize x_current
for iteration in range(N):
    propose x_new ~ q(x_new | x_current)

    acceptance_ratio = pi(x_new) / pi(x_current)
    acceptance_probability = min(1, acceptance_ratio)

    if random_uniform(0,1) < acceptance_probability:
        x_current = x_new

    store x_current


Computational Characteristics: 

1. Time Complexity: O(N)
2. Space Complexity: O(N)
3. Scalability: Extensible to multidimensional targets


Applications of Metropolis Hastings: 

1. Bayesian posterior sampling
2. Probabilistic graphical models
3. Statistical physics simulations
4. Modern probabilistic programming frameworks

