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


def is_valid(kos, max_harga=500000, max_jarak=450):
    return kos["harga"] <= max_harga and kos["jarak"] <= max_jarak


def backtrack(kos_list, index=0, best=None):
    if index == len(kos_list):
        return best

    kos = kos_list[index]
    print(f"Memeriksa: {kos['nama']} (Harga: {kos['harga']}, Jarak: {kos['jarak']})")

    if is_valid(kos):
        print("  => Valid")
        if (
            (best is None)
            or (kos["harga"] < best["harga"])
            or (kos["harga"] == best["harga"] and kos["jarak"] < best["jarak"])
        ):
            print(f"  => Menjadi kandidat terbaik sementara")
            best = kos
    else:
        print("  => Tidak valid")

    return backtrack(kos_list, index + 1, best)


def cari_kos_terbaik(file_path):
    kos_list = baca_kos_dari_word(file_path)
    print("=== Mulai Pencarian Kos Terbaik ===")
    hasil = backtrack(kos_list)
    print("=== Selesai ===\n")

    if hasil:
        print(
            f"Kos yang dipilih: Nama={hasil['nama']}, Harga={hasil['harga']}, Jarak={hasil['jarak']}"
        )
    else:
        print("Tidak ada solusi")


file_path = r"C:\Users\hp\ASA\UTS2\data_kos.docx"
cari_kos_terbaik(file_path)
