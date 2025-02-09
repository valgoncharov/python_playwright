import os
import pytest
from playwright.sync_api import Playwright, sync_playwright
from playwright.sync_api import Page, Route, expect


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


#Локатор or ???
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


#Чек боксы и переключатели - использование клик
def test_checkbox_use_click(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").click()
    page.locator("text=Checked checkbox").click()
    page.locator("text=Default radio").click()
    page.locator("text=Default checked radio").click()
    page.locator("text=Checked switch checkbox input").click()


#Выпадающий список использование select_option()
def test_select(page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#floatingSelect', value="3")
    page.select_option('#floatingSelect', index=1)
    page.select_option('#floatingSelect', label="Нашел и завел bug")


#По умолчанию используется поиск по value. Вы можете использовать синтаксис, без явного указания стратегии поиска
def test_select_without_vlue(page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#floatingSelect', "3")
    page.select_option('#floatingSelect', index=1)
    page.select_option('#floatingSelect', label="Нашел и завел bug")


#Если в вашем приложении реализован множественный выбор в выпадающем списке, то для реализации данного сценария необходимо передать массив опций, который требуется выбрать.
def test_select_multiple(page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#skills', value=["playwright", "python"])


#Drag and Drop
def test_drag_and_drop(page):
    page.goto('https://zimaev.github.io/draganddrop/')
    page.drag_and_drop("#drag", "#drop")


#Диалоговые окна
def test_dialogs(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    page.get_by_text("Диалог Alert").click()
    page.get_by_text("Диалог Confirmation").click()
    page.get_by_text("Диалог Prompt").click()


#Cценарий в котором необходимо нажать кнопку "OK"
def test_dialogs_scenario_ok(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_text("Диалог Confirmation").click()


# чтобы получить сообщение отображаемое в диалоговом окне.
# добавить print() в lambda и самое главное не ставить () после dialog.message
def test_dialogs_scenario_ok1(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://zimaev.github.io/dialog/")
    page.on("dialog", lambda dialog: dialog.accept())
    print('\n')
    page.on("dialog", lambda dialog: print(dialog.message))
    page.get_by_role("button", name="Диалог Confirmation").click()


#Загрузка файла
def test_upload_file(page):
    page.goto('https://zimaev.github.io/upload/')
    page.set_input_files("#formFile", "hello.txt")
    page.locator("#file-submit").click()


#Вы можете зарегистрировать обработчик события "filechooser" и получить тот-же результат.
def test_upload_file_lambda(page):
    page.goto('https://zimaev.github.io/upload/')
    page.on("filechooser", lambda file_chooser: file_chooser.set_files("hello.txt"))
    page.locator("#formFile").click()


#Другой вариант записи теста
def test_upload_file_use_set(page):
    page.goto('https://zimaev.github.io/upload/')
    with page.expect_file_chooser() as fc_info:
        page.locator("#formFile").click()
    file_chooser = fc_info.value
    file_chooser.set_files("hello.txt")


#Скачать файл с оригиналом имени файли
def test_download(page):

    page.goto("https://demoqa.com/upload-download", wait_until='commit')

    with page.expect_download() as download_info:
        page.locator("a:has-text(\"Download\")").click()

    download = download_info.value
    file_name = download.suggested_filename
    destination_folder_path = "./data/"
    download.save_as(os.path.join(destination_folder_path, file_name))


#Скачать файл с присвоением своего имени файла
def test_download_with_name(page):

    page.goto("https://demoqa.com/upload-download", wait_until='commit')

    with page.expect_download() as download_info:
        page.locator("a:has-text(\"Download\")").click()

    download = download_info.value
    destination_folder_path = "./data/"
    download.save_as(os.path.join(destination_folder_path, "foto1.jpeg"))


#Получение значений элемента innerText умеет считывать стили и не возвращает содержимое скрытых элементов, тогда как textContent этого не делает.
def test_get_data_use_inner_text(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print('\n')
    print(row.all_inner_texts())


#Получение значений элемента textContent получает содержимое всех элементов, включая <script> и <style>, тогда как innerText этого не делает.
def test_get_data_use_text_content(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator("tr")
    print('\n')
    print(row.all_text_contents())


#Получение значений элемента: можно получить HTML-код элемента.
def test_get_data_use_html(page):
    page.goto('https://zimaev.github.io/table/')
    row = page.locator('div.container')
    print('\n')
    print(row.inner_html())


#Создание скриншотов
def test_get_screenshot(page):
    page.goto('https://zimaev.github.io/table/')
    page.screenshot(path="screenshots/screenshot.png")


def test_get_full_screenshot(page):
    page.goto('https://zimaev.github.io/table/')
    page.screenshot(path="screenshots/full_page_screenshot.png", full_page=True)


def test_get_element_screenshot(page):
    page.goto('https://zimaev.github.io/table/')
    page.locator("div.container").screenshot(path="screenshots/element_screenshot.png")


def test_get_clip_screenshot(page):
    page.goto('https://zimaev.github.io/table/')
    page.screenshot(path="screenshots/clipped_image.png", clip={"x": 50, "y": 0, "width": 400, "height": 300})


#Работа с несколькими вкладками(Tabs)
def test_new_tab(page):
    page.goto("https://zimaev.github.io/tabs/")
    with page.context.expect_page() as tab:
        page.get_by_text("Переход к Dashboard").click()

    new_tab = tab.value
    assert new_tab.url == "https://zimaev.github.io/tabs/dashboard/index.html?"
    sign_out = new_tab.locator('.nav-link', has_text='Sign out')
    assert sign_out.is_visible()


#expect()  -  вспомогательная функция реализующая процесс опроса страницы
def test_foobar(page: Page):
    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page.get_by_text("Name"), "Сообщение не отображается на странице").to_be_visible()


def test_add_todo_expect(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    expect(page.locator('h2')).to_be_visible()


#Проверки (Assertions)
def test_todo(page):
    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page).to_have_url("https://demo.playwright.dev/todomvc/#/")
    input_field = page.get_by_placeholder('What needs to be done?')
    expect(input_field).to_be_empty()
    input_field.fill("Закончить курс по playwright")
    input_field.press('Enter')
    input_field.fill("Добавить в резюме, что умею автоматизировать")
    input_field.press('Enter')
    todo_item = page.get_by_test_id('todo-item')
    expect(todo_item).to_have_count(2)


#Мониторинг сетевых запросов
def test_listen_network(page: Page):
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto('https://osinit.ru/')


#Модифицировать запрос
def test_network(page):
    page.route("**/register", lambda route: route.continue_(post_data='{"email": "user","password": "secret"}'))
    page.goto('https://reqres.in/')
    page.get_by_text(' Register - successful ').click()


#Модифицировать ответ
def test_mock_tags(page):
    page.route("**/api/tags", lambda route: route.fulfill(path="data.json"))
    page.goto('https://demo.realworld.io/#/')


#Мокинг данных
def test_intercepted(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        json = response.json()
        json["tags"] = ["open", "solutions"]
        route.fulfill(json=json)

    page.route("**/api/tags", handle_route)

    page.goto("https://demo.realworld.io/#/")
    sidebar = page.locator('css=div.sidebar')
    expect(sidebar.get_by_role('link')).to_contain_text(["open", "solutions"])


#Воспроизведение из HAR???
def test_replace_from_har(page):
    page.goto("https://reqres.in/")
    page.route_from_har("example.har")
    users_single = page.locator('li[data-id="users-single"]')
    users_single.click()
    response = page.locator('[data-key="output-response"]')
    expect(response).to_contain_text("Open Solutions")


#???
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(service_workers="block")
    context.route_from_har("C:\\Users\\Valentin\\PycharmProjects\\python_playwright\\example.har", url="**/api/users/2")
    page = context.new_page()
    page.locator("html").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)


#Тестирование API - GET
def test_inventory(page):
    response = page.request.get('https://petstore.swagger.io/v2/store/inventory')
    print(f'\nСтатус код: {response.status}')
    print(f'Тело ответа: {response.json()}')


#Тестирование API - POST
def test_add_user(page):
    data = [
              {
                "id": 9743,
                "username": "fsd",
                "firstName": "fff",
                "lastName": "ggg",
                "email": "bbb",
                "password": "tt",
                "phone": "333",
                "userStatus": 0
              }
            ]
    header = {
        'accept': 'application/json',
        'content-Type': 'application/json'
    }
    response = page.request.post('https://petstore.swagger.io/v2/user/createWithArray', data=data, headers=header)
    print(f'\nСтатус код: {response.status}')
    print(f'Тело ответа: {response.json()}')