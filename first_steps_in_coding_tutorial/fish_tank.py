duljina = int(input())
shirochina = int(input())
visochina = int(input())
procent = float(input()) / 100

obem = ((duljina * shirochina * visochina) / 1000)
final_result = obem - (obem * procent)
print(final_result)
