from collections import defaultdict
import math






# Cell 

def train_bigram(text):
  counts= defaultdict(lambda: defaultdict(int))
  totals = defaultdict(int)

  for i in range(len(text)-1):

    a,b = text[i], text[i+1]
    if a.isalpha() and b.isalpha():

      counts[a][b] += 1
      totals[a] += 1

      probs = defaultdict(dict)
      for a in counts:
        for b in counts[a]:

          probs[a][b] = math.log(counts[a][b] / totals[a])
          return probs





#Cell 





def score_text(text, bigram_probs, floor=-12):

    score = 0.0


    for i in range(len(text) - 1):
        a, b = text[i], text[i+1]

        if a in bigram_probs and b in bigram_probs[a]:
            score += bigram_probs[a][b]
        else:
          
            score += floor
    return score






#Cell



english = "this is a simple english sentence"

random_text = "xqz jkp mwo tttt"

model = train_bigram(english)
score_text(english, model) > score_text(random_text, model)
#It should be True


