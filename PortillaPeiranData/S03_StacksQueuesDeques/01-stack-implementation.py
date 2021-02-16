from  PortillaPeiranData.S03_StacksQueuesDeques.stack import Stack

site_stack = Stack()

print('stack size: {}'.format(site_stack.size()))

site_stack.push('google.com')
site_stack.push('bestbuy.com')
site_stack.push('amazon.com')

print(site_stack.size())
print(site_stack.isEmpty())

print(site_stack.pop())

print(site_stack.size())