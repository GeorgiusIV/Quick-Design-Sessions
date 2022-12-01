
import unittest
import QD99


class testingFunctions(unittest.TestCase):
	def testVolume(self):
		h,w,d = 10,10,10
		answer = 10*10*10
		self.assertEqual(QD99.getVolume(h,w,d),answer)

if __name__ == "__main__":
	unittest.main()