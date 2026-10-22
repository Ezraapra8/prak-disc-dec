from vector_clock import VectorClock

# Simulasi sistem dengan 3 proses
vc0 = VectorClock(num_processes=3, process_id=0)
vc1 = VectorClock(num_processes=3, process_id=1)
vc2 = VectorClock(num_processes=3, process_id=2)

print("=== Kondisi Vector Clock Awal ===")
print(vc0)
print(vc1)
print(vc2)

# P0 melakukan kejadian event lokal
vc0.increment()
print("\n=== Setelah Proses 0 kejadian lokal ===")
print(vc0)

# P0 mengirim pesan ke P1
pesan_dari_p0 = vc0.send_message()
vc1.receive_message(pesan_dari_p0)
print("\n=== Setelah Proses 0 kirim ke Proses 1 ===")
print(vc0)
print(vc1)

# P2 melakukan kejadian event lokal
vc2.increment()
print("\n=== Setelah Proses 2 kejadian lokal ===")
print(vc2)

# P1 mengirim pesan ke P2
pesan_dari_p1 = vc1.send_message()
vc2.receive_message(pesan_dari_p1)
print("\n=== Setelah Proses 1 kirim ke Proses 2 ===")
print(vc1)
print(vc2)

# Pengujian hubungan kausal
print("\n=== Pengujian hubungan kausal ===")
print("VC0 happens before VC1:", vc0.happens_before(vc1))
print("VC1 happens before VC0:", vc1.happens_before(vc0))
print("VC0 is concurrent with VC2:", vc0.is_concurrent(vc2))