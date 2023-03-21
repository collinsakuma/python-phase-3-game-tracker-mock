from classes.result import Result

class Game:
    def __init__(self, title):
        if type(title) == str and 0 < len(title):
            self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not hasattr(self, "_title"):
            self._title = title
        else:
            print("cannot change title")

    def results(self):
        results_list = []
        for result in Result.all:
            if result.game == self:
                results_list.append(result)
        return results_list

    def players(self):
        games_list = []
        for result in self.results():
            games_list.append(result.player)
        return games_list
    
    def average_score(self, player):
        score = 0
        for result in self.results():
            score += result.score
        return score / len(self.results())
