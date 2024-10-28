from unittest import TestCase, main

#from lesson_10.ex_1.class_to_test import Worker


class TestWorker(TestCase):
    def setUp(self) -> None:
        self.worker = Worker('TestName', 1500, 50)

    def test_init_(self):
        self.assertEqual(self.worker.name, 'TestName')
        self.assertEqual(self.worker.salary, 1500)
        self.assertEqual(self.worker.energy, 50)
        self.assertEqual(self.worker.money, 0)

    def test_worker_energy_less_then_or_equal_0_raises(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual(str(ex.exception), 'Not enough energy.')
        self.worker.energy = -1
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual(str(ex.exception), 'Not enough energy.')

    def test_worker_energy_more_then_0_adds_salary_to_money(self):
        energy = self.worker.energy - 1
        money = self.worker.salary + self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money, money)
        self.assertEqual(self.worker.energy, energy)

    def test_worker_rests_energy_recharges(self):
        energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(self.worker.energy, energy)

    def test_get_info_string_returns(self):
        expected = 'TestName has saved 0 money.'
        result = self.worker.get_info()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
