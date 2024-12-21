import json

# Создаем словарь с данными
muscle_mapping = {
    'бицепс': ['L2__Arms_BicepSize'],
    'бицепс бедра': ['L2__Legs_QuadsSize'],
    'грудь': ['L2__Chest_Breast Size', 'L2__Torso_RibsWidth'],
    'икры': ['L2__Legs_CalvesSize'],
    'квадрицепсы': ['L2__Legs_QuadsSize'],
    'нижняя часть': ['L2__Waist_HipWidth'],
    'плечи': ['L2__Shoulders_ShoulderWidth'],
    'предплечья': ['L2__Arms_ForearmGirth'],
    'пресс': ['L2__Waist_HipWidth'],
    'приводящие мышцы': ['L2__Legs_QuadsSize'],
    'средняя часть': ['L2__Chest_Breast Size', 'L2__Torso_RibsWidth'],
    'трицепс': ['L2__Arms_TricepSize'],
    'четырехглавая мышца': ['L2__Legs_QuadsSize'],
    'широчайшие мышцы': ['L2__Shoulders_TrapeziusSize', 'L2__Shoulders_ShoulderWidth'],
    'ягодицы': ['L2__Waist_GluteSize']
}

# Сохраняем в JSON файл с отступами для читаемости
# и обеспечением корректной кодировки кириллицы
with open('muscle_alien_mapping.json', 'w', encoding='utf-8') as f:
    json.dump(muscle_mapping, f, ensure_ascii=False, indent=2)

# Пример чтения JSON файла
def read_muscle_mapping():
    with open('muscle_alien_mapping.json', 'r', encoding='utf-8') as f:
        return json.load(f)
