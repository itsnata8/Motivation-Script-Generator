from google import genai
import os
from dotenv import load_dotenv

class Backend:
    def __init__(self, data):
        print(data)
        content = f"""
        Buat naskah narasi motivasi berdurasi 30 detik untuk video dengan ketentuan berikut:

        Tema Utama:{data["temaUtama"]}
        Target Audiens:{data["targetAudiens"]}
        Poin-Poin Kunci (maksimal 3):
            1.  {data["poinKunci"][0]}
            2.  {data["poinKunci"][1]}
            3.  {data["poinKunci"][2]}
        Gaya Bahasa: {data["gayaBahasa"]}
        Kalimat Pembuka: {data["kalimatPembuka"]}
        Kalimat Penutup (Call to Action): {data["kalimatPenutup"]}
        Kata-kata Kunci: {data["kataKunci"]}
        Visualisasi yang Dibayangkan: {data["visualisasi"]}
        """
        print(content)
        # load_dotenv()
        # API = os.getenv("API_KEY")
        # client = genai.Client(api_key=API)

        # response = client.models.generate_content(
        # model="gemini-2.0-flash",
        # contents="Explain how AI works",
        # )

        # print(response.text)