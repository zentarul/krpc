import unittest
import krpctest

class TestPartsIntake(krpctest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.new_save()
        if cls.connect().space_center.active_vessel.name != 'Parts':
            cls.launch_vessel_from_vab('Parts')
            cls.remove_other_vessels()
        parts = cls.connect().space_center.active_vessel.parts
        cls.intake = parts.with_title('XM-G50 Radial Air Intake')[0].intake

    def test_properties(self):
        self.assertEqual(15, self.intake.speed)
        self.assertAlmostEqual(4.14, self.intake.flow, delta=0.05)
        self.assertAlmostEqual(0.0031, self.intake.area)

    def test_open_and_close(self):
        self.assertTrue(self.intake.open)
        self.intake.open = False
        self.assertFalse(self.intake.open)
        self.intake.open = True
        self.assertTrue(self.intake.open)

if __name__ == '__main__':
    unittest.main()
