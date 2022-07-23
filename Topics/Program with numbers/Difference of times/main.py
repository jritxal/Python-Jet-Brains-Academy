# put your python code here
h_1 = int(input())
m_1 = int(input())
s_1 = int(input())
h_2 = int(input())
m_2 = int(input())
s_2 = int(input())
seconds = (h_2 - h_1) * 60
seconds = (seconds + (m_2 - m_1)) * 60
seconds += s_2 - s_1
print(seconds)
