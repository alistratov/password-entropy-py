import unittest

from data_password_entropy import password_entropy


class TestPasswordEntropy(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(password_entropy(''), 0)

    def test_not_string(self):
        with self.assertRaises(TypeError):
            password_entropy()
        self.assertEqual(password_entropy(0), 3)
        self.assertEqual(password_entropy(209), 9)
        self.assertEqual(password_entropy(None), 22)

    def test_samples(self):
        self.assertEqual(password_entropy('0'), 3)
        self.assertEqual(password_entropy(' '), 4)
        self.assertEqual(password_entropy('a'), 4)
        self.assertEqual(password_entropy("\t"), 5)
        self.assertEqual(password_entropy('123456'), 10)
        self.assertEqual(password_entropy('qwerty'), 28)
        self.assertEqual(password_entropy('P@ssw0rd'), 47)
        self.assertEqual(password_entropy('!ab#cd$'), 32)
        self.assertEqual(password_entropy('zuqiuxinyongwangkaihu'), 72)
        self.assertEqual(password_entropy('1qaz2wsx'), 41)
        self.assertEqual(password_entropy('jackslippedonicefellonhisass'), 79)
        self.assertEqual(password_entropy('JackSlippedOnIceFellOnHisAss'), 117)
        self.assertEqual(password_entropy('at&t'), 19)

        # repeating characters
        self.assertEqual(password_entropy('aa'), 7)
        self.assertEqual(password_entropy('aaa'), 7)
        self.assertEqual(password_entropy('aaaa'), 8)
        self.assertEqual(password_entropy('aaab'), 12)
        self.assertEqual(password_entropy('aaax'), 12)
        self.assertEqual(password_entropy('aaaaaaaaaaaaaaaaax'), 13)

        # pair distance
        self.assertEqual(password_entropy('abab'), 12)
        self.assertEqual(password_entropy('abba'), 14)
        self.assertEqual(password_entropy('ababab'), 14)
        self.assertEqual(password_entropy('abcd'), 13)
        self.assertEqual(password_entropy('xkcd'), 18)

        # punctuation marks from different classes
        self.assertEqual(password_entropy('!!'), 6)
        self.assertEqual(password_entropy('..'), 6)
        self.assertEqual(password_entropy('~~'), 7)

        # from public lists
        self.assertEqual(password_entropy('password1'), 43)
        self.assertEqual(password_entropy('123456789'), 12)
        self.assertEqual(password_entropy('abc123'), 21)
        self.assertEqual(password_entropy('1q2w3e4r5t6y7u8i9o0p'), 93)
        self.assertEqual(password_entropy('!!!!44yankee!!!'), 47)

    def test_unicode(self):
        self.assertEqual(password_entropy('😀'), 7)
        self.assertEqual(password_entropy('петрик п\'яточкін'), 105)
        self.assertEqual(password_entropy('жёлтаяжирнаяжирафа'), 87)
        self.assertEqual(password_entropy('Großer grüner grinsender Gorilla'), 136)

    def test_chrome_suggested(self):
        self.assertEqual(password_entropy('Vgk4@HDk6X7gEp7'), 85)
        self.assertEqual(password_entropy('2vCzzE.Zr3rNSWS'), 85)
        self.assertEqual(password_entropy('QP4ZPzuRFmCgW.f'), 91)
        self.assertEqual(password_entropy('JJ4ADWxi6pnrX@7'), 91)
