import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from early_warning import compute

class EarlyWarningTests(unittest.TestCase):
    def sample(self,score=40,credit=35,market=40,liq=40):
        return {'valid':True,'asof':'2026-09-30','score':{'value':score},'blocks':{'credit':{'score':credit},'market':{'score':market},'liq':{'score':liq}}}
    def test_early_september(self):
        self.assertEqual(compute(self.sample())['state'],'normal')
    def test_september_30(self):
        self.assertEqual(compute(self.sample(63.3,60.8,59.5,62))['state'],'high')
    def test_november_20(self):
        self.assertEqual(compute(self.sample(60.3,71.9,61,50.8))['state'],'high')
    def test_missing_is_unknown(self):
        a=self.sample();del a['blocks']['credit'];self.assertEqual(compute(a)['state'],'unknown')
    def test_invalid_is_unknown(self):
        a=self.sample();a['valid']=False;self.assertEqual(compute(a)['state'],'unknown')
if __name__=='__main__':unittest.main()
