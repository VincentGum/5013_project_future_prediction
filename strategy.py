#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:27:48 2017

@author: MAngO
"""

from sklearn.externals import joblib

my_cash_balance_lower_limit = 3000000.
asset_index = 2


def train():
    pass


def handle_bar(timer, data, info, init_cash, transaction, detail_last_min, memory):
    position_new = detail_last_min[0]

    for index in range(13):
        # data[index] = data[index].reshape(1, -1)
        clf = joblib.load('svm_models/filename'+str(index)+'.pkl')
        value_predict = clf.predict(data[index].reshape(1, -1))
        if value_predict == 1:
            if detail_last_min[1] > my_cash_balance_lower_limit:
                position_new[asset_index] -= 10.

        elif value_predict == 0:
            if detail_last_min[1] > my_cash_balance_lower_limit:
                position_new[asset_index] += 10.

    return position_new, memory


if __name__ == '__main__':
    pass

