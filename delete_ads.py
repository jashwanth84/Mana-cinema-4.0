import re

with open('app/src/main/java/com/manacinema/app/ui/MainScreens.kt', 'r') as f:
    content = f.read()

content = re.sub(r'// ------------------ ADS DIAGNOSTICS SCREEN ------------------.*?fun AdsDiagnosticsScreen.*?(?=\Z|// ------------------)', '', content, flags=re.DOTALL)
content = re.sub(r'fun AdsDiagnosticsScreen\(.*?(?=\Z|// ------------------)', '', content, flags=re.DOTALL)
with open('app/src/main/java/com/manacinema/app/ui/MainScreens.kt', 'w') as f:
    f.write(content)
