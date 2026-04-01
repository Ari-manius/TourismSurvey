from ._builtin import Page
from .models import Player


class BasePage(Page):
    def vars_for_template(self):
        total = self.participant._max_page_index
        current = self.participant._index_in_pages
        progress = int(100 * current / total) if total else 0
        return dict(
            lang=self.player.field_maybe_none('language'),
            progress=progress,
        )


class LanguageSelect(BasePage):
    form_model = Player
    form_fields = ['language']


class Screening(BasePage):
    form_model = Player
    form_fields = ['Q1', 'Q2', 'Q3_province', 'Q3_municipality', 'Q4']

    def before_next_page(self):
        if self.player.Q1 == 3 or self.player.Q2 == 1:
            self.player.screened_out = True


class ScreenedOut(BasePage):
    def is_displayed(self):
        return self.player.screened_out


class TourismImpact(BasePage):
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


class OverallTourism(BasePage):
    form_model = Player
    form_fields = ['Q6', 'Q7', 'Q8']

    def is_displayed(self):
        return not self.player.screened_out


class QualityOfLife(BasePage):
    form_model = Player
    form_fields = ['Q9a', 'Q9b', 'Q9c', 'Q9d', 'Q9e', 'Q9f', 'Q9g', 'Q9h', 'Q9i']

    def is_displayed(self):
        return not self.player.screened_out


class ServiceSatisfaction(BasePage):
    form_model = Player
    form_fields = [
        'Q10_education', 'Q10_health', 'Q10_water', 'Q10_electricity',
        'Q10_transport', 'Q10_other', 'Q10_other_specify',
        'Q11', 'Q12', 'Q13', 'Q14', 'Q15',
    ]

    def is_displayed(self):
        return not self.player.screened_out


class LifeSatisfaction(BasePage):
    form_model = Player
    form_fields = ['Q16a', 'Q16b', 'Q16c', 'Q16d', 'Q16e']

    def is_displayed(self):
        return not self.player.screened_out


class Empowerment(BasePage):
    form_model = Player
    form_fields = [
        'Q17a', 'Q17b', 'Q17c', 'Q17d', 'Q17e',
        'Q17f', 'Q17g', 'Q17h',
        'Q17i', 'Q17j', 'Q17k', 'Q17l', 'Q17m',
    ]

    def is_displayed(self):
        return not self.player.screened_out


class PlaceAttachment(BasePage):
    form_model = Player
    form_fields = ['Q18a', 'Q18b', 'Q18c', 'Q18d', 'Q18e', 'Q18f', 'Q19']

    def is_displayed(self):
        return not self.player.screened_out


class FutureTourism(BasePage):
    form_model = Player
    form_fields = [
        'Q20',
        'Q21_local_here','Q21_local_wallisfutuna', 'Q21_local_vanuatu' ,'Q21_local_fiji', 'Q21_local_tahiti', 'Q21_local_pacific', 'Q21_france', 'Q21_eu', 'Q21_usa', 'Q21_au_nz',
        'Q21_asia', 'Q21_other_countries', 'Q21_business', 'Q21_event',
        'Q22_luxury_hotel', 'Q22_midrange_hotel', 'Q22_guesthouse',
        'Q22_homestay', 'Q22_airbnb', 'Q22_floating',
        'Q22_cultural', 'Q22_nature', 'Q22_sports',
    ]

    def is_displayed(self):
        return not self.player.screened_out


class Demographics(BasePage):
    form_model = Player
    form_fields = ['Q23', 'Q24', 'Q25', 'Q26', 'Q27', 'Q28', 'Q29', 'Q30', 'Q31']

    def is_displayed(self):
        return not self.player.screened_out


class ThankYou(BasePage):
    pass


page_sequence = [
    LanguageSelect,
    Screening,
    ScreenedOut,
    OverallTourism,
    TourismImpact,
    QualityOfLife,
    ServiceSatisfaction,
    LifeSatisfaction,
    Empowerment,
    PlaceAttachment,
    FutureTourism,
    Demographics,
    ThankYou,
]
