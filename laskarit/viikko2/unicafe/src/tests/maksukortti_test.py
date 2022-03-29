import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_saldon_kasvattaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "saldo: 2.1")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_ei_voi_nostaa_liikaa_rahaa(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_metodi_palauttaa_true_onnistuessaan(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)

    def test_metodi_palauttaa_false_epäonnistuessaan(self):
        self.assertEqual(self.maksukortti.ota_rahaa(20), False)