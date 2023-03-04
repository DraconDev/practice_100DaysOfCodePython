import random

import pandas

# quotes = pandas.read_csv('./quotes.csv', delimiter='-')
# quotes = pandas.read_csv('./data/quotes.csv', sep='-')
quotes = pandas.read_csv('./data/quotes.csv', names=['quotes'])
# quotes = pandas.Series(quotes)


def rand_quote():
    # * select specific emelent at cross of labels
    # return quotes.at[random.randint(0, len(quotes)), 'quotes']
    # * select column then random samples 0 index
    return quotes['quotes'].sample().iloc[0]


print(rand_quote())
# print(quotes)
