h, m = map(int, input().split())
cook = int(input())

m_tot = m+cook
if m_tot >= 60:
    h += m_tot//60
    m_tot = m_tot % 60
    if h >= 24:
        h %= 24
    print(h, m_tot)
else:
    print(h, m_tot)
