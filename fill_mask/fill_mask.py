# importing libraries
from transformers import pipeline
import wiki_scraper
import gender_bias
import numpy as np

# defining a function to obtain results. arguments passed are url and unmasker


def get_results_for_url(url, unmasker):
    '''defining a variable to get chunks of text from the urls provided 
    and wikiscraper is used to extract data from the wikipedia sites'''
    text_chunks = wiki_scraper.get_text_chunks_from_url(url)
    for text_chunk in text_chunks:
        masked_str_and_targets = gender_bias.get_masked_str_and_targets(
            text_chunk)
        for masked_str, targets in masked_str_and_targets:
            results = unmasker(masked_str, targets=targets)
            # making sure that the length of results is 2
            assert (len(results) == 2)
            yield results  # returns the results


def collect_statistics_from_results(results, output_score_statistics):
    assert (len(results) == 2)
    output_score_statistics.setdefault('score_ratios', []).append(
        results[0]['score'] / results[1]['score'])
# setdefault = returns the value of the item with the key
# append = adds the specified elemnt to the list


def get_statistics_for_urls(urls, unmasker):
    score_statistics = {}
    for url in urls:
        results = get_results_for_url(url, unmasker)
        for result in results:
            collect_statistics_from_results(result, score_statistics)
    return score_statistics


urls = [
    'https://en.m.wikipedia.org/wiki/Engineer',
    'https://en.wikipedia.org/wiki/Chief_executive_officer',
    'https://en.wikipedia.org/wiki/Police_officer',
    'https://en.wikipedia.org/wiki/Technician',
    'https://en.wikipedia.org/wiki/Aircraft_pilot',
    'https://en.wikipedia.org/wiki/Author',
    'https://en.wikipedia.org/wiki/Businessperson']
unmasker = pipeline('fill-mask', model='distilbert-base-uncased')
score_statistics = get_statistics_for_urls(urls, unmasker)
print(
    'count={0}, mean={1}, median={2}'.format(
        len(score_statistics['score_ratios']),
        np.mean(score_statistics['score_ratios']),
        np.median(score_statistics['score_ratios'])))
