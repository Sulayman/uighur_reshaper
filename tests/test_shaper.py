"""Round-trip and shape-correctness tests for UighurReshaper."""

import unittest

from uighur_reshaper import UighurReshaper


class TestUighurReshaper(unittest.TestCase):
    def setUp(self):
        self.r = UighurReshaper()

    def test_roundtrip_preserves_text(self):
        original = " بۇ بىر سىناق خەت، بىز بۇنىڭدا خەت كېڭەيتىلگەن رايونغا ئۆزگەردىمۇ شۇنى بىلمەكچى.   "
        self.assertEqual(self.r.extend2basic(self.r.basic2extend(original)), original)

    def test_lam_alef_ligature(self):
        # ل + ا at word start → isolated ligature ﻻ (U+FEFB)
        self.assertEqual(self.r.basic2extend("لا"), "ﻻ")

    def test_lam_alef_after_connecting_letter(self):
        # ك + ل + ا → ﻛ + ﻼ (final-form ligature U+FEFC)
        out = self.r.basic2extend("كلا")
        self.assertEqual(out, "ﻛﻼ")

    def test_letter_after_lam_alef_does_not_link(self):
        # The alef in the ligature has no left-link. A following letter must
        # appear in its isolated form, not its final form.
        out = self.r.basic2extend("لا" + "م")
        self.assertEqual(out, "ﻻﻡ")  # ﻻ + ﻡ (isolated)

    def test_yeh_with_hamza_isolated(self):
        # 0x0626 standalone should render as the isolated form U+FE89, not initial.
        self.assertEqual(self.r.basic2extend("ئ"), "ﺉ")

    def test_non_arabic_passthrough(self):
        self.assertEqual(self.r.basic2extend("hello 123"), "hello 123")
        self.assertEqual(self.r.extend2basic("hello 123"), "hello 123")


if __name__ == "__main__":
    unittest.main()
