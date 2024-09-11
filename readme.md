# Создайте свой собственный Taplink с помощью Python и GitHub Pages

Этот проект предоставляет шаблон и скрипт для создания вашей собственной страницы в стиле Taplink с использованием Python и GitHub Pages. Он позволяет вам создать статическую веб-страницу, которая отображает ссылки на ваши различные профили в социальных сетях или другие важные сайты.

![my analog of linktree using github page](https://github.com/user-attachments/assets/5713df1f-1161-4660-9efb-cdfd53685374)

## Обзор

Taplink — это генератор статических сайтов, который создает личную веб-страницу с деревом ссылок. Он использует Python и Jinja2 для генерации HTML из конфигурационного файла и может быть легко развернут с использованием GitHub Pages.

## Возможности

- **Настраиваемые ссылки**: Определите свои ссылки и их описания в файле YAML.
- **Персонализация**: Настройте свою фотографию профиля, биографию и тему сайта.
- **Простота развертывания**: Хостинг вашего сайта на GitHub Pages с простыми инструкциями по настройке.

## Структура проекта

- **`config.yml`**: Configuration file for site details.
- **`generate_site.py`**: Python script to generate the static site.
- **`themes/custom/`**: Custom theme directory with assets, CSS, JavaScript, and the HTML template.
- **`docs/`**: Output directory for generated site files.

- **config.yml**: Конфигурационный файл для деталей сайта.
- **generate_site.py**: Скрипт на Python для генерации статического сайта.
- **themes/custom/**: Директория с пользовательской темой, содержащая ресурсы, CSS, JavaScript и HTML-шаблон.
- **docs/**: Директория для выходных файлов сгенерированного сайта.

## Настройка

1. **Клонируйте репозиторий**

   ```bash
   git clone https://github.com/king-tri-ton/pythonpagelink.git
   cd pythonpagelink
   ```

2. **Установите зависимости**

   Make sure you have Python 3 and pip installed. Install the required Python packages:

   ```bash
   pip install jinja2 pyyaml
   ```

## Персонализация

1. **Настройте вашу страницу**

   Отредактируйте `config.yml` чтобы обновить свою личную информацию и ссылки. Пример конфигурации:

   ```yaml
   name: "Vanitoo"
   picture: "assets/img/picture.jpg"
   bio: "Programmer python"
   meta:
     lang: "en"
     description: "Programmer python"
     title: "Vanitoo"
     author: "Vanitoo"
     siteUrl: "https://vanitoo.github.io/taplink/"
   links:
     - name: "Github"
       url: "https://github.com/vanitoo"
     - name: "Dev.to"
       url: "https://dev.to"
     - name: "Patreon"
       url: "https://www.patreon.com"
     - name: "Telegram"
       url: "https://t.me"
     - name: "Instagram"
       url: "https://www.instagram.com"
     - name: "Youtube"
       url: "https://www.youtube.com"
     - name: "VK"
       url: "https://www.vk.com"
     - name: "RuTube"
       url: "https://www.rutube.ru"
     - name: "Dzen"
       url: "https://www.dzen.ru"
     - name: "TikTok"
       url: "https://www.tiktor.com"
   theme: "custom"
   ```

2. **Настройте свою тему**

   - **CSS**: Измените  `themes/custom/assets/css/styles.css` to adjust the styling of your site.
   - **JavaScript**: Обновите  `themes/custom/assets/js/script.js` to add or change functionality.
   - **HTML Template**: Отредактируйте  `themes/custom/index.html` for structural changes to your webpage.

## Generate Your Site

After customization, generate your static site by running:

```bash
python main.py
```

This command will create the `docs` folder with the generated files.

## Развертывание на GitHub Pages

![steps to create a github page](https://github.com/user-attachments/assets/1ce1a9c2-f2d5-4cec-9d4b-e5ba9453cefb)


1. Создайте новый репозиторий на GitHub.
2. Загрузите все файлы, включая папку docs, в репозиторий.
3. Перейдите в раздел "Settings" вашего репозитория.
4. В разделе "Pages" выберите ветку master и папку /docs в качестве источника.
5. Сохраните изменения и подождите, пока GitHub Pages развернет ваш сайт.

Ваш сайт теперь будет доступен по адресу 'https://<username>.github.io/<repository-name>/'

Вы можете проверить конечный результат по адресу [vanitoo.github.io/taplink](https://king-tri-ton.github.io/pythonpagelink/).

## Лицензия

Этот проект лицензирован под [MIT License](https://choosealicense.com/licenses/mit/).

