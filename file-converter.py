import sys
import markdown

if len(sys.argv) != 4:
    print("Usage: python3 file-converter.py markdown inputfile outputfile")
    sys.exit(1)

command = sys.argv[1]
input_path = sys.argv[2]
output_path = sys.argv[3]

if command != "markdown":
    print("Error: unsupported command")
    sys.exit(1)

with open(input_path, "r", encoding="utf-8") as f:
    md_text = f.read()

html = markdown.markdown(md_text)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Converted successfully") 
