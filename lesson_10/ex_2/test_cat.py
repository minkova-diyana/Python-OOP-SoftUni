from unittest import TestCase, main

#from lesson_10.ex_2.class_test import Cat


class TestCat(TestCase):
    def setUp(self) -> None:
        self.cat = Cat('TestName')

    def test_init_if_works(self):
        self.assertEqual(self.cat.name, 'TestName')
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(self.cat.size, 0)

    def test_cat_eat_when_the_cat_fed_is_true_raises(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual(str(ex.exception), 'Already fed.')

    def test_cat_eat_when_the_cat_fed_is_false(self):
        size = self.cat.size + 1
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(self.cat.size, size)

    def test_cat_sleep_when_is_not_fed_raises(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

    def test_cat_sleep_when_is_fed(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
