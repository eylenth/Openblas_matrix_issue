from rpy2 import robjects
import numpy as np

robjects.r['load']("data.RData")

data = robjects.r['Khat']

data = np.array(data)

np.savetxt('data.txt', data)


