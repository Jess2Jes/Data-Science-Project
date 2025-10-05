def cari_task(tasks):
    keyword = input("\nMasukkan nama task yang ingin dicari: ").strip().lower()
    found = [t for t in tasks if keyword in t["name"].lower()]
    
    if not found:
        print(f"\n⚠ Task dengan nama => {keyword} tidak ditemukan.")
        return

    print(f"\nHasil pencarian untuk => {keyword} :\n")
    for idx, t in enumerate(found, start=1):
        pnjg_garis = f"{idx}. {t['name']}, {t['deadline']}, {t['priority']}, {t['status']}"
        garis = "─" * len(pnjg_garis)
        print("\n" + garis)
        print(pnjg_garis)
