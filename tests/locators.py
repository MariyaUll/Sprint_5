# --- Главная страница ---
BTN_ENTER_ACCOUNT = "//button[normalize-space()='Войти в аккаунт']"
BTN_PERSONAL_CABINET = 'a[href*="/account"]'

# --- Форма входа ---
INPUT_LOGIN =  "//label[normalize-space()='Email']/following-sibling::input[1]"
INPUT_PASSWORD = "//label[normalize-space()='Пароль']/following-sibling::input[1]"
BTN_LOGIN_SUBMIT = "//button[normalize-space()='Войти']"

# --- Форма регистрации ---
BTN_SIGN_UP = 'a[href*="/register"]'
INPUT_NAME = "//label[normalize-space()='Имя']/following-sibling::input[1]"
BTN_REGISTER_SUBMIT = "//button[normalize-space()='Зарегистрироваться']"
ERR_MSG_REG = "//p[normalize-space()='Некорректный пароль']"

# --- Личный кабинет ---
BTN_LOGOUT = "//button[normalize-space()='Выход']"
BTN_SIGN_UP = 'a[href*="/register"]'

# --- Восстановление пароля ---
BTN_FORGOT_PASSWORD = 'a[href*="/forgot-password"]'
BTN_LOGIN = 'a[href*="/login"]'

# --- Конструктор бургеров ---
BTN_CONSTRUCTOR = "//a[normalize-space()='Конструктор']"
H1_ASSEMBLE_BURGER = "//h1[normalize-space()='Соберите бургер']"
LOGO_STELLAR_BURGERS = 'a[href*="/"]'
BTN_ORDER = "//button[normalize-space()='Оформить заказ']"

# --- Разделы конструктора ---
TAB_BUNS = "//div[normalize-space()='Булки']"
TAB_SAUCES = "//div[normalize-space()='Соусы']"
TAB_INGREDIENTS = "//div[normalize-space()='Начинки']"
