import random


def handle_response(message) -> str:
    p_message = message

    if p_message == "abgeneral":
        number_rolled = random.randint(1, 100)
        if 1 <= number_rolled <= 30:
            return f"**{number_rolled}D**, You got a -1 general!"
        elif 31 <= number_rolled <= 71:
            return f"**{number_rolled}D**, You got a +0 general!"
        elif 72 <= number_rolled <= 90:
            return f"**{number_rolled}D**, You got a +1 general!"
        elif 91 <= number_rolled <= 99:
            return f"**{number_rolled}D**, You got a +2 general!"
        elif number_rolled == 100:
            return f"**{number_rolled}D**, You got a +3 general!"
    if p_message == "abhelp":
        return (f"Hello! You can use the following commands:" + " \n" + "**abgeneral**(to roll for a general)" +" \n" + "**abfertility**(to roll for character fertility)" + "\n" "**abcharacter**(to roll for a character)")
    if p_message == "abfertility":
        fert_number_rolled = random.randint(1, 100)
        if 1 <= fert_number_rolled <= 25:
            return f"**{fert_number_rolled}D**, You are infertile."
        elif 26 <= fert_number_rolled <= 55:
            return f"**{fert_number_rolled}D**, Medium Fertility - Max of 4 rolls"
        elif 56 <= fert_number_rolled <= 80:
            return f"**{fert_number_rolled}D**, Medium-High Fertility - Max of 6 rolls"
        elif 81 <= fert_number_rolled <= 95:
            return f"**{fert_number_rolled}D**, High Fertility - Max of 10 rolls"
        elif 96 <= fert_number_rolled <= 100:
            return f"**{fert_number_rolled}D**, Prolific - Max of 20 rolls."

    if p_message == "abcharacter":
        preg_number_rolled_var = ""
        maternal_death_numroll_var = ""
        preg_number_rolled = random.randint(1, 100)
        if 1 <= preg_number_rolled <= 79:
            preg_number_rolled_var = f"**Pregnancy: {preg_number_rolled}D**, Successful pregnancy!"
        elif 79 < preg_number_rolled > 81:
            preg_number_rolled_var = f"**Pregnancy: {preg_number_rolled}D**, Successful pregnancy, and, surprise, twins!"
        elif 81 <= preg_number_rolled <= 100:
            preg_number_rolled_var = f"**Pregnancy: {preg_number_rolled}D**, Miscarriage! :sob:"
            return "Miscarriage! :sob:"

        maternal_death_numroll = random.randint(1, 100)
        if 1 <= maternal_death_numroll <= 95:
            maternal_death_numroll_var = f"**Maternal Death: {maternal_death_numroll}D**, Mother Survives!"
        elif 96 <= maternal_death_numroll <= 100:
            maternal_death_numroll_var = f"**Maternal Death: {maternal_death_numroll}D**, Mother Dies. :cry:"

        health_roll = random.randint(1, 100)
        if 1 <= health_roll <= 5:
            health_roll_var = f"**Health: {health_roll}D**, Prosperous health! +5 lifetime -15 ailments"
        elif 6 <= health_roll <= 70:
            health_roll_var = f"**Health: {health_roll}D**, Healthy! -5 Ailments"
        elif 71 <= health_roll <= 90:
            health_roll_var = f"**Health: {health_roll}D**, Unhealthy! +15 Ailments, -15 Lifetime"
        elif 91 <= health_roll <= 100:
            health_roll_var = f"**Health: {health_roll}D**, Stillborn 💀"
            return "Stillborn 💀"

        gender_roll = random.randint(1, 100)
        if 1 <= gender_roll <= 50:
            gender_roll_var = f"**Gender: {gender_roll}D**, Male! Nice!"
        elif 51 <= gender_roll <= 100:
            gender_roll_var = f"**Gender: {gender_roll}D**, Female."

        sexuality_roll = random.randint(1, 100)
        if 1 <= sexuality_roll <= 70:
            sexuality_roll_var = f"**Sexuality: {sexuality_roll}D**, Normal"
        elif 71 <= sexuality_roll <= 100:
            sexuality_roll_var = f"**Sexuality: {sexuality_roll}D**, Non-Straight -15 Fertility"

        lifetime_roll = random.randint(1, 100)
        if lifetime_roll <= 101:
            lifetime_roll_var = f"**Lifetime: {lifetime_roll}D**, hopefully you rolled high!"
        appearance_roll = random.randint(1, 100)

        if 1 <= appearance_roll <= 5:
            appearance_roll_var = f"**Appearance: {appearance_roll}D**, Unsightly, -15 Diplomacy"
        elif 6 <= appearance_roll <= 30:
            appearance_roll_var = f"**Appearance: {appearance_roll}D**, Ugly, -5 Diplomacy"
        elif 31 <= appearance_roll <= 70:
            appearance_roll_var = f"**Appearance: {appearance_roll}D**, Average"
        elif 71 <= appearance_roll <= 95:
            appearance_roll_var = f"**Appearance: {appearance_roll}D**, Attractive, +5 Diplomacy"
        elif 96 <= appearance_roll <= 100:
            appearance_roll_var = f"**Appearance: {appearance_roll}D**, Beautiful, +15 Diplomacy"

        strength_roll = random.randint(1, 100)
        if 1 <= strength_roll <= 10:
            strength_roll_var = f"**Strength: {strength_roll}D**, Fragile, -10 Martial"
        elif 11 <= strength_roll <= 30:
            strength_roll_var = f"**Strength: {strength_roll}D**, Scrawny, -1 Duels"
        elif 31 <= strength_roll <= 80:
            strength_roll_var = f"**Strength: {strength_roll}D**, Average"
        elif 81 <= strength_roll <= 95:
            strength_roll_var = f"**Strength: {strength_roll}D**, Brawny, +1 Duels"
        elif 96 <= strength_roll <= 100:
            strength_roll_var = f"**Strength: {strength_roll}D**, +2 Duels, +5 Martial"

        ailments_roll = random.randint(1, 100)
        if 1 <= ailments_roll <= 75:
            ailments_roll_var = f"**Ailments: {ailments_roll}D**, No Ailments!"
        elif 76 <= ailments_roll <= 85:
            ailments_roll_var = f"**Ailments: {ailments_roll}D**, Imbecile! -50 All Traits, smooth brained :smile:"
        elif 85 < ailments_roll < 87:
            ailments_roll_var = f"**Ailments: {ailments_roll}D**, Blind! -100 Martial, +25 Wisdom, -50 Ambition. :man_with_probing_cane:"
        elif 87 <= ailments_roll <= 93:
            ailments_roll_var = f"**Ailments: {ailments_roll}D**, Hemophiliac! Roll for survival every 10 years."
        elif 93 < ailments_roll < 95:
            ailments_roll_var = f"**Ailments: {ailments_roll}D**, Mute! -50 Diplomacy, +15 Wisdom."
        elif 95 <= ailments_roll <= 100:
            ailments_roll_var = f"**Ailments: {ailments_roll}D**, Insane! -50 Diplomacy, +15 Martial. :fearful:"

        diplomacy_roll = random.randint(1, 100)
        if diplomacy_roll <= 100:
            diplomacy_roll_var = f"**Diplomacy: {diplomacy_roll}D**, See more at: https://discord.com/channels/1102113406091276319/1102525704362545254/1104234054200598539"

        martial_roll = random.randint(1, 100)
        if martial_roll <= 30:
            martial_roll_var = f"**Martial: {martial_roll}D**, -1"
        elif 31 <= martial_roll <= 70:
            martial_roll_var = f"**Martial: {martial_roll}D**, +0"
        elif 71 <= martial_roll <= 90:
            martial_roll_var = f"**Martial: {martial_roll}D**, +1"
        elif 91 <= martial_roll <= 99:
            martial_roll_var = f"**Martial: {martial_roll}D**, +2"
        elif martial_roll >= 100:
            martial_roll_var = f"**Martial: {martial_roll}D**, +3"

        admin_roll = random.randint(1, 100)
        if admin_roll <= 100:
            admin_roll_var = f"**Administration: {admin_roll}D**, See more at: https://discord.com/channels/1102113406091276319/1102525704362545254/1104234054200598539"

        wisdom_roll = random.randint(1, 100)
        if wisdom_roll <= 20:
            wisdom_roll_var = f"**Wisdom: {wisdom_roll}D**, Ignorant. -10 All Traits"
        elif 21 <= wisdom_roll <= 77:
            wisdom_roll_var = f"**Wisdom: {wisdom_roll}D**, Average."
        elif 78 <= wisdom_roll <= 92:
            wisdom_roll_var = f"**Wisdom: {wisdom_roll}D**, Clever. +5 All Traits"
        elif 93 <= wisdom_roll <= 100:
            wisdom_roll_var = f"**Wisdom: {wisdom_roll}D**, Wise. +10 All Traits"

        ambition_roll = random.randint(1, 100)
        if ambition_roll <= 100:
            ambition_roll_var = f"**Ambition: {ambition_roll}D**, See more at: https://discord.com/channels/1102113406091276319/1102525704362545254/1104234054200598539"

        personality_roll = random.randint(1, 100)
        if personality_roll <= 12:
            personality_roll_var = f"**Personality: {personality_roll}D**, Humble +10 Diplo -5 Ambition "
        elif 13 <= personality_roll <= 24:
            personality_roll_var = f"**Personality: {personality_roll}D**, Brave +10 Martial -10 Wisdom"
        elif 25 <= personality_roll <= 36:
            personality_roll_var = f"**Personality: {personality_roll}D**, Just +5 Admin"
        elif 37 <= personality_roll <= 48:
            personality_roll_var = f"**Personality: {personality_roll}D**, Kind +5 +10 Diplo -5 Martial"
        elif 49 <= personality_roll <= 52:
            personality_roll_var = f"**Personality: {personality_roll}D**, illustrious +5 all"
        elif 53 <= personality_roll <= 64:
            personality_roll_var = f"**Personality: {personality_roll}D**, Cruel +10 Martial, -10 Diplo, -5 Wisdom"
        elif 65 <= personality_roll <= 76:
            personality_roll_var = f"**Personality: {personality_roll}D**, Arbitrary +5 Ambition, -5 Admin"
        elif 77 <= personality_roll <= 88:
            personality_roll_var = f"**Personality: {personality_roll}D**, Coward +15 Wisdom, -10 Martial"
        elif 89 <= personality_roll <= 100:
            personality_roll_var = f"**Personality: {personality_roll}D**, Flamboyant +10 Ambition, -5 Admin"

        return (
                    "## Health Related\n" + preg_number_rolled_var + " \n" + maternal_death_numroll_var + " \n" + health_roll_var
                    + " \n" + gender_roll_var + " \n" + sexuality_roll_var + " \n" + lifetime_roll_var + " \n" + " \n" + "## Genetics" + " \n" + appearance_roll_var +
                    " \n" + strength_roll_var + " \n" + ailments_roll_var + " \n" + " \n" + "## Skill Set"+ " \n" + diplomacy_roll_var + " \n" + martial_roll_var + " \n" + admin_roll_var +
                    " \n") + wisdom_roll_var + " \n" + ambition_roll_var + " \n" + " \n" + "## Personality" + " \n" + personality_roll_var + " \n" + "Remember: Bonuses are not added by the bot, you have to add them yourself! (i.e if you have a +15 martial bonus, you need to add that to the amount provided by the bot.)"
