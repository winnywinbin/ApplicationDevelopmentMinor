from django.test import SimpleTestCase
from django.urls import reverse, resolve
from BVATApp.views import home, statistiek, help_view, speelscherm_tijd, speelscherm_woorden, instellingenDatabase, instellingenCustom, resultaat


class TestUrls(SimpleTestCase):

    def test_Home_url_is_resolved(self):
        url = reverse('Home')
        self.assertEquals(resolve(url).func, home)

    def test_Statistiek_url_is_resolved(self):
        url = reverse('Statistiek')
        self.assertEquals(resolve(url).func, statistiek)

    def test_Help_url_is_resolved(self):
        url = reverse('Help')
        self.assertEquals(resolve(url).func, help_view)

    def test_SpeelschermTijd_url_is_resolved(self):
        url = reverse('speelscherm-tijd')
        self.assertEquals(resolve(url).func, speelscherm_tijd)

    def test_SpeelschermWoorden_url_is_resolved(self):
        url = reverse('speelscherm-woorden')
        self.assertEquals(resolve(url).func, speelscherm_woorden)

    def test_InstellingenDataBase_url_is_resolved(self):
        url = reverse('InstellingenDataBase')
        self.assertEquals(resolve(url).func, instellingenDatabase)

    def test_InstellingenCustom_url_is_resolved(self):
        url = reverse('InstellingenCustom')
        self.assertEquals(resolve(url).func, instellingenCustom)

    def test_Resultaat_url_is_resolved(self):
        url = reverse('Resultaat')
        self.assertEquals(resolve(url).func, resultaat)