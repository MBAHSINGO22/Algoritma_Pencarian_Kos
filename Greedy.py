from docx import Document


def baca_kos_dari_word(file_path):
    doc = Document(file_path)
    kos_list = []

    for table in doc.tables:
        for row in table.rows[1:]:
            nama = row.cells[0].text.strip()
            harga = int(row.cells[1].text.strip())
            jarak = int(row.cells[2].text.strip())
            kos_list.append({"nama": nama, "harga": harga, "jarak": jarak})

    return kos_list


def cari_kos_terbaik(file_path):
    kos_list = baca_kos_dari_word(file_path)

    print("=== Filter Kos yang Valid (harga ≤ 500000 dan jarak ≤ 450) ===")
    C = []
    for kos in kos_list:
        print(
            f"Memeriksa: {kos['nama']} (Harga: {kos['harga']}, Jarak: {kos['jarak']})"
        )
        if kos["harga"] <= 500000 and kos["jarak"] <= 450:
            print("  => VALID, ditambahkan ke kandidat")
            C.append(kos)
        else:
            print("  => Tidak valid")

    S = None
    print("\n=== Pemilihan Kos Terbaik Berdasarkan Harga Termurah ===")
    while C:
        x = min(C, key=lambda kos: kos["harga"])
        C.remove(x)
        print(
            f"Memeriksa kandidat: {x['nama']} (Harga: {x['harga']}, Jarak: {x['jarak']})"
        )

        if x["harga"] <= 500000 and x["jarak"] <= 450:
            print("  => Dipilih sebagai kos terbaik (greedy)")
            S = x
            break

    print("\n=== Hasil Akhir ===")
    if S:
        print(
            f"Kos yang dipilih: Nama={S['nama']}, Harga={S['harga']}, Jarak={S['jarak']}"
        )
    else:
        print("Tidak ada solusi")


file_path = r"C:\Users\hp\ASA\UTS2\data_kos.docx"
cari_kos_terbaik(file_path)
