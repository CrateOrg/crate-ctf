import random
import sys
import select

class AnswerWrongException(Exception):
    pass


class AnswerTimeoutException(Exception):
    pass


class ProblemSolver:
    def __init__(self):
        self._FLAG = "Nature never uses prime numbers. But mathematicians do."
        #REPLACE_FLAG# #(placeholder for tools to automatically replace flag

    @staticmethod
    def send_comment(text):
        print(f"# {text}")

    def ask_problem(self, timeout, count_min, count_max, value_min, value_max):
        numbers = []
        count = random.randint(count_min, count_max)
        for i in range(count):
           numbers.append(random.randint(value_min, value_max))

        answer = sum(numbers)
        problem = str(numbers[0])
        for n in numbers[1:]:
            if n < 0:
                # minus sign is prepended automatically
                problem += format("%d" % n)
            else:
                # manually prepend plus sign
                problem += format("+%d" % n)
        print(problem)
        i, o, e = select.select([sys.stdin], [], [], timeout)
        if i:
            reply = sys.stdin.readline().strip("\r\n")
            if int(reply) == answer:
                return True
            else:
                raise AnswerWrongException
        else:
            raise AnswerTimeoutException


    def run(self):
        # Send some comments
        self.send_comment("Answer my questions and you will be rewarded in the end.")
        self.send_comment("Remember to answer before I get tired waiting!")
        self.send_comment("")
        self.send_comment("For example, the answer to the question '2+3+4' is '9'")
        self.send_comment("")
        self.send_comment("We will begin with some simple additions!")
        self.send_comment("Shout READY to go!")

        data = sys.stdin.readline()
        if "READY" not in data:
            self.send_comment("ok bye")
            return

        try:
            # easy ones that can be done manually
            for j in range(3):
                self.ask_problem(10.0, 2, 2, 0, 10)

            # harder ones with larger numbers but still time to do copy-n-paste for calculation
            for j in range(3):
                self.ask_problem(10.0, 7, 7, 0, 1000)

            # harder ones with larger numbers, but 2 sec timeout
            for j in range(3):
                self.ask_problem(2.0, 5, 10, 0, 1000)

            # finally, harder ones with larger numbers, 2 sec timeout and both positive and negative numbers
            for j in range(3):
                self.ask_problem(2.0, 5, 10, -1000, 1000)

            # Give the flag
            self.send_comment("You have proven yourself WORTHY! Here is the flag:")
            self.send_comment(self._FLAG)

        except AnswerTimeoutException as e:
            self.send_comment("sorry, time's up!")
            return
        except AnswerWrongException as e:
            self.send_comment("sorry, wrong answer!")
            return
        except Exception as e:
            self.send_comment("unexpected input")
            return

def main():
    problem_solver = ProblemSolver()
    problem_solver.run()

if __name__ == "__main__":
    main()
