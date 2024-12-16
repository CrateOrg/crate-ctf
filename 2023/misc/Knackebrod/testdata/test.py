import unittest
from subprocess import Popen, PIPE, STDOUT

def run_with_input(filename, in_data):
    p = Popen(['python3', "../docker/challenge.py", filename], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    return p.communicate(input=in_data.encode())[0].decode("ascii")

class TestHashCrackingThing(unittest.TestCase):

    def test_can_get_flag(self):
        in_data = "e38ad214943daad1d64c102faec29de4afe9da3d:password1\n" \
                  "2aa60a8ff7fcd473d321e0146afd9e26df395147:password2\n" \
                  "1119cfd37ee247357e034a08d844eea25f6fd20f:password3\n" \
                  "a1d7584daaca4738d499ad7082886b01117275d8:password4\n" \
                  "edba955d0ea15fdef4f61726ef97e5af507430c0:password5\n" \
                  "6d749e8a378a34cf19b4c02f7955f57fdba130a5:password6\n"
        output = run_with_input("10_hashes_password1_to_password10", in_data)

        self.assertIn("Amazing!", output)

    def test_fail_to_get_flag(self):
        in_data = "e38ad214943daad1d64c102faec29de4afe9da3d:password1\n" \
                  "2aa60a8ff7fcd473d321e0146afd9e26df395147:password2\n" \
                  "edba955d0ea15fdef4f61726ef97e5af507430c0:password5\n" \
                  "6d749e8a378a34cf19b4c02f7955f57fdba130a5:password6\n"
        output = run_with_input("10_hashes_password1_to_password10", in_data)

        self.assertIn("Sadly,", output)

    def test_multiline_cheat(self):
        in_data = "e38ad214943daad1d64c102faec29de4afe9da3d:password1\n" \
                  "2aa60a8ff7fcd473d321e0146afd9e26df395147:password2\n" \
                  "2aa60a8ff7fcd473d321e0146afd9e26df395147:password2\n" \
                  "  \t  2aa60a8ff7fcd473d321e0146afd9e26df395147:password2\t  \t\n" \
                  "2aa60a8ff7fcd473d321e0146afd9e26df395147:  password2\n" \
                  "    2aa60a8ff7fcd473d321e0146afd9e26df395147:password2\n" \
                  "2aa60a8ff7fcd473d321e0146afd9e26df395147:password2   \n" \
                  "\t 2aa60a8ff7fcd473d321e0146afd9e26df395147 :password2\t\n"
        output = run_with_input("10_hashes_password1_to_password10", in_data)
        duplicate_count = output.count("You have already sent the line")
        self.assertIn("Sadly,", output)
        self.assertIn("2 out of 10 targets", output)
        self.assertEqual(duplicate_count, 6)

    def test_hash_not_in_file(self):
        in_data = "2aa60a8ff7fcd473d321e0146afd9e26df395147:password2\n"
        output = run_with_input("password1_hash", in_data)
        self.assertIn("Sadly,", output)
        self.assertIn("does not appear to be valid", output)

if __name__ == '__main__':
    unittest.main()
