import re

CATCH_WORD_TO_PRONOUNS = {
    'he/she': ['he', 'she'],
    'him/her': ['him', 'her'],
    'his/her': ['his', 'her'],
    'they': ['he', 'she'],
    'he': ['he', 'she'],
    'she': ['he', 'she'],
    'them': ['him', 'her'],
    'him': ['him', 'her'],
    'his': ['him', 'her'],
    'her': ['him', 'her']

}


def get_masked_str_and_targets(text):
    text_words = text.split(' ')
    masked_str_and_targets = []
    for i in range(len(text_words)):
        pronouns = CATCH_WORD_TO_PRONOUNS.get(text_words[i], None)
        if pronouns:
            masked_str = ' '.join(
                text_words[:i] + ['[MASK]'] + text_words[i + 1:])
            yield (masked_str, pronouns)
