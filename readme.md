# Build Your Own LinkTree with Python and GitHub Pages

This project provides a template and script for creating your own LinkTree (or Taplink) style landing page using Python and GitHub Pages. It allows you to generate a static webpage that displays links to your various social media profiles or other important sites.

![my analog of linktree using github page](https://github.com/user-attachments/assets/5713df1f-1161-4660-9efb-cdfd53685374)

## Overview

PythonPageLink is a static site generator that creates a personal link tree webpage. It uses Python and Jinja2 for generating HTML from a configuration file and can be easily deployed using GitHub Pages.

## Features

- **Customizable Links**: Define your links and their descriptions in a YAML file.
- **Personalization**: Customize your profile picture, bio, and site theme.
- **Easy Deployment**: Host your site on GitHub Pages with simple setup instructions.

## Project Structure

- **`config.yml`**: Configuration file for site details.
- **`generate_site.py`**: Python script to generate the static site.
- **`themes/custom/`**: Custom theme directory with assets, CSS, JavaScript, and the HTML template.
- **`docs/`**: Output directory for generated site files.

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/king-tri-ton/pythonpagelink.git
   cd pythonpagelink
   ```

2. **Install Dependencies**

   Make sure you have Python 3 and pip installed. Install the required Python packages:

   ```bash
   pip install jinja2 pyyaml
   ```

## Customization

1. **Configure Your Page**

   Edit `config.yml` to update your personal information and links. Example configuration:

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

2. **Customize Your Theme**

   - **CSS**: Modify `themes/custom/assets/css/styles.css` to adjust the styling of your site.
   - **JavaScript**: Update `themes/custom/assets/js/script.js` to add or change functionality.
   - **HTML Template**: Edit `themes/custom/index.html` for structural changes to your webpage.

## Generate Your Site

After customization, generate your static site by running:

```bash
python main.py
```

This command will create the `docs` folder with the generated files.

## Deploying on GitHub Pages

![steps to create a github page](https://github.com/user-attachments/assets/1ce1a9c2-f2d5-4cec-9d4b-e5ba9453cefb)

1. Create a new repository on GitHub.
2. Upload all files, including the `docs` folder, to the repository.
3. Go to the repository’s Settings section.
4. In the Pages section, select the `master` branch and the `/docs` folder as the source.
5. Save changes and wait for GitHub Pages to deploy your site.

Your site will now be available at `https://<username>.github.io/<repository-name>/`.

You can check the final result at [king-tri-ton.github.io/pythonpagelink](https://king-tri-ton.github.io/pythonpagelink/).

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Contact

If you have any questions or suggestions, feel free to reach out to me via [telegram](https://t.me/king_triton).
