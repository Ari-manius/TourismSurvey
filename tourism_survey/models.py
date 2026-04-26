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
    name_in_url = 'tourism_survey'
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
    # === Metadata (auto-collected via JS on Screening page) ===
    # Collected on Screening page
    meta_timestamp = models.StringField(blank=True)
    meta_device_type = models.StringField(blank=True)   # desktop / tablet / mobile
    meta_os = models.StringField(blank=True)
    meta_browser = models.StringField(blank=True)
    meta_screen_width = models.IntegerField(blank=True)
    meta_screen_height = models.IntegerField(blank=True)
    meta_viewport_width = models.IntegerField(blank=True)
    meta_viewport_height = models.IntegerField(blank=True)
    meta_timezone = models.StringField(blank=True)
    meta_language = models.StringField(blank=True)      # browser language
    meta_user_agent = models.StringField(blank=True)
    meta_connection_type = models.StringField(blank=True)  # wifi / 4g / 3g / 2g / unknown
    meta_touch_support = models.StringField(blank=True)    # yes / no
    meta_referrer = models.StringField(blank=True)
    # Collected on ThankYou page
    meta_end_timestamp = models.StringField(blank=True)
    meta_duration_seconds = models.IntegerField(blank=True)

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
    Q5a_importance = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5a_satisfaction = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5b_importance = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5b_satisfaction = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5c_importance = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5c_satisfaction = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5d_importance = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5d_satisfaction = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5e_importance = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5e_satisfaction = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5f_importance = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5f_satisfaction = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5g_importance = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5g_satisfaction = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5h_importance = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5h_satisfaction = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5i_importance = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5i_satisfaction = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5j_importance = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5j_satisfaction = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5k_importance = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5k_satisfaction = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5l_importance = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5l_satisfaction = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5m_importance = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q5m_satisfaction = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)

    # === Page 3: Overall Tourism Assessment ===
    Q6 = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q7 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q8 = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)

    # === Page 4: Quality of Life (Q9a-Q9i) ===
    Q9a = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q9b = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q9c = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q9d = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q9e = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q9f = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q9g = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q9h = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q9i = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)

    # === Page 5: Service Satisfaction ===
    Q10_education = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q10_health = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q10_water = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q10_electricity = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q10_public_transport = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q10_private_transport = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q10_admin_services = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q10_other = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q10_other_specify = models.StringField(blank=True)
    Q11 = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q12 = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q13 = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q14 = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)
    Q15 = models.IntegerField(choices=Constants.SCALE_0_10_CHOICES, blank=True)

    # === Page 6: General Life Satisfaction (Q16a-Q16e) ===
    Q16a = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q16b = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q16c = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q16d = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q16e = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)

    # === Page 7: Empowerment (Q17a-Q17l) ===
    Q17a = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17b = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17c = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17d = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17e = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17f = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17g = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17h = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17i = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17j = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17k = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17l = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q17m = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)

    # === Page 8: Place Attachment (Q18a-Q18f, Q19) ===
    Q18a = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18b = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18c = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18d = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18e = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q18f = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q19 = models.LongStringField(blank=True)

    # === Page 9: Future Tourism Directions ===
    Q20 = models.IntegerField(blank=True)
    # Q21: visitor types matrix (8 items, scale 1-4)
    Q21_local_here = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q21_local_wallisfutuna = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q21_local_vanuatu = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q21_local_fiji = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q21_local_tahiti = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q21_local_pacific = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)    
    Q21_france = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q21_eu = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q21_usa = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q21_au_nz = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q21_asia = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q21_other_countries = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q21_business = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)
    Q21_event = models.IntegerField(choices=[[1, ''], [2, ''], [3, ''], [4, '']], widget=widgets.RadioSelectHorizontal, blank=True)

    # Q22: tourism types matrix (9 items, scale 1-5)
    Q22_luxury_hotel = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_midrange_hotel = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_guesthouse = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_homestay = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_airbnb = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_floating = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_cultural = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_nature = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)
    Q22_sports = models.IntegerField(choices=Constants.LIKERT5_AGREE_CHOICES, widget=widgets.RadioSelectHorizontal, blank=True)

    # === Page 10: Sociodemographic Information ===
    Q23 = models.StringField(
        choices=[['M', ''], ['F', ''], ['O', ''], ['NA', '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q24 = models.IntegerField(min=1920, max=2008, blank=True)
    Q25 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q26 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q27 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q28 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q29 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, ''], [8, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q30 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
    Q31 = models.IntegerField(
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, ''], [99, '']],
        widget=widgets.RadioSelect,
        blank=True,
    )
