import unittest
import Player
import PresidentGame

class TestCardsExercice2(unittest.TestCase):
    def test_player_constructor(self):
        player_trump = Player.Player('Trump')
        self.assertTrue(player_trump.getName() == 'Trump')

    def test_incognito_player_should_have_random_name(self):
        player_incognito = Player.Player()
        self.assertFalse(player_incognito.getName() == '')

    def test_default_game_has_three_players(self):
        game = PresidentGame.PresidentGame(["test1","test2","test3"])
        self.assertTrue(game.player_nbr == 3)

    def test_game_launch_distributes_cards(self):
        """ Game generation should distribute cards evenly. """
        game = PresidentGame.PresidentGame(["test1","test2","test3"])
        game.makeDeck()
        print("Players")
        print(len(game.players))
        player_1 = game.players[0]
        player_2 = game.players[1]
        print(player_1.getDeckOrganized())
        self.assertTrue(len(player_1.getDeckOrganized()) > 0)
        self.assertTrue(len(player_1.getDeckOrganized()) >= len(player_2.getDeckOrganized()))

if __name__ == '__main__':
    unittest.main()
