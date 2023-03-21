class Result:
    
    all = []
    
    def __init__(self, player_instance, game_insance, score):
        self.player = player_instance
        self.game = game_insance
        self.score = score
        Result.all.append(self)

    @property 
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if type(score) == int and 1 <= score <= 5000:
            self._score = score
