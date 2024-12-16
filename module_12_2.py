import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Runner: {self.name}>'

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Usain", speed=10)
        self.andrey = Runner("Andrey", speed=9)
        self.nick = Runner("Nick", speed=3)

    @classmethod
    def tearDownClass(cls):
        print("\nAll results:")
        for key, value in cls.all_results.items():
            formatted_value = {k: str(v) for k, v in value.items()}
            print(f"{key}: {formatted_value}")

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.all_results["usain_and_nick"] = result
        last_runner = max(result.keys())
        self.assertTrue(result[last_runner].name == "Nick")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results["andrey_and_nick"] = result
        last_runner = max(result.keys())
        self.assertTrue(result[last_runner].name == "Nick")

    def test_all_three(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        self.all_results["all_three"] = result
        last_runner = max(result.keys())
        self.assertTrue(result[last_runner].name == "Nick")


if __name__ == "__main__":
    unittest.main()
