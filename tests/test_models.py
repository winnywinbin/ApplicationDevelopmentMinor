# from django.test import TestCase
# from BVATApp.models import Woord
#
#
# class YourTestClass(TestCase):
#     def setUp(self):
#         Woord.objects.create(id='1', woord='Water', taal='Nederlands', moeilijkheidsgraad='makkelijk')
#
#     def test_id_label(self):
#         id = Woord.objects.get(id=1)
#         field_label = id._meta.get_field('woord').verbose_name
#         self.assertEqual(field_label, 'woord')
#
#     def tearDown(self):
#         # Clean up run after every test method.
#         pass
