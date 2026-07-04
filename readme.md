# Taplink

Self-hosted статическая страница ссылок в стиле Link-in-bio: YAML-конфигурация → Python/Jinja2 → готовый сайт для GitHub Pages.

Без базы данных, CMS, подписки и набора микросервисов, который обычно появляется там, где человеку просто нужно разместить пять ссылок.

![Preview](https://github.com/user-attachments/assets/5713df1f-1161-4660-9efb-cdfd53685374)

## Возможности

- Статическая страница ссылок с профилем, описанием и кнопками.
- Настройка через один файл `config.yml`.
- Шаблоны на Jinja2 и кастомная тема.
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

## Настройка

Скопируйте пример конфигурации:

```bash
cp config.example.yml config.yml
```

На Windows можно просто открыть `config.example.yml`, сохранить копию как `config.yml` и заполнить данные.

Пример:

```yaml
name: "Your name"
picture: "assets/img/picture.jpg"
bio: "DevOps engineer, creator and problem solver"
meta:
  lang: "ru"
  description: "Personal link page"
  title: "Your name"
  author: "Your name"
  siteUrl: "https://username.github.io/taplink/"
links:
  - name: "Telegram"
    url: "https://t.me/username"
  - name: "GitHub"
    url: "https://github.com/username"
theme: "custom"
```

### Тема

- HTML: `themes/custom/index.html`
- CSS: `themes/custom/assets/css/styles.css`
- JavaScript: `themes/custom/assets/js/script.js`
- Изображения и другие файлы: `themes/custom/assets/`

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
├── config.yml                 # личные данные и ссылки
├── config.example.yml         # безопасный пример конфигурации
├── main.py                    # генератор статической страницы
├── requirements.txt           # Python-зависимости
├── themes/custom/             # шаблон, стили и assets
├── docs/                      # результат сборки
└── .github/workflows/         # автоматическая публикация
```

## Roadmap

### v0.2 — Project foundation

- [x] Актуальная документация.
- [x] Изолированные Python-зависимости.
- [x] Пример конфигурации.
- [x] `.gitignore` и MIT License.
- [x] Автоматическая сборка и deploy в GitHub Pages.

### Следующие версии

- Темная и светлая темы.
- Open Graph, favicon и корректные превью в мессенджерах.
- QR-код страницы.
- Иконки платформ и дополнительные типы кнопок.
- Click analytics без отдельного сервера.

## Лицензия

[MIT](LICENSE)
