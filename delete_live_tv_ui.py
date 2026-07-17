import re

with open('app/src/main/java/com/manacinema/app/ui/MainScreens.kt', 'r') as f:
    content = f.read()

content = re.sub(r'// ------------------ LIVE TV SCREEN ------------------.*?fun LiveTvScreen.*?(?=\Z|// ------------------)', '', content, flags=re.DOTALL)
content = content.replace('PLAY_MOVIE, PLAY_SERIES, PLAY_LIVETV', 'PLAY_MOVIE, PLAY_SERIES')
content = content.replace('        Triple(Screen.PLAY_LIVETV, "Live TV", Icons.Default.Tv),\n', '')
content = content.replace('        Triple(Screen.PLAY_LIVETV, "Live TV", Icons.Default.Tv)', '')

nav_replace = """                    Screen.PLAY_LIVETV -> {
                        // Removed
                    }"""
content = re.sub(r'                    Screen\.PLAY_LIVETV -> \{.*?\}\n', '', content, flags=re.DOTALL)

with open('app/src/main/java/com/manacinema/app/ui/MainScreens.kt', 'w') as f:
    f.write(content)
