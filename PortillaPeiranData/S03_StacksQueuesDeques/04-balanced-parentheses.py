from PortillaPeiranData.S03_StacksQueuesDeques.stack import Stack
from nose.tools import assert_equal

def balance_check(s):
    if len(s)%2 != 0:
        return False

    opening = set('({[')

    matches = set(['()','{}','[]'])

    stack = Stack()

    for paren in s:
        if paren in opening:
            stack.push(paren)
        else:
            if stack.size() == 0:
                return False
            else:
                last_open = stack.pop()

                if last_open + paren not in matches:
                    return False

    return stack.size() == 0



"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
class TestBalanceCheck(object):

    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print('ALL TEST CASES PASSED')

# Run Tests

t = TestBalanceCheck()
t.test(balance_check)
