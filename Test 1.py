import matplotlib.pyplot as plt
import numpy as np
import pandas as pandas
import pandas as pd
import pandas as pd
import pickle
np.random.seed(123)
all_walks = []
for i in range (500):
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
        if np.random.rand() <= 0.0001 :

            step = 0

    all_walks.append(random_walk)

np_aw_t = np.transpose((np.array(all_walks)))
end = np_aw_t [-1,:]
ends = np_aw_t[-1,:]
final_tails = []
for x in range (10000) :
    tails =[0]
    for x in range(10):
        coin = np.random.randint(0,2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
x = np.median(final_tails)
print(x)
y = np.mean(final_tails)
