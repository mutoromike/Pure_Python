""""
Sets manipulation:
    Write a function named covers that accepts a single parameter,
    a set of topics. Have the function return a list of
    courses from COURSES where the supplied set and the course's
    value (also a set) overlap.
    For example, covers({"Python"}) would return ["Python Basics"].
"""

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

