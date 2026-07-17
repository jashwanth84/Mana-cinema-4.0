import re

with open('app/src/main/java/com/manacinema/app/ui/MainScreens.kt', 'r') as f:
    content = f.read()

content = re.sub(r'// ------------------ LIVETV SCREEN ------------------.*?fun LiveTvScreen.*?(?=\Z|// ------------------)', '', content, flags=re.DOTALL)
content = content.replace(', LIVETV,', ',')
content = content.replace(', PLAY_LIVETV', '')
content = content.replace('    val liveTvChannel: com.manacinema.app.models.LiveTvChannel? = null,\n', '')
content = content.replace('    val liveTvChannel: LiveTvChannel? = null,\n', '')

content = re.sub(r'                    Screen\.LIVETV -> LiveTvScreen.*?\}\)\n', '', content, flags=re.DOTALL)
content = re.sub(r'                    Screen\.PLAY_LIVETV -> state\.liveTvChannel\?\.let \{ channel ->.*?\}\n', '', content, flags=re.DOTALL)

# Bottom Nav Item
content = content.replace('        Triple(Screen.LIVETV, "Live TV", Icons.Default.Tv),\n', '')

# Floating video
content = re.sub(r'                                \} else if \(fState\.type == "livetv"\) \{.*?\}\n', '\n', content, flags=re.DOTALL)


with open('app/src/main/java/com/manacinema/app/ui/MainScreens.kt', 'w') as f:
    f.write(content)
