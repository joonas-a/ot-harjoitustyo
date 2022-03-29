import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassapaate_saldo_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisia_ei_myyty_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaita_ei_myyty_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kateisosto_toimii_maksu_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_kateisosto_toimii_maksu_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_kateisosto_raha_ei_riita_ja_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_kateisosto_raha_ei_riita_ja_palautetaan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_maksu_kortilla_toimii_oikein(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.test_kassapaate_saldo_oikein()

    def test_maukas_maksu_kortlla_toimii_oikein(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.test_kassapaate_saldo_oikein()

    def test_edullinen_korttiosto_epaonnistuu(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(kortti.saldo, 100)

    def test_maukas_korttiosto_epaonnistuu(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(kortti.saldo, 200)

    def test_rahan_lataus_kortille_toimii_oikein(self):
        kortti = Maksukortti(3000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 123)
        self.assertEqual(kortti.saldo, 3123)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100123)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(kortti, -100), None)
        self.assertEqual(kortti.saldo, 1000)