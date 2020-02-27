from player import Player

SPACE_ADDED = 5


class Team:
    """A class representing a dodgeball team"""
    # All methods in Python include arguments representing the object
    # itself. In the method definition, this is represented by the
    # `self` parameter.
    def __init__(self):
        self.name = "Anonymous Team"
        self.players = []

    # Another example of self. The method call only passes one argument,
    # the 'name; value. But the method definition must always include the
    # self parameter.
    def set_team_name(self, name):
        # set the team name
        self.name = name

    # Note again that `self` is the first parameter.
    def add_player(self, player_name, player_number, player_position):
        # call the Player class constructor with the appropriate
        # values to create a new player object, then add that
        # player object to the team's players list.
        player = Player(player_name, player_number, player_position)
        self.players.append(player)

    def cut_player(self, player):
        # Remove the player from the players list.
        self.players.remove(player)

    def is_position_filled(self, position):
        # Write the method that checks whether
        # there is currently at least one player on the team
        # occupying the requested position

        for player in self.players:
            if player.position == position:
                return True
        return False

    def find_player(self, name):
        # find if the player already exists
        for player in self.players:
            if player.name == name:
                return player

    # Write any necessary methods to support the methods
    # above, and write the method that will display (print to screen)
    # the full team roster in the following format:
    def print_roster(self):
        print(f"The lineup for {self.name} is:")
        try:

            # find max lenth of player's name and number for formatting purpose
            max_number = max(len(player.number) for player in self.players)
            max_name = max(len(player.name) for player in self.players)

            for player in self.players:
                # formating
                number_output = player.number.ljust(max_number + SPACE_ADDED)
                name_output = player.name.ljust(max_name + SPACE_ADDED)
                print(f"{number_output}{name_output}{player.position}")
        except ValueError:
            print("The team currently has no players")
