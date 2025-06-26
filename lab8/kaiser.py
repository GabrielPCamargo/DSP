from scipy.signal import kaiserord
A_s = 40
fs = 12000
fp = 1800
fst = 2000

width = 0.006666666666

##width = (2/fs)*(fst-fp)
N, beta = kaiserord(A_s, width)
print(f"Ordem estimada: {N}, beta: {beta}")