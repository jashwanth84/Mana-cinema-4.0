import re

with open('app/src/main/java/com/manacinema/app/database/models/Models.kt', 'r') as f:
    content = f.read()

content = content.replace('data class CastMember(val name: String = "", val photo: String = "")\npackage com.manacinema.app.models\n', 'package com.manacinema.app.models\n\ndata class CastMember(val name: String = "", val photo: String = "")\n')

with open('app/src/main/java/com/manacinema/app/database/models/Models.kt', 'w') as f:
    f.write(content)
