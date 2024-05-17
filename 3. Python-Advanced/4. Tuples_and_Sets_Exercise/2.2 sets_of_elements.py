n, m = map(int, input().split())

n_set = {input() for _ in range(n)}
m_set = {input() for _ in range(m)}

print(*n_set & m_set, sep="\n")