import numpy as np

from math import sqrt
class searchOn:
    def __init__(self, index_dict):
        self.index = index_dict
    def compareWith(self, queryimage):
        result = {}
        for key, value in self.index.items():
            
            dist = self.metric(value, queryimage)
            result[key] = dist

        res1 = sorted([(v,k) for (k,v) in result.items()])
        return (res1)

    def metric(self, feat1, feat2, eps=1e-10):
        print(feat1, feat2, sep='\n')
        dist = (0.5*np.sum([((a-b)**2)/(a+b+eps) for (a,b) in zip(feat1,feat2)]))
        print(dist)
        return(dist)
