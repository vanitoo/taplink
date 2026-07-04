# Taplink

Self-hosted статическая страница-визитка в стиле Link-in-bio: `config.json` → Python/Jinja2 → готовый сайт для GitHub Pages.

Без базы данных, CMS, подписки и набора микросервисов, который обычно появляется там, где человеку просто нужно разместить пять ссылок и QR-код.

![Preview](https://github.com/user-attachments/assets/5713df1f-1161-4660-9efb-cdfd53685374)

## Возможности

- Статическая страница-визитка с аватаром, описанием и кнопками.
- Настройка через один файл `config.json`.
- JSON не зависит от отступов: редактируется даже обычным Блокнотом.
- Социальные кнопки в отдельном блоке `socials`.
- Типы ссылок: `telegram`, `whatsapp`, `email`, `call`, `link`.
- Open Graph и Twitter preview для красивого отображения в мессенджерах.
- SVG favicon.
- Автоматическая генерация QR-кода страницы.
- Светлая и тёмная тема с сохранением выбора в браузере.
- Mobile-first адаптивная вёрстка.
- Сборка локально или автоматически через GitHub Actions.
- Публикация на GitHub Pages без отдельного сервера.

## Быстрый старт

```bash
git clone https://github.com/vanitoo/taplink.git
cd taplink
python -m venv .venv
```

Активируйте виртуальное окружение:

```bash
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

Установите зависимости и соберите сайт:

```bash
pip install -r requirements.txt
python main.py
```

После сборки готовая страница появится в `docs/index.html`.

## Настройка страницы

Откройте в Блокноте файл `config.json` в корне проекта. Все данные страницы находятся там.

### Аватар

```json
"picture": "assets/img/picture.jpg"
```

Проще всего заменить файл `themes/custom/assets/img/picture.jpg` своим изображением с тем же именем.

### Социальные иконки

```json
"socials": [
  { "name": "Telegram", "url": "https://t.me/username", "icon": "TG" },
  { "name": "GitHub", "url": "https://github.com/username", "icon": "GH" }
]
```

Поле `icon` сейчас текстовое. Можно использовать короткую подпись вроде `TG`, `GH`, `VK` или символ.

### Основные кнопки

```json
"links": [
  { "name": "Telegram", "url": "https://t.me/username", "type": "telegram" },
  { "name": "WhatsApp", "url": "https://wa.me/79990000000", "type": "whatsapp" },
  { "name": "Email", "url": "mailto:hello@example.com", "type": "email" },
  { "name": "Call", "url": "tel:+79990000000", "type": "call" }
]
```

Доступные типы:

- `telegram`
- `whatsapp`
- `email`
- `call`
- `link`

Важно: запятая нужна **между** блоками, но не после последнего. Если допустить ошибку, генератор покажет номер строки и символ.

### Open Graph

Для красивого превью в Telegram, VK, LinkedIn и других сервисах настройте блок `meta`:

```json
"meta": {
  "lang": "ru",
  "locale": "ru_RU",
  "description": "Personal link page",
  "title": "Your name",
  "author": "Your name",
  "siteUrl": "https://username.github.io/taplink/",
  "ogImage": "https://username.github.io/taplink/assets/img/picture.jpg"
}
```

`siteUrl` используется и для генерации QR-кода.

Для чистого старта используйте `config.example.json` как образец.

## Тема и внешний вид

- HTML: `themes/custom/index.html`
- CSS: `themes/custom/assets/css/styles.css`
- JavaScript: `themes/custom/assets/js/script.js`
- Изображения и другие файлы: `themes/custom/assets/`

Светлая и тёмная тема переключаются кнопкой на странице. Выбор сохраняется в браузере через `localStorage`.

## QR-код

QR-код генерируется автоматически при запуске:

```bash
python main.py
```

Файл появляется здесь:

```text
docs/assets/img/qr-code.png
```

## Публикация на GitHub Pages

В репозитории есть workflow `.github/workflows/deploy-pages.yml`.

1. Откройте **Settings → Pages**.
2. В разделе **Build and deployment** выберите **GitHub Actions**.
3. Сделайте push в ветку `master`.
4. После успешного workflow страница будет опубликована по адресу:

```text
https://<username>.github.io/taplink/
```

Для проверки локально откройте `docs/index.html` в браузере.

## Структура проекта

```text
├── config.json                # личные данные, ссылки, соцсети и meta
├── config.example.json        # безопасный пример конфигурации
├── main.py                    # генератор статической страницы и QR-кода
├── requirements.txt           # Python-зависимости
├── themes/custom/             # шаблон, стили и assets
├── docs/                      # результат сборки
└── .github/workflows/         # автоматическая публикация
```

## Roadmap

### v0.2 — Project foundation

- [x] Актуальная документация.
- [x] JSON-конфигурация, удобная для ручного редактирования.
- [x] Изолированные Python-зависимости.
- [x] Пример конфигурации.
- [x] `.gitignore` и MIT License.
- [x] Автоматическая сборка и deploy в GitHub Pages.

### v0.3 — Portfolio card

- [x] Новый адаптивный интерфейс.
- [x] Аватар через `config.json`.
- [x] Социальные иконки.
- [x] Open Graph и Twitter preview.
- [x] SVG favicon.
- [x] QR-код страницы.
- [x] Светлая и тёмная тема.
- [x] Кнопки Telegram / WhatsApp / Email / Call.
- [x] Mobile-first вёрстка.

### Следующие версии

- Настоящие SVG-иконки платформ.
- Несколько готовых визуальных тем.
- Click analytics без отдельного сервера.
- Кнопка экспорта/импорта конфигурации.

## Лицензия

[MIT](LICENSE)
