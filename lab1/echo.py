import scipy.io.wavfile
import scipy.signal
import matplotlib.pyplot as plt 
import sounddevice as sd
import numpy as np 

# Carregar o arquivo de áudio
filename = './vogais.wav'
fs, wave = scipy.io.wavfile.read(filename)

# Verificar se o áudio tem mais de um canal (estéreo) e converter para mono, se necessário
if wave.ndim > 1:
    wave = np.mean(wave, axis=1)  # Converte estéreo para mono

# Informações do áudio
print('Sampling rate:', fs)
print('Audio length:', len(wave)/fs, 'seconds')
print('Lowest amplitude:', np.min(wave))
print('Highest amplitude:', np.max(wave))

# Tocar o áudio original
print("Reproduzindo áudio original...")
sd.play(wave, fs)
sd.wait()  # Espera o áudio terminar antes de continuar

#####################
###### APLICANDO O ECO
#####################
alpha = 0.8  # Intensidade do eco (ajuste para testar)
D = int(fs * 0.3)  # Atraso de 300ms (fs * tempo_em_segundos)
b = np.zeros(D+1)  # Criando vetor de coeficientes do filtro
b[0] = 1
b[D] = alpha

# Aplicando o filtro FIR para criar o eco
saida = scipy.signal.lfilter(b, 1, wave)  

# Normalizar e converter para int16 para evitar distorção
saida = np.int16(saida / np.max(np.abs(saida)) * 32767)

# Reproduzir o áudio com eco
print("Reproduzindo áudio com eco...")
sd.play(saida, fs)
sd.wait()  # Aguarda o áudio terminar antes de encerrar o script
