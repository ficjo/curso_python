from pathlib import Path

p = Path("log.txt")

print()

print(p.exists())
print(p.read_text())

p.write_text("Arquivo recriado.\n")

print(p.read_text())

print()