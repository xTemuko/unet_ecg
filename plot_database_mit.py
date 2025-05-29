import wfdb
import matplotlib.pyplot as plt

#registro_path = r'C:\Users\mruiz\Projects\ecg_project\mit-bih-normal-sinus-rhythm-database-1.0.0\16272'
registro_path = r'C:\Users\mruiz\Projects\ecg_project\mit-bih-arrhythmia-database-1.0.0\101'
record = wfdb.rdrecord(registro_path)
annotation = wfdb.rdann(registro_path, 'atr')


#print(record)
#print(annotation)
print(len(record.p_signal))        
print(len(record.fs))               
print(annotation.sample)       
print(annotation.symbol)      



# Suponiendo que hemos leído el registro '100'
plt.figure(figsize=(16, 4))
plt.plot(record.p_signal[:, 0])  # Graficar canal 0 (MLII)
plt.title('ECG del registro 100 (canal MLII)')
plt.xlabel('Muestras')
plt.ylabel('mV (aprox.)')
plt.show()
