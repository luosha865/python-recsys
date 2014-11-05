__author__ = 'admin'
from recsys.algorithm.factorize import SVD


svd = SVD()
svd.load_data(filename='./data/movielens/ratings.dat',
            sep='::',
            format={'col':0, 'row':1, 'value':2, 'ids': int})

k = 100
svd.compute(k=k,
            min_values=10,
            pre_normalize=None,
            mean_center=True,
            post_normalize=True,
            savefile='/tmp/movielens')

ITEMID1 = 1    # Toy Story (1995)
ITEMID2 = 2355 # A bug's life (1998)

print svd.similarity(ITEMID1, ITEMID2)
print svd.similar(ITEMID1)

MIN_RATING = 0.0
MAX_RATING = 5.0
ITEMID = 1
USERID = 1

print svd.predict(ITEMID, USERID, MIN_RATING, MAX_RATING)
# Predicted value 5.0
print svd.get_matrix().value(ITEMID, USERID)
# Real value 5.0
print svd.recommend(USERID, is_row=False) #cols are users and rows are items, thus we set is_row=False
print svd.recommend(ITEMID)