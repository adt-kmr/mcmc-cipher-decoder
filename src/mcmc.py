import math
import random
from cipher import decrypt, propose_key









def mcmc_decode(ciphertext, score_fn, iterations=5000, temperature=1.0):
    current_key = random_key()
    current_score = score_fn(decrypt(ciphertext, current_key))

    best_key = current_key
    best_score = current_score

    scores = []

    for i in range(iterations):
        candidate_key = propose_key(current_key)
        candidate_score = score_fn(decrypt(ciphertext, candidate_key))

        delta = candidate_score - current_score
        if delta > 0 or random.random() < math.exp(delta / temperature):
            current_key = candidate_key
            current_score = candidate_score

        if current_score > best_score:
            best_key = current_key
            best_score = current_score

        scores.append(best_score)

    return best_key, scores





























