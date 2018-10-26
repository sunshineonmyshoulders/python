import sys

h1 = int(sys.argv[1])
m1 = int(sys.argv[2])
s1 = int(sys.argv[3])
h2 = int(sys.argv[4])
m2 = int(sys.argv[5])
s2 = int(sys.argv[6])

h_result = h1 + h2
m_result = m1 + m2
s_result = s1 + s2
d_result = 0

if s_result >= 60:
	s_result-= 60
	m_result+= 1

if m_result >= 60:
	m_result-= 60
	h_result+= 1

if h_result > 24:
	h_result-= 24
	d_result+= 1


print(h1, m1, s1)
print(h2, m2, s2)
print("#############")
print(d_result, h_result, m_result, s_result)

