import unittest

import Opgave1
import Opgave2
import Opgave3
import Opgave4
import Opgave5
import Opgave6

class TestTheExercisesForAfleveringsopgave1(unittest.TestCase):

    def test_gangTalMed7(self):
        #tester om 7*10 = 70
        self.assertEqual(Opgave1.gangTalMed7(10),70)
        #Tester randværdier
        self.assertEqual(Opgave1.gangTalMed7(1),7)
        self.assertEqual(Opgave1.gangTalMed7(-1),-7)
        #Tester reelle tal
        self.assertEqual(Opgave1.gangTalMed7(2.25),15.75)
        #Tester at strenge ikke kan håndteres
        self.assertNotEqual(Opgave1.gangTalMed7("10"),70)

    def test_laegtotalsammen(self):
        #Nu testes Opgave 2, hvor to tal lægges sammen
        #Først testes vha self.assert, hvor man indsætter to tal (inputtal1 og inputtal2),
        #og tjekker om de giver et tredje
        self.assertEqual(Opgave2.lægToTalSammen(7,10),17)

        #her er inputtal1 og inputtal2 ikke lig med resulatatet, så den printer det rigtige resultat i stedet
        self.assertNotEqual(Opgave2.lægToTalSammen(4,10),16)

        #vi kan også testes om koden kan klare negative teal, således:
        self.assertEqual(Opgave2.lægToTalSammen(-7,10),3)
        self.assertNotEqual(Opgave2.lægToTalSammen(-7,10),17)

        #nu tester vi så, om den kan klare deimaltal:
        self.assertEqual(Opgave2.lægToTalSammen(7.1,9.9),17)

        #tilsidst testes kodens ability til at håndtere skrift:
        self.assertNotEqual(Opgave2.lægToTalSammen("7","10"),17)

    def test_laegToStrengeSammen(self):
        self.assertEqual(Opgave3.lægToStrengeSammen("Vi havde ferie i uge"," 42"),"Vi havde ferie i uge 42")

    def test_talletErStoerreEndTI(self):
        #tester at 4 ikke er større end 10
        self.assertNotEqual(Opgave4.talletErStørreEndTI(4),1)
        #tester at 11 er større end 10
        self.assertEqual(Opgave4.talletErStørreEndTI(11),1)

    def test_printInputvaerdiFraInputVaerdiTilNul(self):
        self.assertEqual(Opgave5.printInputværdiFraInputVærdiTilNul(10),0)

    def test_getValutasKurs(self):
        self.assertEqual(Opgave6.getValutasKurs("EUR"),744.12)


if __name__ == '__main__':
    unittest.main()
