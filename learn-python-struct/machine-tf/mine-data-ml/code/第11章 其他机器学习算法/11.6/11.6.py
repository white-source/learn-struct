import numpy as np
from scipy import stats
from matplotlib.pyplot import *
n = 10  
k = 5  
p = np.linspace(0, 1, 100)  
pbeta = stats.beta.pdf(p, k+1, n-k+1)  
plot(p, pbeta, label="k=5", lw=2)  
  
k = 4  
pbeta = stats.beta.pdf(p, k+1, n-k+1)  
plot(p, pbeta, label="k=4", lw=2)  
xlabel("$p$")  
legend(loc="best");  
show()
