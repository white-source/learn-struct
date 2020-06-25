#import numpy as np
#import theano.tensor as tt
import pymc3 as pm

#import seaborn as sns
import matplotlib.pyplot as plt

# with pm.Model() as model:
#     cold =  pm.Dirichlet('cold', a=np.array([1., 1., 2.0]), shape=3)
#     cough = pm.Categorical('cough', p = cold, observed=([2, 2, 2]))
#     tan = pm.Categorical('tan', p = cold)

#     #sprinkler_p = pm.Deterministic('sprinkler_p', pm.math.switch(tan, 0.01, 0.40))
#     #sprinkler = pm.Bernoulli('sprinkler', sprinkler_p,shape=1)
    
#     trace = pm.sample(100)
#     print(pm.summary(trace))

# exit()
    
basic_model = pm.Model()
with basic_model:
    asia_p = pm.Beta('asia_p', 5, 95)
    asia = pm.Bernoulli('asia', p=asia_p, observed=False)
    smoking = pm.Bernoulli('smoking', p=0.3, observed=True)

    tuberculosis_p = pm.Deterministic('tuberculosis_p', pm.math.switch(asia, 0.4, 0.1))
    tuberculosis = pm.Bernoulli('tuberculosis', p=tuberculosis_p)
    cancer_p = pm.Deterministic('cancer_p', pm.math.switch(smoking, 0.3, 0.1))
    cancer = pm.Bernoulli('cancer', p=cancer_p)
    bronchitis_p = pm.Deterministic('bronchitis_p', pm.math.switch(smoking, 0.3, 0.1))
    bronchitis = pm.Bernoulli('bronchitis', p=cancer_p)

    xray_p = pm.Deterministic('xray_p', pm.math.switch(tuberculosis,
                                                      pm.math.switch(cancer, 0.9, 0.7),
                                                      pm.math.switch(cancer, 0.8, 0.1))
    )
    xray = pm.Bernoulli('xray', p=xray_p, observed=True)
    dyspnea_p = pm.Deterministic('dyspnea_p',
                                 pm.math.switch(tuberculosis,
                                                pm.math.switch(cancer,
                                                              pm.math.switch(bronchitis,
                                                                             1.0, 0.9),
                                                              pm.math.switch(bronchitis,
                                                                             0.8, 0.7)),
                                                pm.math.switch(cancer,
                                                              pm.math.switch(bronchitis,
                                                                             0.7, 0.5),
                                                              pm.math.switch(bronchitis,
                                                                             0.6, 0.1))))
    dyspnea = pm.Bernoulli('dyspnea', p=dyspnea_p, observed=True)

map_estimate = pm.find_MAP(model=basic_model)
print(map_estimate)
#exit()
print("=======================")
with basic_model:
    trace = pm.sample(100)
    # basic_model.observe("asia", value=True)
    print(pm.summary(trace, varnames=['tuberculosis', 'cancer', 'bronchitis']))
    for i, s in enumerate(trace.points()):
        print(i, s)
        if i > 2:
            break

    approx = pm.fit()
    trace = approx.sample(1000)
    print(pm.summary(trace, varnames=['tuberculosis', 'cancer', 'bronchitis']))
    # trace = pm.sample(100)
    pm.traceplot(trace, varnames=['xray_p', 'xray'])
    # print(pm.summary(trace));
    plt.show()
    # print(pm.find_MAP())
    
