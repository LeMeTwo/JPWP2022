import yfinance as yf
import 3matplotlib.pyplot as plt

'''
Chcemy napisać funkcję, która obliczy i zwróci skumulowane zwroty z inwestycji 1$ w akcję Cisco Systems. 
Przygotowano szkielet programu. Napisz funkcję cumulative_returns tak aby realizowała następujące kroki:
    - zaciągnięcie za pomocą modułu yfinance danych giełdowych dla tickera (argument funckcji) z ostatnich 6 miesięcy.
    - obliczenie procentowych zmian ceny zamknięcia dla rozpatrywanego okresu.
    - obliczenie skumulowanego iloczynu (skorzystaj z jednej z funkcji modułu numpy) z uzyskanych procentowych zmian powiększonych o 1 (co oznacza inwestycję 1$)   
    - usunięcie wszystkich wartości nan - możesz skorzystać z funckji dropna()
    - zwrócenie otrzymanych wartości skumulowanych zwrotów
Po uruchomieniu programu powinien pokazać się wykres, który przedstawia zmiany wartości zaiwestowanego 1$ w okresie 6 miesięcy. 
Powodzenia!
'''

def cumulative_returns(ticker):
    # tutaj napisz swój kod
    data = yf.Ticker('CSCO')
    print = data.history(period="6mo")
    x = price["Close"].pct_change()
    returns = (x+1).cumprod()
    return = returns.dropna()
    return returns


if __name__ == "__main__":

    data = cumulative_returns('CSC0')
    data.plot()
    plt.show()