"""Build index.html from src/template.html, embedding the fonts.

Edit src/template.html, then run:  python3 build.py
"""
import base64, pathlib

root = pathlib.Path(__file__).parent
html = (root / "src" / "template.html").read_text(encoding="utf-8")
for token, name in [("__F400__", "regular"), ("__F500__", "medium"), ("__F700__", "bold")]:
    data = (root / "fonts" / f"sfpro-{name}.woff").read_bytes()
    html = html.replace(token, base64.b64encode(data).decode())
(root / "index.html").write_text(html, encoding="utf-8")
print("Built index.html")
