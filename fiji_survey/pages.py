from ._builtin import Page
from .models import Player


class LanguageSelect(Page):
    form_model = Player
    form_fields = ['language']


class Screening(Page):
    form_model = Player
    form_fields = ['Q1', 'Q2', 'Q3', 'Q4']

    def before_next_page(self):
        # Screen out non-residents (Q1=3) and under 18 (Q2=1)
        if self.player.Q1 == 3 or self.player.Q2 == 1:
            self.player.screened_out = True

    def vars_for_template(self):
        return dict(lang=self.player.language)


class ScreenedOut(Page):
    def is_displayed(self):
        return self.player.screened_out

    def vars_for_template(self):
        return dict(lang=self.player.language)


class TourismImpact(Page):
    form_model = Player
    form_fields = [
        'Q5a_importance', 'Q5a_satisfaction',
        'Q5b_importance', 'Q5b_satisfaction',
        'Q5c_importance', 'Q5c_satisfaction',
        'Q5d_importance', 'Q5d_satisfaction',
        'Q5e_importance', 'Q5e_satisfaction',
        'Q5f_importance', 'Q5f_satisfaction',
        'Q5g_importance', 'Q5g_satisfaction',
        'Q5h_importance', 'Q5h_satisfaction',
        'Q5i_importance', 'Q5i_satisfaction',
        'Q5j_importance', 'Q5j_satisfaction',
        'Q5k_importance', 'Q5k_satisfaction',
        'Q5l_importance', 'Q5l_satisfaction',
        'Q5m_importance', 'Q5m_satisfaction',
    ]

    def is_displayed(self):
        return not self.player.screened_out

    def vars_for_template(self):
        return dict(lang=self.player.language)


class OverallTourism(Page):
    form_model = Player
    form_fields = ['Q6', 'Q7', 'Q8']

    def is_displayed(self):
        return not self.player.screened_out

    def vars_for_template(self):
        return dict(lang=self.player.language)


class QualityOfLife(Page):
    form_model = Player
    form_fields = ['Q10a', 'Q10b', 'Q10c', 'Q10d', 'Q10e', 'Q10f', 'Q10g', 'Q10h', 'Q10i']

    def is_displayed(self):
        return not self.player.screened_out

    def vars_for_template(self):
        return dict(lang=self.player.language)


class ServiceSatisfaction(Page):
    form_model = Player
    form_fields = [
        'Q11_education', 'Q11_health', 'Q11_water', 'Q11_electricity',
        'Q11_transport', 'Q11_other', 'Q11_other_specify',
        'Q12', 'Q13', 'Q14', 'Q15', 'Q16',
    ]

    def is_displayed(self):
        return not self.player.screened_out

    def vars_for_template(self):
        return dict(lang=self.player.language)


class LifeSatisfaction(Page):
    form_model = Player
    form_fields = ['Q17a', 'Q17b', 'Q17c', 'Q17d', 'Q17e']

    def is_displayed(self):
        return not self.player.screened_out

    def vars_for_template(self):
        return dict(lang=self.player.language)


class Empowerment(Page):
    form_model = Player
    form_fields = [
        'Q18a', 'Q18b', 'Q18c', 'Q18d', 'Q18e',
        'Q18f', 'Q18g', 'Q18h',
        'Q18i', 'Q18j', 'Q18k', 'Q18l',
    ]

    def is_displayed(self):
        return not self.player.screened_out

    def vars_for_template(self):
        return dict(lang=self.player.language)


class PlaceAttachment(Page):
    form_model = Player
    form_fields = ['Q19a', 'Q19b', 'Q19c', 'Q19d', 'Q19e', 'Q19f', 'Q20']

    def is_displayed(self):
        return not self.player.screened_out

    def vars_for_template(self):
        return dict(lang=self.player.language)


class FutureTourism(Page):
    form_model = Player
    form_fields = [
        'Q21',
        'Q22_local_polynesia', 'Q22_france', 'Q22_usa', 'Q22_au_nz',
        'Q22_asia', 'Q22_other_countries', 'Q22_business', 'Q22_event',
        'Q23_luxury_hotel', 'Q23_midrange_hotel', 'Q23_guesthouse',
        'Q23_homestay', 'Q23_airbnb', 'Q23_floating',
        'Q23_cultural', 'Q23_nature', 'Q23_sports',
    ]

    def is_displayed(self):
        return not self.player.screened_out

    def vars_for_template(self):
        return dict(lang=self.player.language)


class Demographics(Page):
    form_model = Player
    form_fields = ['Q24', 'Q25', 'Q26', 'Q27', 'Q28', 'Q29', 'Q30', 'Q31', 'Q32']

    def is_displayed(self):
        return not self.player.screened_out

    def vars_for_template(self):
        return dict(lang=self.player.language)


class ThankYou(Page):
    def vars_for_template(self):
        return dict(lang=self.player.language)


page_sequence = [
    LanguageSelect,
    Screening,
    ScreenedOut,
    TourismImpact,
    OverallTourism,
    QualityOfLife,
    ServiceSatisfaction,
    LifeSatisfaction,
    Empowerment,
    PlaceAttachment,
    FutureTourism,
    Demographics,
    ThankYou,
]
