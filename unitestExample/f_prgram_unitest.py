import unittest
from unitestExample.f_prgram_run import f

class TestF(unittest.TestCase):
    """Classe de testes para a função f."""

    def test_f_negativo(self) -> None:
        """Caso inválido: n = -1 (< 0) deve levantar ValueError.
           :return: None
        """
        with self.assertRaises(ValueError):
            f(-1)

    def test_f_zero(self) -> None:
        """Caso inicial: n = 0 deve retornar 0.
           :return: None
        """
        self.assertEqual(f(0), [0])

    def test_f_positivo(self) -> None:
        """Verifica os primeiros valores da sequência.
           :return: None
        """
        self.assertEqual(f(1), [0, 1])
        self.assertEqual(f(2), [0, 1, 1])
        self.assertEqual(f(3), [0, 1, 1, 3])
        self.assertEqual(f(4), [0, 1, 1, 3, 5])

if __name__ == '__main__':
    unittest.main()