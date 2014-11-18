__author__ = 'admin'
from recsys.algorithm.factorize import SVD
from recsys.datamodel.data import Data

svd = SVD()
data = Data()
data.load(path='../data/userchlfav',#
          force=True, sep=','
          , format={'col':0, 'row':1, 'ids': int} #, 'value':2
          , pickle=False)

print len(data._data)

for rate in data._data:
    rate[0]

data.set([rate for rate in data._data if rate[1]<1000])

print len(data._data)

svd.set_data(data)

k = 100
svd.compute(k=k,
            min_values=10,
            pre_normalize=None,
            mean_center=True,
            post_normalize=True)


#ITEMID1 = 1    # Toy Story (1995)
#ITEMID2 = 2355 # A bug's life (1998)

#print svd.similarity(ITEMID1, ITEMID2)
#print svd.similar(ITEMID1)

MIN_RATING = 0.0
MAX_RATING = 5.0
ITEMID = 1
USERID = 1

#print svd.predict(ITEMID, USERID, MIN_RATING, MAX_RATING)
# Predicted value 5.0
#print svd.get_matrix().value(ITEMID, USERID)
# Real value 5.0
print svd.recommend(USERID, is_row=False) #cols are users and rows are items, thus we set is_row=False
print svd.recommend(ITEMID)

