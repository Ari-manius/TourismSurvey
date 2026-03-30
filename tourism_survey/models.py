from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)

doc = """
Tourism Perceptions and Quality of Life Survey for Polynesian Islands.
Bilingual survey (French/English) with language selection.
"""


class Constants(BaseConstants):
    name_in_url = 'fiji_survey'
    players_per_group = None
    num_rounds = 1

    # Likert 5 agreement scale + nonresponse
    LIKERT5_AGREE_CHOICES = [1, 2, 3, 4, 5, 99]

    # Likert 5 scale without nonresponse (for Tourism Impact)
    LIKERT5_CHOICES = [1, 2, 3, 4, 5]

    # Scale 0 to 10 + nonresponse
    SCALE_0_10_CHOICES = list(range(0, 11)) + [99]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # === Language Selection ===
    language = models.StringField(
        choices=[['fr', 'Français'], ['en', 'English']],
        widget=widgets.RadioSelect,
        blank=False,
    )

    # === Page 1: Screening & Residence ===
    Q1 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q2 = models.IntegerField(
        choices=[[1, ''], [0, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q3_province = models.StringField(blank=True)
    Q3_municipality = models.StringField(blank=True)
    Q4 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    # Track if screened out
    screened_out = models.BooleanField(initial=False)

    # === Page 2: Tourism Impact Perception (Q5a-Q5m paired likert) ===
    Q5a_importance = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5a_satisfaction = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5b_importance = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5b_satisfaction = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5c_importance = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5c_satisfaction = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5d_importance = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5d_satisfaction = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5e_importance = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5e_satisfaction = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5f_importance = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5f_satisfaction = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5g_importance = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5g_satisfaction = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5h_importance = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5h_satisfaction = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5i_importance = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5i_satisfaction = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5j_importance = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5j_satisfaction = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5k_importance = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5k_satisfaction = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5l_importance = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5l_satisfaction = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5m_importance = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5m_satisfaction = models.IntegerField(choices=Constants.LIKERT5_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)

    # === Page 3: Overall Tourism Assessment ===
    Q6 = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q7 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q8 = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)

    # === Page 4: Quality of Life (Q10a-Q10i) ===
    Q10a = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q10b = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q10c = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q10d = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q10e = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q10f = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q10g = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q10h = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q10i = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)

    # === Page 5: Service Satisfaction ===
    Q11_education = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q11_health = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q11_water = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q11_electricity = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q11_transport = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q11_other = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q11_other_specify = models.StringField(blank=True)
    Q12 = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q13 = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q14 = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q15 = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q16 = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)

    # === Page 6: General Life Satisfaction (Q17a-Q17e) ===
    Q17a = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17b = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17c = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17d = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17e = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)

    # === Page 7: Empowerment (Q18a-Q18l) ===
    Q18a = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18b = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18c = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18d = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18e = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18f = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18g = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18h = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18i = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18j = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18k = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18l = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)

    # === Page 8: Place Attachment (Q19a-Q19f, Q20) ===
    Q19a = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q19b = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q19c = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q19d = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q19e = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q19f = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q20 = models.LongStringField(blank=True)

    # === Page 9: Future Tourism Directions ===
    Q21 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [0, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    # Q22: visitor types matrix (8 items, scale 1-4)
    Q22_local_here = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_local_pacific = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_france = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_usa = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_au_nz = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_asia = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_other_countries = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_business = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_event = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    # Q23: tourism types matrix (9 items, scale 1-5)
    Q23_luxury_hotel = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q23_midrange_hotel = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q23_guesthouse = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q23_homestay = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q23_airbnb = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q23_floating = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q23_cultural = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q23_nature = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q23_sports = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)

    # === Page 10: Sociodemographic Information ===
    Q24 = models.StringField(
        choices=[['M', ''], ['F', ''], ['O', '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q25 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q26 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q27 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q28 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q29 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q30 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, ''], [8, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q31 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q32 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
