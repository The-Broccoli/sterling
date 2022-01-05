import re

class BadWords():

    def __init__(self):

        self.bad_words = [
            r'[f][u][c][k]',
            r'[s][h][i][t]',
            r'[a][s][s]',
            r'[b][i][t][c][h]',
            r'[h][u][r][e][n][s][o][h][n]']
    
    def forbidden_words(self, message):
        for word in self.bad_words:
            if re.search(word, message):
                return True
        return False