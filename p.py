import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


# Fungsi untuk menghitung penguatan tegangan
def calculate_voltage_gain(rb1, rb2, rc, re, coupling1, rb, coupling2, rl, vin):
    # Menghitung penguatan tegangan pada tingkat pertama
    voltage_gain1 = - (rc / re) * (1 + (rb2 / (rb1 + rb2)))
    
    # Menghitung penguatan tegangan pada tingkat kedua
    voltage_gain2 = - (rl / re) * (1 + (rb / (rb + (1 + (rc / re)) * rb)))
    
    # Menghitung penguatan tegangan total
    total_gain = voltage_gain1 * voltage_gain2
    
    # Menghitung tegangan output
    vout = vin * total_gain
    
    return voltage_gain1, voltage_gain2, total_gain, vout

# Fungsi untuk menghitung penguatan arus
def calculate_current_gain(rb1, rb2, rb):
    # Menghitung penguatan arus pada tingkat pertama
    current_gain1 = (rb1 + rb2) / rb2
    
    # Menghitung penguatan arus pada tingkat kedua
    current_gain2 = (rb + (1 + (rc / re)) * rb) / rb
    
    return current_gain1, current_gain2

# Fungsi untuk menghitung impedansi input
def calculate_input_impedance(rb1, rb2, coupling1):
    input_impedance1 = (1 + (rb1 + rb2) / rb2) * coupling1
    
    return input_impedance1

# Fungsi untuk menghitung impedansi output
def calculate_output_impedance(rl, coupling2):
    output_impedance2 = (1 + (rb + (1 + (rc / re)) * rb) / rb) * coupling2
    
    return output_impedance2

# Fungsi untuk menghitung sinyal output
def calculate_output_signal(input_signal, voltage_gain1, voltage_gain2):
    output_signal = input_signal * voltage_gain1 * voltage_gain2
    
    return output_signal

# Fungsi untuk menampilkan tampilan sinyal input dan output
def plot_signals(input_signal, output_signal):
    time = np.linspace(0, 1, len(input_signal))
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
    ax1.plot(time, input_signal, label='Sinyal Input')
    ax1.set_xlabel('Waktu (detik)')
    ax1.set_ylabel('Amplitudo (Volt)')
    ax1.legend()
    
    ax2.plot(time, output_signal, label='Sinyal Output')
    ax2.set_xlabel('Waktu (detik)')
    ax2.set_ylabel('Amplitudo (Volt)')
    ax2.legend()
    
    plt.tight_layout()
    st.pyplot(fig)

# Judul aplikasi
st.header('TUGAS BESAR ELEKTRONIKA ANALOG')
st.header('Institut Teknologi Nasional Bandung')
st.header('Dosen : Ir. Rustamaji, M.T')
st.header('Tiara Adinda (11-2021-042)')

#judul aplikasi 2
st.title('Analisis Penguatan Rangkaian Bertingkat Transistor')

st.title("Contoh Rangkaian Penguatan Bertingkat")
st.image("PP (2).jpeg", width = 500)

# Input nilai komponen tingkat pertama
st.header('Input Nilai Komponen Tingkat Pertama')
rb1 = st.number_input('Resistor Base 1 (ohm)')
rb2 = st.number_input('Resistor Base 2 (ohm)')
rc = st.number_input('Resistor Kolektor (ohm)')
re = st.number_input('Resistor Emitter (ohm)')
coupling1 = st.number_input('Kapasitor Bypass Emitter (F)')

# Input nilai komponen tingkat kedua
st.header('Input Nilai Komponen Tingkat Kedua')
rb = st.number_input('Resistor Base (ohm)')
coupling2 = st.number_input('Kapasitor Bypass Base (F)')
rl = st.number_input('Resistor Load (ohm)')

# Input tegangan input
st.header('Input Tegangan Input')
vin = st.number_input('Tegangan Input (V)')

# input sinyal frekuensi
input_signal_frequency = st.number_input('Frekuensi Sinyal Input (Hz)')

# Tombol untuk menghitung
if st.button('Hitung'):
    # Menghitung penguatan tegangan
    voltage_gain1, voltage_gain2, total_gain, vout = calculate_voltage_gain(rb1, rb2, rc, re, coupling1, rb, coupling2, rl, vin)
    
    # Menghitung penguatan arus
    current_gain1, current_gain2 = calculate_current_gain(rb1, rb2, rb)
    
    # Menghitung impedansi input
    input_impedance1 = calculate_input_impedance(rb1, rb2, coupling1)
    
    # Menghitung impedansi output
    output_impedance2 = calculate_output_impedance(rl, coupling2)
    
    # Menghitung sinyal input
    time = np.linspace(0, 1, 1000)
    input_signal = vin * np.sin(2 * np.pi * input_signal_frequency * time)
    
    # Menghitung sinyal output
    output_signal = calculate_output_signal(input_signal, voltage_gain1, voltage_gain2)
    
    # Menampilkan hasil analisis
    st.header('Hasil Analisis')
    st.subheader('Penguatan Tegangan')
    st.write('Penguatan Tegangan Pertama:', voltage_gain1)
    st.write('Penguatan Tegangan Kedua:', voltage_gain2)
    st.write('Penguatan Tegangan Total:', total_gain)
    
    st.subheader('Penguatan Arus')
    st.write('Penguatan Arus Pertama:', current_gain1)
    st.write('Penguatan Arus Kedua:', current_gain2)
    
    st.subheader('Impedansi Input')
    st.write('Impedansi Input Pertama (ohm):', input_impedance1)
    
    st.subheader('Impedansi Output')
    st.write('Impedansi Output Kedua (ohm):', output_impedance2)
    
    st.subheader('Tampilan Sinyal')
    plot_signals(input_signal, output_signal)
