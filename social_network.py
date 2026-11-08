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

# Design Memo

# A graph is the best data structure for representing a social network because it naturally models people and their relationships. 
# In a graph, each person is represented as a node, while each friendship is represented as an edge connecting two nodes. 
# Since friendships are mutual, an undirected graph accurately represents these connections. 
# Using an adjacency list allows each person to maintain a list of the friends they are connected to, making the structure efficient and easy to understand.

# A list would not work as well because it only stores items in sequence and does not directly represent relationships between people. 
# Finding all of a person's friends would require additional structures and processing. A tree is also not ideal because trees require hierarchical parent-child relationships. 
# Social networks are not hierarchical. 
# People can have many friends and can belong to multiple interconnected groups, creating cycles that trees cannot easily accommodate.

# One trade-off I noticed was that creating a friendship requires updating both people's friend lists to keep the relationship bidirectional. 
# This adds a small amount of work compared to a one-way connection. However, using a dictionary to store people by name makes finding a person very efficient because dictionary lookups are generally O(1). 
# Printing the network requires traversing every person and every friendship, which becomes slower as the network grows. 
# Despite this, adjacency lists remain memory efficient because they only store existing friendships, unlike adjacency matrices that must allocate space for every possible connection. 
# Therefore, a graph implemented with adjacency lists is an effective solution for managing a social network.
