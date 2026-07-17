import re

with open('app/src/main/java/com/manacinema/app/repository/MovieRepository.kt', 'r') as f:
    content = f.read()

content = re.sub(r'    fun getLiveTvChannelsFromFirebase.*?return@callbackFlow\n    }\n', '', content, flags=re.DOTALL)

with open('app/src/main/java/com/manacinema/app/repository/MovieRepository.kt', 'w') as f:
    f.write(content)
