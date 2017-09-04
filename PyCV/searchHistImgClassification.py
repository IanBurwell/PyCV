import numpy as np
import _pickle
import descriptors
import cv2

class Search:
    def __init__(self, index):
        self.index = index

    def search(self, searchFeatures):

        results = {}

        for k,features in self.index.items():
            #replace features with distances
            d = self.distance(features, searchFeatures)
            results[k] = d
        #sort imgs so small distances are towards begginning
        results = sorted([(v,k) for (k,v) in results.items()])

        return results

    def distance(self, histA, histB):
        #this super small value stops devide by zero errors
        eps = 1e-10
        # compute the chi-squared distance (wtf)
        return 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(histA, histB)])


dataStore = "C:/Users/ian/Desktop/PyCV/PyCV/Resources/data/HistClassData"
searchImg = "C:/Users/ian/Desktop/PyCV/PyCV/Resources/pictures/search.jpg"
index = _pickle.loads(open(dataStore, "rb").read())
searcher = Search(index)

desc = descriptors.RGBHist([8,8,8])
searched = cv2.imread(searchImg)
results = searcher.search(desc.describe(searched))
    
cv2.imshow("Query", searched)  
resultImg = None
for j in range(5):
    (score, imageKey) = results[j]
    print(imageKey)
    path = "C:/Users/ian/Desktop/PyCV/PyCV/Resources/pictures/" + imageKey
    if resultImg is not None:
        resultImg = np.concatenate((resultImg, cv2.resize(cv2.imread(path),(300, 168))), axis=1) 
    else:
        resultImg = cv2.resize(cv2.imread(path),(300, 168))
    
cv2.imshow("Results", resultImg)
cv2.waitKey(0)


