import pytest
from playwright.sync_api import Playwright


def test_add_todo(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_role("checkbox", name="Toggle Todo").check()

    # ---------------------
    context.close()
    browser.close()


def test_add_todo1(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")


#Пропустить тест браузером
@pytest.mark.only_browser("chromium")
def test_visit_example(page):
    page.goto("https://example.com")
    # ...


#Запуск в определенном браузере
@pytest.mark.skip_browser("firefox")
def test_visit_example(page):
    page.goto("https://example.com")
    # ...


def test_loc(page):
    page.goto('https://zimaev.github.io/text_input/')
    page.get_by_label("Email address").fill("qa@example.com")
    page.get_by_title("username").fill("Anton")
    page.get_by_placeholder('password').fill("secret")
    page.get_by_role('checkbox').click()


# Действия с веб элементами - ввод текста
def test_login(page):
    page.goto('https://zimaev.github.io/text_input/')
    page.locator("#exampleInputEmail1").fill("admin@example.com")


# Действия с веб элементами - передача посимвольно
def test_use_type_login(page):
    page.goto('https://zimaev.github.io/text_input/')
    page.locator("#exampleInputEmail1").type("admin@example.com")


# Действия с веб элементами - двойное нажатие
def test_use_db_click_login(page):
    page.goto('https://zimaev.github.io/text_input/')
    page.get_by_text("Submit").dblclick()


# Действия с веб элементами - Метод pressSequentially последовательно отправляет нажатия клавиш к элементу, имитируя процесс набора текста вручную
def test_use_press_login(page):
    page.goto('https://zimaev.github.io/text_input/')
    page.locator("#exampleInputEmail1").press_sequentially("world", delay=100)


#Локатор or
def test_or(page):
    selector = page.locator("input").or_(page.locator("text"))
    selector.fill("Hello Stepik")


def test_locator_and(page):
    page.goto("https://zimaev.github.io/locatorand/")
    selector = page.get_by_role("button", name="Sing up").and_(page.get_by_title("Sing up today"))
    selector.click()


#Цепочка локаторов
def test_locator_as_chain(page):
    page.goto("https://zimaev.github.io/navbar/")
    page.locator("#navbarNavDropdown >> li:has-text('Company')").click()


#Цепочка локаторов - сохранение веб-элемента в переменную
def test_locator_as_chain_variable(page):
    page.goto("https://zimaev.github.io/navbar/")
    nav_bar = page.locator('div#navbarNavDropdown')
    nav_bar.locator("li:has-text('Company')").click()


#Фильтрация
def test_locator_filter(page):
    page.goto("https://zimaev.github.io/filter/")
    row_locator = page.locator("tr")
    total = row_locator.filter(has_not=page.get_by_role("button")).count()
    print(f'"\nКоличество элементов на странице: {total}')


#Фильтрация отсутствует текст
def test_locator_filter1(page):
    page.goto("https://zimaev.github.io/filter/")
    row_locator = page.locator("tr")
    row_locator.filter(has_not_text="helicopter")


#Фильтрация комбинирование ???
def test_locator_filter2(page):
    page.goto("https://zimaev.github.io/filter/")
    row_locator = page.locator("tr")
    row_locator.filter(has_text="text in column 1")
    row_locator.filter(has=page.get_by_role("button", name="column 2 button"))
    row_locator.click()


#Работа с несколькими элементами
def test_locator_some(page):
    page.goto("https://zimaev.github.io/filter/")
    total = page.get_by_role("button").count()
    page.get_by_role("listitem").nth(1)
    print(f'"\nКоличество элементов на странице: {total}')


#Работа с несколькими элементами
def test_locator_some_role(page):
    page.goto("https://zimaev.github.io/filter/")
    page.get_by_role("listitem").nth(1)


#Работа с несколькими элементами
def test_locator_some_checkbox0(page):
    page.goto("https://zimaev.github.io/checks-radios/")
    total = page.get_by_role("button").count()
    print(f'"\nКоличество элементов на странице: {total}')


#Работа с несколькими элементами
def test_locator_some_checkbox1(page):
    page.goto("https://zimaev.github.io/navbar/")
    total = page.get_by_role("button").count()
    print(f'"\nКоличество элементов на странице: {total}')


#Работа с несколькими элементами
def test_locator_some_checkbox2(page):
    page.goto("https://zimaev.github.io/checks-radios/")
    page.get_by_role("listitem").nth(1)
    total = page.get_by_role("checkbox").count()
    print(f'"\nКоличество элементов на странице: {total}')


#Работа с несколькими элементами
def test_locator_some_checkbox(page):
    page.goto("https://zimaev.github.io/checks-radios/")
    checkbox = page.locator("input")
    for i in range(checkbox.count()):
        checkbox.nth(i).click()


#Работа со всем элементами (поиск по всем элементам)
def test_locator_all_checkbox(page):
    page.goto("https://zimaev.github.io/checks-radios/")
    checkboxes = page.locator("input")
    for checkbox in checkboxes.all():
        checkbox.check()


#Чек боксы и переключатели
def test_checkbox(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").check()
    page.locator("text=Checked checkbox").check()
    page.locator("text=Default radio").check()
    page.locator("text=Default checked radio").check()
    page.locator("text=Checked switch checkbox input").check()
