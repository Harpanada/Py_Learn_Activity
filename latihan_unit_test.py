import unittest

def hitung_total(harga, qty):
    return harga * qty


class TestHitungTotal(unittest.TestCase):
    def tes_hitung_total(self):
        self.assertEqual(hitung_total(10, 5), 50)
        self.assertEqual(hitung_total(20, 3), 60)
 