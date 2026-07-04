import json
import os
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


ROOT_DIR = Path(__file__).parent
CONFIG_PATH = ROOT_DIR / "config.json"
OUTPUT_DIR = ROOT_DIR / "docs"


def load_config() -> dict:
    try:
        with CONFIG_PATH.open("r", encoding="utf-8") as config_file:
            return json.load(config_file)
    except FileNotFoundError as error:
        raise SystemExit(
            "Не найден config.json. Создайте его на основе config.example.json."
        ) from error
    except json.JSONDecodeError as error:
        raise SystemExit(
            f"Ошибка в config.json: строка {error.lineno}, символ {error.colno}. "
            "Проверьте запятые, кавычки и скобки."
        ) from error


def main() -> None:
    config = load_config()
    theme_name = config.get("theme", "custom")

    OUTPUT_DIR.mkdir(exist_ok=True)

    env = Environment(loader=FileSystemLoader(ROOT_DIR / "themes" / theme_name))
    template = env.get_template("index.html")

    output_html = template.render(config=config)
    (OUTPUT_DIR / "index.html").write_text(output_html, encoding="utf-8")

    assets_source = ROOT_DIR / "themes" / theme_name / "assets"
    assets_dest = OUTPUT_DIR / "assets"
    if assets_source.exists():
        shutil.copytree(assets_source, assets_dest, dirs_exist_ok=True)

    print("Site generated successfully.")


if __name__ == "__main__":
    main()
