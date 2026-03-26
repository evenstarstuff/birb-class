#!/usr/bin/env python3

from pathlib import Path

import yaml
from ryland import Ryland

ROOT_DIR = Path(__file__).parent.parent
OUTPUT_DIR = ROOT_DIR / "site"
TEMPLATE_DIR = ROOT_DIR / "templates"
PANTRY_DIR = ROOT_DIR / "pantry"
DATA_DIR = ROOT_DIR / "data"

import os
url_root = os.environ.get("URL_ROOT", "/")
ryland = Ryland(output_dir=OUTPUT_DIR, template_dir=TEMPLATE_DIR, url_root=url_root)

ryland.clear_output()

##style

ryland.copy_to_output(PANTRY_DIR / "style.css")
ryland.add_hash("style.css")

## birds

for yaml_file in DATA_DIR.glob("*.yaml"):
    bird = yaml.safe_load(open(yaml_file))
    ryland.render_template("bird.html", f"birds/{bird['name'].lower().replace(' ', '-')}/index.html", {
        "bird": bird,
    })

## home page

ryland.render_template("home.html", "index.html", {
    "birds": [yaml.safe_load(open(f)) for f in DATA_DIR.glob("*.yaml")],
})