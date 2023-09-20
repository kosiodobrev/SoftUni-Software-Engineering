v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

pipe_1 = p1 * h
pipe_2 = p2 * h
pool_fullness = pipe_1 + pipe_2
pool_fullness_prozent = (pool_fullness / v) * 100
pool_overflow_proznet = ((pipe_1 + pipe_2) - v)
pipe_1_prozent = (pipe_1 / pool_fullness) * 100
pipe_2_prozent = (pipe_2 / pool_fullness) * 100

if pool_fullness <= v:
    print(f"The pool is {pool_fullness_prozent:.2f}% full. Pipe 1: {pipe_1_prozent:.2f}%. Pipe 2: {pipe_2_prozent:.2f}%.")
elif pool_fullness > v:
    print(f"For {h:.2f} hours the pool overflows with {pool_overflow_proznet:.2f} liters.")