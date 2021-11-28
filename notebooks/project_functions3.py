import pandas as pd
import numpy as np

def load_data(csv_file):
    superheroes = pd.read_csv(csv_file)
    return superheroes



superheroes.copy().drop(["has_flight","has_intelligence", "has_marksmanship", "has_invulnerability", "has_stealth", "has_accelerated_healing", "has_weapons_master", "has_reflexes", "has_super_speed", "has_durability", "has_stamina", "has_agility", "has_super_strength", "has_regeneration","has_immortality","has_teleportation","has_force_fields","has_energy_manipulation","has_endurance", "has_longevity","has_weapon-based_powers","has_energy_blasts","has_enhanced_senses","has_shapeshifting","has_heat_resistance","has_jump","has_self-sustenance","has_energy_absorption","has_cold_resistance","has_magic","has_telekinesis","has_toxin_and_disease_resistance","has_telepathy","has_dimensional_travel","has_element_control","has_size_changing","has_fire_resistance","has_fire_control","has_dexterity","has_reality_warping","has_illusions","has_energy_beams","has_peak_human_condition","hair_color","skin_color","img","has_electrokinesis","has_energy_constructs","has_mind_control_resistance","has_matter_manipulation","has_telepathy_resistance","has_mind_control","has_enhanced_hearing"],axis=1)

NA_val = superheroes_cleaned.isna().sum() 
def na_filter(na, threshold = .4):
    col_pass = []
    for i in na.keys():
        if na[i]/superheroes_cleaned.shape[0]<threshold:
            col_pass.append(i)
        return col_passsuperheroes_cleaned == superheroes_cleaned[na_filter(NA_val)]
    superheroes_cleaned.columns
    
    superheroes_cleaned.sort_values("strength_score")
    
