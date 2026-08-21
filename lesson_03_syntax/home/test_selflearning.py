# test_tasks.py
# Автоматичні тести для перевірки виконання завдань
# Запустіть цей файл після виконання всіх завдань у файлі tasks.py

import sys
import os
from pathlib import Path

def run_tests():
    print("="*60)
    print("АВТОМАТИЧНА ПЕРЕВІРКА ЗАВДАНЬ")
    print("="*60)
    
    filedir = Path(__file__).parent
    filepath = filedir / "_selflearning01.py"
    # Перевіряємо чи існує файл з завданнями
    if not filepath.exists():
        print("❌ ПОМИЛКА: Файл 'tasks.py' не знайдено!")
        print("Переконайтеся, що ви зберегли файл з завданнями як 'tasks.py'")
        return
    
    try:
        # Імпортуємо змінні з файлу завдань
        sys.path.insert(0, '.')
        import _selflearning01 as tasks
        
        tests_passed = 0
        total_tests = 0
        
        print("Початок тестування...\n")
        
        # ТЕСТ 1: Перевірка особистих даних
        print("📋 ТЕСТ 1: Особисті дані")
        total_tests += 4
        
        if hasattr(tasks, 'student_name') and isinstance(tasks.student_name, str) and len(tasks.student_name) > 0:
            print("  ✅ student_name: правильний тип і не пустий")
            tests_passed += 1
        else:
            print("  ❌ student_name: повинна бути непустим рядком")
        
        if hasattr(tasks, 'student_age') and isinstance(tasks.student_age, int) and tasks.student_age > 0:
            print("  ✅ student_age: правильний тип і позитивне число")
            tests_passed += 1
        else:
            print("  ❌ student_age: повинен бути позитивним цілим числом")
        
        if hasattr(tasks, 'is_enrolled') and isinstance(tasks.is_enrolled, bool):
            print("  ✅ is_enrolled: правильний тип")
            tests_passed += 1
        else:
            print("  ❌ is_enrolled: повинна бути булевим значенням (True/False)")
        
        if hasattr(tasks, 'gpa_score') and isinstance(tasks.gpa_score, (int, float)) and tasks.gpa_score >= 0:
            print("  ✅ gpa_score: правильний тип і невід'ємне число")
            tests_passed += 1
        else:
            print("  ❌ gpa_score: повинен бути числом >= 0")
        
        # ТЕСТ 2: Арифметичні операції (25 та 4)
        print("\n🔢 ТЕСТ 2: Арифметичні операції")
        total_tests += 7
        
        expected_results = {
            'addition_result': 29,      # 25 + 4
            'subtraction_result': 21,   # 25 - 4
            'multiplication_result': 100,  # 25 * 4
            'division_result': 6.25,    # 25 / 4
            'floor_division_result': 6, # 25 // 4
            'modulo_result': 1,         # 25 % 4
            'power_result': 390625      # 25 ** 4
        }
        
        for var_name, expected in expected_results.items():
            if hasattr(tasks, var_name):
                actual = getattr(tasks, var_name)
                if abs(actual - expected) < 0.001:
                    print(f"  ✅ {var_name}: {actual} (правильно)")
                    tests_passed += 1
                else:
                    print(f"  ❌ {var_name}: очікувалось {expected}, отримано {actual}")
            else:
                print(f"  ❌ {var_name}: змінна не знайдена")
        
        # ТЕСТ 3: Робота з рядками
        print("\n📝 ТЕСТ 3: Обробка рядка 'Python Programming Language'")
        total_tests += 5
        
        string_tests = {
            'first_char': 'P',
            'last_char': 'e', 
            'text_length': 27,
            'first_word': 'Python',
            'last_word': 'Language'
        }
        
        for var_name, expected in string_tests.items():
            if hasattr(tasks, var_name):
                actual = getattr(tasks, var_name)
                if actual == expected:
                    print(f"  ✅ {var_name}: '{actual}' (правильно)")
                    tests_passed += 1
                else:
                    print(f"  ❌ {var_name}: очікувалось '{expected}', отримано '{actual}'")
            else:
                print(f"  ❌ {var_name}: змінна не знайдена")
        
        # ТЕСТ 4: Форматування рядків
        print("\n🎨 ТЕСТ 4: Форматування рядків")
        total_tests += 3
        
        format_tests = [
            ('greeting', ['Марія', 'звати']),
            ('age_info', ['22', 'роки']),
            ('height_info', ['1.65', 'зріст'])
        ]
        
        for var_name, required_words in format_tests:
            if hasattr(tasks, var_name):
                actual = getattr(tasks, var_name)
                if all(word in str(actual) for word in required_words):
                    print(f"  ✅ {var_name}: містить необхідні слова")
                    tests_passed += 1
                else:
                    print(f"  ❌ {var_name}: не містить всі необхідні слова {required_words}")
            else:
                print(f"  ❌ {var_name}: змінна не знайдена")
        
        # ТЕСТ 5: Конвертація типів
        print("\n🔄 ТЕСТ 5: Конвертація типів")
        total_tests += 3
        
        conversion_tests = {
            'converted_int': (123, int),
            'converted_float': (45.67, float),
            'converted_str': ('89', str)
        }
        
        for var_name, (expected_value, expected_type) in conversion_tests.items():
            if hasattr(tasks, var_name):
                actual = getattr(tasks, var_name)
                if isinstance(actual, expected_type) and (abs(actual - expected_value) < 0.001 if isinstance(expected_value, (int, float)) else actual == expected_value):
                    print(f"  ✅ {var_name}: {actual} ({expected_type.__name__}) - правильно")
                    tests_passed += 1
                else:
                    print(f"  ❌ {var_name}: очікувалось {expected_value} ({expected_type.__name__}), отримано {actual} ({type(actual).__name__})")
            else:
                print(f"  ❌ {var_name}: змінна не знайдена")
        
        # ТЕСТ 6: Математичні обчислення прямокутника
        print("\n📐 ТЕСТ 6: Площа та периметр прямокутника")
        total_tests += 2
        
        math_tests = {
            'rectangle_area': 103.75,      # 12.5 * 8.3
            'rectangle_perimeter': 41.6    # 2 * (12.5 + 8.3)
        }
        
        for var_name, expected in math_tests.items():
            if hasattr(tasks, var_name):
                actual = getattr(tasks, var_name)
                if abs(actual - expected) < 0.001:
                    print(f"  ✅ {var_name}: {actual} (правильно)")
                    tests_passed += 1
                else:
                    print(f"  ❌ {var_name}: очікувалось {expected}, отримано {actual}")
            else:
                print(f"  ❌ {var_name}: змінна не знайдена")
        
        # ТЕСТ 7: Робота з індексами рядка "Programming"
        print("\n🔍 ТЕСТ 7: Індексація рядка 'Programming'")
        total_tests += 4
        
        index_tests = {
            'char_at_0': 'P',      # Programming[0]
            'char_at_5': 'a',      # Programming[5]
            'char_at_minus_1': 'g', # Programming[-1]
            'char_at_minus_3': 'i'  # Programming[-3]
        }
        
        for var_name, expected in index_tests.items():
            if hasattr(tasks, var_name):
                actual = getattr(tasks, var_name)
                if actual == expected:
                    print(f"  ✅ {var_name}: '{actual}' (правильно)")
                    tests_passed += 1
                else:
                    print(f"  ❌ {var_name}: очікувалось '{expected}', отримano '{actual}'")
            else:
                print(f"  ❌ {var_name}: змінна не знайдена")
        
        # ТЕСТ 8: Зрізи рядка "Hello World Python"
        print("\n✂️ ТЕСТ 8: Зрізи рядка 'Hello World Python'")
        total_tests += 4
        
        slice_tests = {
            'first_five': 'Hello',         # [0:5]
            'middle_part': 'World',        # [6:11]
            'last_six': 'Python',          # [-6:]
            'every_second': 'HloWrdPto'    # [::2]
        }
        
        for var_name, expected in slice_tests.items():
            if hasattr(tasks, var_name):
                actual = getattr(tasks, var_name)
                if actual == expected:
                    print(f"  ✅ {var_name}: '{actual}' (правильно)")
                    tests_passed += 1
                else:
                    print(f"  ❌ {var_name}: очікувалось '{expected}', отримано '{actual}'")
            else:
                print(f"  ❌ {var_name}: змінна не знайдена")
        
        # ТЕСТ 9: Логічні операції
        print("\n🔗 ТЕСТ 9: Логічні операції (a=True, b=False, c=True)")
        total_tests += 4
        
        logic_tests = {
            'and_result': False,    # True and False
            'or_result': True,      # True or False
            'not_result': False,    # not True
            'complex_result': True  # (True and True) or (not False)
        }
        
        for var_name, expected in logic_tests.items():
            if hasattr(tasks, var_name):
                actual = getattr(tasks, var_name)
                if actual == expected:
                    print(f"  ✅ {var_name}: {actual} (правильно)")
                    tests_passed += 1
                else:
                    print(f"  ❌ {var_name}: очікувалось {expected}, отримано {actual}")
            else:
                print(f"  ❌ {var_name}: змінна не знайдена")
        
        # ТЕСТ 10: Складні обчислення
        print("\n🧮 ТЕСТ 10: Складні обчислення (x=10, y=3, z=2)")
        total_tests += 4
        
        complex_tests = {
            'result1': 26,              # (10 + 3) * 2
            'result2': 998,             # 10 ** 3 - 2
            'result3': 7.333333333333333, # (10 / 3) + (2 * 2)
            'result4': 5                # 10 % 3 + 2 ** 2
        }
        
        for var_name, expected in complex_tests.items():
            if hasattr(tasks, var_name):
                actual = getattr(tasks, var_name)
                if abs(actual - expected) < 0.001:
                    print(f"  ✅ {var_name}: {actual} (правильно)")
                    tests_passed += 1
                else:
                    print(f"  ❌ {var_name}: очікувалось {expected}, отримано {actual}")
            else:
                print(f"  ❌ {var_name}: змінна не знайдена")
        
        # ПІДСУМОК ТЕСТУВАННЯ
        print("\n" + "="*60)
        print("🎯 ПІДСУМОК ТЕСТУВАННЯ")
        print("="*60)
        
        percentage = (tests_passed / total_tests) * 100
        print(f"Пройдено тестів: {tests_passed}/{total_tests}")
        print(f"Відсоток виконання: {percentage:.1f}%")
        
        if percentage == 100:
            print("\n🏆 ВІДМІННО! Всі завдання виконані правильно!")
            print("   Ви чудово засвоїли основи Python!")
        elif percentage >= 90:
            print("\n🎉 ЧУДОВО! Майже всі завдання правильні!")
            print("   Перевірте кілька деталей і будете ідеальні!")
        elif percentage >= 75:
            print("\n👍 ДОБРЕ! Основи засвоєні, але є над чим попрацювати.")
            print("   Перегляньте помилки та спробуйте ще раз.")
        elif percentage >= 50:
            print("\n📚 ЗАДОВІЛЬНО. Рекомендую:")
            print("   - Переглянути матеріал лекції")
            print("   - Звернути увагу на помилки вище")
            print("   - Спробувати виправити та перетестувати")
        else:
            print("\n⚠️ ПОТРІБНО БІЛЬШЕ ПРАКТИКИ:")
            print("   - Уважно вивчіть матеріал лекції")
            print("   - Зверніться до викладача за допомогою")
            print("   - Практикуйте базові операції з Python")
        
        print("\n💡 Поради для покращення:")
        if percentage < 100:
            print("   - Уважно читайте коментарі до завдань")
            print("   - Перевіряйте типи даних (int, float, str, bool)")
            print("   - Звертайте увагу на індексацію (починається з 0)")
            print("   - Практикуйте арифметичні та логічні операції")
        
        print("\n" + "="*60)
        
    except ImportError as e:
        print(f"❌ ПОМИЛКА ІМПОРТУ: {e}")
        print("Переконайтеся, що файл 'tasks.py' не має синтаксичних помилок")
    except Exception as e:
        print(f"❌ НЕОЧІКУВАНА ПОМИЛКА: {e}")
        print("Зверніться до викладача за допомогою")

if __name__ == "__main__":
    run_tests()