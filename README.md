# Проект автоматических тестов мобильного приложения RuDesktop

Этот проект предназначен для автоматизации тестирования мобильных приложений с использованием Python, Pytest, UIAutomator2 и Allure для отчетности.

## Структура проекта

- `tests/` — директория с тестами.
- `pages/` — директория для Page Object Model структурирования.
- `config.py` — конфигурационный файл для запуска тестов.
- `requirements.txt` — список зависимостей Python.
- `allure-results/` — [автоматически] создается директория для результатов Allure.

## Установка

1. Убедитесь, что ваш рабочий компьютер имеет установленный Python 3.7 или выше.
2. Склонируйте репозиторий проекта:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    ```

3. Перейдите в директорию проекта:

    ```bash
    cd your-repo-name
    ```

4. Установите необходимые пакеты:

    ```bash
    pip install -r requirements.txt
    ```

5. Установите и настройте Android SDK и UIAutomator2.

## Запуск тестов

1. Запустите эмулятор. 

2. Выполните команду для запуска тестов:

    ```bash
    pytest -m smoke --alluredir=allure-results
    ```


3. Для генерации отчета Allure выполните следующие команды:

    ```bash
    allure serve allure-results
    ```

## Конфигурация

По умолчанию выполняется подключение к устройству `emulator-5554`. 
Для редактирования изменить значение `device_id` в файле `config.py`. 
Так-же можно запускать тест с ключом `--device` для передачи `device_id` в момент запуска.

Для настройки параметров тестирования, таких как URL-адреса, данные пользователей и другие параметры, измените соответствующие параметры в файле `config.py`.


## Документация

- [Pytest](https://docs.pytest.org/)
- [UIAutomator2](https://github.com/openatx/uiautomator2)
- [Allure](https://docs.qameta.io/allure/)