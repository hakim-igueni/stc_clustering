# -*- coding: utf-8 -*-

import numpy as np
from sklearn.metrics import normalized_mutual_info_score

nmi = normalized_mutual_info_score


def acc(y_true, y_pred):
    y_true = y_true.astype(np.int64)
    assert y_pred.size == y_true.size
    D = max(y_pred.max(), y_true.max()) + 1
    w = np.zeros((D, D), dtype=np.int64)
    for i in range(y_pred.size):
        w[y_pred[i], y_true[i]] += 1
        
    from scipy.optimize import linear_sum_assignment as linear_assignment
    row_ind, col_ind = linear_assignment(w.max() - w)
    inds = [w[i, j] for i, j in zip(row_ind, col_ind)]

    return sum(inds) * 1.0 / y_pred.size
