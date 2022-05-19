from django.test import SimpleTestCase
from BVATApp.forms import InstellingenForm, CustomForm

class TestForms(SimpleTestCase):

    def test_expense_form_valid_data(self):
        form = InstellingenForm(data={
            'naam': 'Anna',
            'spelmodus': 'tijd',
            'tijd': '60',
            'woorden': '50',
            'taal': 'nederlands',
            'moeilijkheid': 'makkelijk'
        })
        self.assertTrue(form.is_valid())

    def test_expense_form_no_data(self):
        form = InstellingenForm(data={
            'naam': 'jsijxojidiwijdijowjidjiwojo',
            'spelmodus': '-',
            'tijd': '-',
            'woorden': '-',
            'taal': '-',
            'moeilijkheid': '-'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    def test_expense_form_name_valse_one(self):
        form = InstellingenForm(data={
            'naam': 'Annananananananana',
            'spelmodus': 'tijd',
            'tijd': '60',
            'woorden': '50',
            'taal': 'nederlands',
            'moeilijkheid': 'makkelijk'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_expense_form_time_valse_(self):
        form = InstellingenForm(data={
            'naam': 'An23467',
            'spelmodus': 'tijd',
            'tijd': '70',
            'woorden': '50',
            'taal': 'nederlands',
            'moeilijkheid': 'makkelijk'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_expense_form_game_valse(self):
        form = InstellingenForm(data={
            'naam': 'Anna',
            'spelmodus': 'custom',
            'tijd': '60',
            'woorden': '50',
            'taal': 'nederlands',
            'moeilijkheid': 'makkelijk'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_expense_form_time_valse(self):
        form = InstellingenForm(data={
            'naam': 'Anna',
            'spelmodus': 'tijd',
            'tijd': 'duizend',
            'woorden': '50',
            'taal': 'nederlands',
            'moeilijkheid': 'makkelijk'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_expense_form_words_valse(self):
        form = InstellingenForm(data={
            'naam': 'Anna',
            'spelmodus': 'tijd',
            'tijd': '60',
            'woorden': 'duizend',
            'taal': 'nederlands',
            'moeilijkheid': 'makkelijk'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_expense_form_taal_valse(self):
        form = InstellingenForm(data={
            'naam': 'Anna',
            'spelmodus': 'tijd',
            'tijd': '60',
            'woorden': '50',
            'taal': 'Frans',
            'moeilijkheid': 'makkelijk'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_expense_form_grade_valse(self):
        form = InstellingenForm(data={
            'naam': 'Anna',
            'spelmodus': 'tijd',
            'tijd': '60',
            'woorden': '50',
            'taal': 'nederlands',
            'moeilijkheid': 'easy'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_expense_form_combination(self):
        form = InstellingenForm(data={
            'naam': 'Annananananananana',
            'spelmodus': 'tijd',
            'tijd': 'duizend',
            'woorden': '50',
            'taal': 'nederlands',
            'moeilijkheid': 'easy'
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)
