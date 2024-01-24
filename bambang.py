import streamlit as st
from IPython.display import display, HTML
import threading

# Membuat area teks Streamlit untuk input kode Python
code_input = st.text_area("Masukkan kode Python di sini:")
run_button = st.button("Jalankan")
stop_button = st.button("Hentikan")

# Flag untuk menandakan apakah kode sedang berjalan
code_running = False

# Fungsi untuk mengeksekusi kode dalam thread terpisah
def execute_code():
    global code_running
    code_running = True
    try:
        exec(code_input)
    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        code_running = False

# Penangan acara untuk tombol "Jalankan"
if run_button and not code_running:
    thread = threading.Thread(target=execute_code)
    thread.start()

# Penangan acara untuk tombol "Hentikan"
if stop_button and code_running:
    st.warning("Menghentikan eksekusi... (Catatan: Penghentian mungkin tidak seketika)")
    # Anda mungkin perlu meningkatkan bagian ini tergantung pada kasus penggunaan spesifik

# Menampilkan hasil atau pesan kesalahan jika kode tidak sedang berjalan
if not code_running:
    st.text("Eksekusi selesai atau belum dimulai.")
