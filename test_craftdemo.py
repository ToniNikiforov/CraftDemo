import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_Github_data(self):
        self.assertIsNotNone(main.Github_Email)
        self.assertIsNot(main.Github_Name,'',None)
    try:
        def test_UpdateContact(self):
            self.assertEqual(main.Freshdesk_UpdateResponse, 200)
    except:
        def test_CreateContact(self):
            self.assertEqual(main.Freshdesk_CreateResponse,200)






if __name__ == '__main__':
    unittest.main()
