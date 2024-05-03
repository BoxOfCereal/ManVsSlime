
ticks=721
mins = (ticks/60)-((ticks/60)%1)
mins_tens= (mins/10)-((mins/10)%1)
mins_ones= mins%10
# mins_ones
secs = ticks%60
sec_tens= (secs/10)-((secs/10)%1)
sec_ones= secs%10  
print(f"min_tens: {mins_tens}, min_ones: {mins_ones}, sec_tens: {sec_tens}, sec_ones: {sec_ones}")