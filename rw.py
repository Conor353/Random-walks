import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Number of steps in the random walk
n_steps = 1000


# use a function to generate a random walk
def norm_walk(n):
    random_numbers = np.random.normal(size=n)
    walk = np.concatenate(([0], np.cumsum(random_numbers)))
    return walk

def cauchy_walk(n):
    random_numbers = np.random.standard_cauchy(size=n)
    walk = np.concatenate(([0], np.cumsum(random_numbers)))
    return walk



n_walks = 300

# Create the dataframe
norm_column_names = ["norm_walk_" + str(i) for i in range(1, n_walks)]
Cauchy_column_names = ["Cauchy_walk_" + str(i) for i in range(1, n_walks)]
df = pd.DataFrame(columns = Cauchy_column_names + norm_column_names )


for i in range(1, n_walks):

#    df["norm_walk_"+ str(i)] = norm_walk(n_steps)
    df["Cauchy_walk_"+ str(i)] = cauchy_walk(n_steps)





plt.plot(df)

plt.show()


