# social_network.py

class Person:
    """
    Represents a person in the social network.
    """

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        """
        Adds a friend to this person's friend list
        if they are not already friends.
        """
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    """
    Represents the social network graph using
    an adjacency list.
    """

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        """
        Creates and stores a new person.
        """
        if name in self.people:
            print(f"{name} already exists in the network.")
        else:
            self.people[name] = Person(name)
            print(f"{name} added to the network.")

    def add_friendship(self, person1_name, person2_name):
        """
        Creates a bidirectional friendship
        between two people.
        """

        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

        print(f"Friendship created between {person1_name} and {person2_name}.")

    def print_network(self):
        """
        Prints every person and all of their friends.
        """

        print("\nSOCIAL NETWORK")
        print("-" * 50)

        for person in self.people.values():
            friend_names = [friend.name for friend in person.friends]

            if friend_names:
                print(
                    f"{person.name} is friends with: "
                    f"{', '.join(friend_names)}"
                )
            else:
                print(f"{person.name} has no friends.")


# --------------------------------------------------
# TESTING
# --------------------------------------------------

network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Edge Case #1: Duplicate person
network.add_person("Alex")

# Create friendships (8 total)
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

# Edge Case #2: Person doesn't exist
network.add_friendship("Jordan", "Johnny")

# Edge Case #3: Print network
network.print_network()
