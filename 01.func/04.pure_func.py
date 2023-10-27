

def say_prime_or_not(number):

    def prime_or_not(x):
        for a in range(2, int(x ** 0.5 + 1)):
            if x % a == 0:
                return False
        return True

    def say(n):
        if prime_or_not(n):
            print('yes')
        else:
            print('no')

    say(number)


say_prime_or_not(5)
