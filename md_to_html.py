import markdown
import sys


with open(sys.argv[1], "r", encoding="utf-8") as f_in:
        contents = f_in.read()
        md_to_html = markdown.markdown(contents)
with open(sys.argv[2], "w", encoding="utf-8") as f_out:
        f_out.write(md_to_html)

