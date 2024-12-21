import json

# Создаем словарь с данными
muscle_mapping = {
    'бицепс': ['L2__Arms_UpperarmMass-UpperarmTone_max-max'],
    'бицепс бедра': ['L2__Legs_UpperlegsMass-UpperlegsTone_max-max'],
    'грудь': ['L2__Torso_Mass-Tone_max-max'],
    'икры': ['L2__Legs_LowerlegsMass-LowerlegsTone_max-max'],
    'квадрицепсы': ['L2__Legs_UpperlegsMass-UpperlegsTone_max-max'],
    'нижняя часть': ['L2__Waist_Size_max'],
    'плечи': ['L2__Shoulders_Mass-Tone_max-max'],
    'предплечья': ['L2__Arms_ForearmMass-ForearmTone_max-max', 'L2__Wrists_Size_max'],
    'пресс': ['L2__Abdomen_Mass-Tone_max-max'],
    'приводящие мышцы': ['L2__Legs_UpperlegsMass-UpperlegsTone_max-max'],
    'средняя часть': ['L2__Torso_Mass-Tone_max-max'],
    'трицепс': ['L2__Arms_UpperarmMass-UpperarmTone_max-max'],
    'четырехглавая мышца': ['L2__Legs_UpperlegsMass-UpperlegsTone_max-max'],
    'широчайшие мышцы': ['L2__Shoulders_Mass-Tone_max-max', 'L2__Neck_Mass-Tone_max-max'],
    'ягодицы': ['L2__Pelvis_GluteusMass-GluteusTone_max-max']
}

# Сохраняем в JSON файл с отступами для читаемости
# и обеспечением корректной кодировки кириллицы
with open('muscle_mapping.json', 'w', encoding='utf-8') as f:
    json.dump(muscle_mapping, f, ensure_ascii=False, indent=2)

# Пример чтения JSON файла
def read_muscle_mapping():
    with open('muscle_mapping.json', 'r', encoding='utf-8') as f:
        return json.load(f)
