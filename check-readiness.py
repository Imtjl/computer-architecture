import re

total = 218
path = "exam-notes-short.md"

with open(path, "r", encoding="utf-8") as f:
    c = f.read()

q = re.findall(r"#### (\d+)\.", c)
q = set(int(q_) for q_ in q)

missing = [i for i in range(1, total + 1) if i not in q]

print(f"Готово: {len(q)} из {total}")
print(f"Осталось: {len(missing)}")
if missing:
    print(f"Пропущенные номера: {missing}")
