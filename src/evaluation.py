def char_accuracy(true, pred):
    correct = sum(t == p for t, p in zip(true, pred))
    return correct / len(true)






import matplotlib.pyplot as plt

def plot_scores(scores):
    plt.plot(scores)
    plt.xlabel("Iteration")
    plt.ylabel("Log Posterior")
    plt.show()
