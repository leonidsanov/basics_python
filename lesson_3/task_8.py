"""
Три друга взяли вещи в поход.
Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
Какие вещи взяли все три друга?
Какие вещи уникальны, есть только у одного друга?
Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует?
Для решения используйте операции с множествами.
Код должен расширяться на любое большее количество друзей.
"""

hike = {
    "Aaz": ("спички", "спальник", "дрова", "топор"),
    "Skeeve": ("спальник", "спички", "вода", "еда"),
    "Tananda": ("вода", "спички", "косметичка"),
}

at_all = set()
for values in hike.values():
    for value in values:
        at_all.add(value)
print(f"Полный список вещей: {at_all = }")

unique = {}
for master_key, master_values in hike.items():
    for slave_key, slave_values in hike.items():
        if master_key != slave_key:
            if unique.get(master_key):
                unique[master_key] -= set(slave_values)
            else:
                unique[master_key] = set(master_values) - set(slave_values)
print(f"Уникальные вещи: {unique = }")

duplicates = set(at_all)
for value in unique.values():
    duplicates -= value
print(f"Дублирующие вещи: {duplicates = }")
for key, value in hike.items():
    print(
        f"У {key} отсутствует {(set(value) ^ duplicates) - set(unique[key])}, но есть у остальных"
    )
