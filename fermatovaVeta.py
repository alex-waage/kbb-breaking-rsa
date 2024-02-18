# funkce isqrt, nalezená na internetu
def isqrt(n):
	x = n
	y = (x + n // x) //2
	while(y < x):
		x = y
		y = (x + n // x) //2
	return x

def fermatovaVeta(n):
    a = isqrt(n) + 1
    for counter in range(0, n):
        b = a + counter
        temp = isqrt(b * b - n)
        if temp * temp == b * b - n:
            s = temp
            p = b + s
            q = b - s
            return p, q
    return None, None

print("Vložte číslo pro faktorizaci: ")
n = int(input())
p, q = fermatovaVeta(n)
print("p : ",int(p))
print("q : ",int(q))