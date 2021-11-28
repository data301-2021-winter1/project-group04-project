import pandas as pd
import numpy as np

def load_data(csv_file):
    mcu = pd.read_csv(csv_file)
    return mcu

def clean_data(mcu1):
    (mcu.copy().drop(columns=['full_name', 'occupation', 'type_race', 'has_jump', 'has_illusions', 'alter_egos', 'first_appearance', 'relatives', 'eye_color', 'hair_color', 'skin_color', 'img', 'has_electrokinesis', 'has_energy_constructs', 'has_matter_manipulation', 'has_telepathy_resistance', 'has_enhanced_hearing', 'has_dimensional_travel', 'has_element_control', 'has_size_changing', 'has_fire_resistance', 'has_fire_control', 'has_dexterity', 'has_reality_warping', 'has_energy_beams', 'has_shapeshifting', 'has_heat_resistance', 'has_heat_resistance', 'has_energy_absorption', 'has_cold_resistance', 'has_magic', 'has_toxin_and_disease_resistance', 'has_regeneration', 'has_immortality', 'has_teleportation', 'has_force_fields', 'has_energy_manipulation', 'has_longevity', 'has_weapon-based_powers', 'has_energy_blasts', 'has_enhanced_senses', 'has_invulnerability', 'has_stealth', 'has_marksmanship', 'has_flight', 'has_accelerated_healing', 'has_weapons_master', 'has_telepathy', 'has_telekinesis', 'has_self-sustenance'])) 
    mcu1 = mcu1[mcu1['intelligence_score'] > 0]
    mcu1 = mcu1[mcu1['strength_score'] > 0]
        )    
    return mcu1


def process_wrangle_data(dfp):
    sum_column = mcu1["intelligence_score"] + mcu1["strength_score"]
    mcu1["intelligence_strength_sum"] = sum_column 
    mcu1 = mcu1.sort_values("overall_score")
        .reset_index(drop=True)
        )    
    return mcu1