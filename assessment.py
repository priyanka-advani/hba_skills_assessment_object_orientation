"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Encapsulation:
   - data (objects) is bound to the functions that manipulate it (methods)
   - accessible (due to abstraction), but protected from external interference

   Abstraction:
   - internal code can be easily accessed by external code
   - not necessary to understand inner workings of methods
   - can focus on what an object does instead of how it does it

   Polymorphism:
   - flexibility of creating different types of the same object (subtypes)
   - can still utilize same functionality (methods)
   - functionality can have different implementations for different subtypes

2. What is a class?
    - object type to store data
    - like a template for creating objects (instances)
    - can create multiple instances of the same class

3. What is an instance attribute?
    - attribute bound to an individual object

4. What is a method?
    - way of interacting with objects within a particular class
    - will always have at least one parameter, self

5. What is an instance in object orientation?
    - an object that has all the functionality and attributes of the class

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   - class attributes are shared by all members of the class
   - instance attributes are bound to a particular instance
   - python will always search for an instance attribute before a class attribute
   - once it finds one, it won't search further, so instance attributes can
   override class attributes
   - instance attributes are useful when you want to store a list of items
   that can be edited for one instance without changing the list for another instance
   - class attributes are useful when you want to use a method from the parent
   class and want to pass in the same variable for all members in the subclass
"""


class Student(object):
    """Student."""

    def __init__(self, first_name, last_name, address):
        """Initialize student."""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __repr__(self):
        """Student description."""

        return '{} {}'.format(self.first_name, self.last_name)


class Question(object):
    """Questions."""

    def __init__(self, question, correct_answer):
        """Initialize question."""

        self.question = question
        self.correct_answer = correct_answer

    def __repr__(self):
        """Question text."""

        return '{}'.format(self.question)

    def ask_and_evaluate(self):
        """Print question, return True or False based on user answer."""

        return raw_input(self.question + ' > ') == self.correct_answer


class Exam(object):
    """Exam."""

    def __init__(self, name):
        """Initialize exam."""

        self.name = name
        self.questions = []

    def __repr__(self):
        """Exam name."""

        return '{}'.format(self.name)

    def add_question(self, question):
        """Adds a question to the exam's list of questions."""

        self.questions.append(question)

    def administer(self):
        """Administers all exam questions and returns user score."""

        user_correct_answers = 0

        for question in self.questions:
            if question.ask_and_evaluate() == True:
                user_correct_answers += 1

        return float(user_correct_answers) / len(self.questions) * 100


class StudentExam(object):
    """Exam for a student."""
    
    def __init__(self, student, exam):
        """Initialize exam for a student."""

        self.student = student
        self.exam = exam
        self.score = None

    def __repr__(self):
        """Student name, exam name, and score."""

        return 'Student: {}, exam: {}, score: {}'.format(self.student,
            self.exam, self.score)

    def take_test(self):
        """Administer exam and update score."""

        self.score = self.exam.administer()

        print repr(self)


def example():
    """Creates example exam and student, administers test to student."""

    midterm = Exam('midterm')

    q_a_list = {
        'What is the method for adding an element to a set?': '.add()',
        'What does pwd stand for?': 'print working directory',
        'Python lists are mutable, iterable, and what?': 'ordered'
        }

    for q, a in q_a_list.items():
        midterm.add_question(Question(q, a))

    student1 = Student('Jasmine', 'Debugger', '0101 Computer Street')

    student1_midterm = StudentExam(student1, midterm)

    student1_midterm.take_test()


class Quiz(Exam):
    """Like an exam, but pass/fail instead of percentage score."""

    def administer(self):
        """Administers all questions and returns pass/fail result."""

        return int(super(Quiz, self).administer() > 50)


class StudentQuiz(StudentExam):
    """Quiz for a student."""

    def __init__(self, student, exam):
        """Initialize exam for a student."""

        self.student = student
        self.exam = exam
        self.score = None
