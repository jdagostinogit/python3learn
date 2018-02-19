
message = input("What is message to print? ")
count = input("How many times would you like to print your message? ").strip()

if count:
    count = int(count)
else:
    count = 1


def multi_echo(message, count):
    while count > 0:
        print(message)
        count -= 1

multi_echo(message, count)
