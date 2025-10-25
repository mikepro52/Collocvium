import math
import logging
from typing import List
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('factorials.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)


class FactorialCalculator:

    def __init__(self):
        self._cache = [1]
        self._max_calculated = 0

    def calculate_factorials(self, n: int) -> List[int]:
        if not isinstance(n, int) or n <= 0:
            raise ValueError("n должно быть натуральным числом")

        if n > 10000:
            logger.warning(f"Вычисление {n} факториалов может занять много времени")

        if n <= len(self._cache):
            return self._cache[:n]

        for i in range(len(self._cache), n):
            try:
                next_factorial = self._cache[-1] * (i + 1)
                if math.isinf(next_factorial):
                    raise OverflowError(f"Факториал для {i + 1} превышает максимальное значение")
                self._cache.append(next_factorial)
            except OverflowError as e:
                logger.error(f"Переполнение при вычислении факториала {i + 1}: {e}")
                raise

        self._max_calculated = max(self._max_calculated, n)
        return self._cache[:n]

    def get_cache_info(self) -> dict:
        return {
            'cached_count': len(self._cache),
            'max_calculated': self._max_calculated,
            'max_cached_value': self._cache[-1] if self._cache else None
        }


def validate_input(input_str: str) -> int:
    try:
        n = int(input_str)
        if n <= 0:
            raise ValueError("Число должно быть положительным")
        return n
    except ValueError as e:
        logger.error(f"Некорректный ввод: {input_str}")
        raise ValueError(f"Некорректный ввод: {input_str}") from e


def main():
    calculator = FactorialCalculator()

    print("Вычисление последовательности факториалов")
    print("Для выхода введите 'quit'")

    while True:
        try:
            user_input = input("\nВведите натуральное число n: ").strip()

            if user_input.lower() in ('quit', 'exit', 'q'):
                print("Завершение работы...")
                break

            n = validate_input(user_input)
            factorials = calculator.calculate_factorials(n)

            print(f"Первые {n} факториалов:")
            for i, fact in enumerate(factorials, 1):
                print(f"{i}! = {fact}")

            cache_info = calculator.get_cache_info()
            logger.info(f"Вычислено {n} факториалов. В кэше: {cache_info['cached_count']}")

        except ValueError as e:
            print(f"Ошибка: {e}")
            logger.warning(f"Ошибка ввода: {e}")
        except OverflowError as e:
            print(f"Ошибка вычислений: {e}")
            logger.error(f"Переполнение: {e}")
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем")
            break
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")
            logger.exception(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical(f"Критическая ошибка: {e}")
        sys.exit(1)