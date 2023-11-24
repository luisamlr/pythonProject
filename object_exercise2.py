class AgeAnalyzer:
    def __init__(self, age):
        self.age = age
        self.voting_age = 18
        self.retirement_age = 65

    def can_vote(self):
        return self.age >= self.voting_age

    def until_retire(self):
        return max(0, self.retirement_age - self.age)


# This class, AgeAnalyzer, takes an age as an argument when instantiated. It has two methods, can_vote and
# until_retire, which correspond to your previous functions.

# we could add an example now
# the example goes into name == main; because a lot of times you want to import and if you send the file to somebody
# else, they only want the functions to use them
# like mentioned before, this indicates an example so it can be called by other people


if __name__ == '__main__':
    # This will call the function input_names_scores() in the object initialization
    fs = FootballScorer()
    # and then calculate_points()
    fs.calculate_points()
    # and then print using the reserved method __str__()
    print(fs)
    # This will directly input the names and scores in the object initialization
    fs2 = FootballScorer('t1', 't2', 1, 2)
    fs2.calculate_points()
    print(fs2)
