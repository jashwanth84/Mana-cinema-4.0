import re

with open('app/src/main/java/com/manacinema/app/repository/MovieRepository.kt', 'r') as f:
    content = f.read()

# Fix CachedSeriesEntity missing fields
replacement = """                genre = s.genre,
                storyline = s.storyline,
                castJson = com.google.gson.Gson().toJson(s.cast),
                isPremium = s.isPremium,
                isNew = s.isNew,
                qualityBadge = s.qualityBadge,
                episodesJson = arr.toString()"""
content = content.replace('                genre = s.genre,\n                storyline = s.storyline,\n                episodesJson = arr.toString()', replacement)

# Fix Gson error on line 289? No, it says unresolved reference: gson... Wait! 
content = content.replace('gson', 'com.google.gson.Gson()') # I don't know where it is, let's just let compiler tell me

# Also fix Conflicting declarations in getMoviesFromFirebase (val isPremium, etc.)
# I think I replaced storylines with series_parsing_additions in getMoviesFromFirebase by mistake because both had storyline!
with open('app/src/main/java/com/manacinema/app/repository/MovieRepository.kt', 'w') as f:
    f.write(content)
