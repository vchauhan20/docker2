stop = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd",
        'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers',
        'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
        'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
        'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but',
        'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against',
        'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from',
        'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once',
        'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most',
        'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's',
        't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're',
        've', 'y',  'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',
        "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',
        "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren',
        "weren't", 'won', "won't", 'wouldn', "wouldn't"]


class TextSimilarity:
    def __init__(self, text):
        self.text = text
        self.tokens = None
        self.cleaned_tokens = None
        self.token_present = []
        self.stop = stop

    def create_tokens(self):
        self.tokens = self.text.split(' ')

    def remove_stop_words(self, stop_usage=1):
        if stop_usage:
            self.cleaned_tokens = {token for token in self.tokens if not token in self.stop}
        else:
            self.cleaned_tokens = set(self.tokens)

    def cosine_similar_score(self, second_obj):
        if self.text == second_obj.text:
            cosine_similarity_score = 1
        else:
            score = 0
            combined_tokens_set = list(self.cleaned_tokens.union(second_obj.cleaned_tokens))
            combined_tokens_set.sort()
            for token in combined_tokens_set:
                if token in self.tokens:
                    self.token_present.append(1)
                else:
                    self.token_present.append(0)
                if token in second_obj.tokens:
                    second_obj.token_present.append(1)
                else:
                    second_obj.token_present.append(0)

            for i in range(len(combined_tokens_set)):
                score += self.token_present[i] * second_obj.token_present[i]
            cosine_similarity_score = (score / float((sum(self.token_present) * sum(second_obj.token_present)) ** .5))
        return cosine_similarity_score




