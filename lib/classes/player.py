from classes.result import Result

class Player:
    def __init__(self, username):
        self.username = username
    
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if( type(username) and (2 <= len(username) <= 16)):
            self._username = username
        else:
            print('Username must be string and between 2 and 16 characters')

    def results(self):
        results_list = []
        for result in Result.all:
            if result.player == self:
                results_list.append(result)
        return results_list

    def games_played(self):
        games_list = []
        for result in self.results():
            games_list.append(result.game)
        return games_list
            
    def played_game(self, game):
        if game in self.games_played():
            return True
        else:
            return False

    def num_times_played(self, game):
        count = 0
        for played_game in self.games_played():
            if played_game == game:
                count += 1
        return count

    def add_result(self, game, score):
        Result(self, game, score)