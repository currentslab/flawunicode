import os
import gzip
import json

path_dir = os.path.dirname(os.path.abspath(__file__))
neg_file_path = os.path.join(path_dir, 'resources', 'neg_freq_3gram.json.gz')
with gzip.open(neg_file_path, 'rb') as f:
    neg_freq_trigram = set(json.loads(f.read().decode('utf-8')))


pos_file_path = os.path.join(path_dir, 'resources', 'high_freq_2gram.json.gz')
with gzip.open(pos_file_path, 'rb') as f:
    high_freq_bigram = set(json.loads(f.read().decode('utf-8')))

def get_ngram(text, n=2):
    bigrams = [''.join(bi) for bi in zip(*[text[i:] for i in range(n)])]
    char_stats = set(bigrams)
    return char_stats


def calculate_intersection(text, truncate_size=2048):
    text = text.lower()[:truncate_size]
    bigrams = get_ngram(text)
    # add 1 to prevent division error
    denorm = (len(set(bigrams))+1)
    intersec = len(bigrams.intersection(high_freq_bigram))
    pos_ratio = intersec/denorm

    trigrams = get_ngram(text, n=3)
    neg_intersec = len(trigrams.intersection(neg_freq_trigram))
    neg_ratio = neg_intersec/(len(set(trigrams))+1)
    return pos_ratio-neg_ratio



