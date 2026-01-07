def fizzbuzz(n):
    """
    Convert a number to it`s name in the game FizzBuzz
    """
    answer = ""
    rules = {3: "Fizz", 5: "Buzz"}
    for divisor in sorted(rules.keys()):
        if n % divisor == 0:
            answer += rules[divisor]
    if not answer:
        answer = str(n)
    return answer
