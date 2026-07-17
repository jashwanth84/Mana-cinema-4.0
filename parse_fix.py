import re

with open('app/src/main/java/com/manacinema/app/repository/MovieRepository.kt', 'r') as f:
    content = f.read()

movie_parsing = """                            val id = child.child("id").getValue(String::class.java) ?: child.key ?: ""
                            val title = child.child("title").getValue(String::class.java) ?: ""
                            val poster = child.child("poster").getValue(String::class.java) ?: ""
                            val backdrop = child.child("backdrop").getValue(String::class.java) ?: ""
                            val category = child.child("category").getValue(String::class.java) ?: ""
                            val rating = child.child("rating").getValue(String::class.java) ?: ""
                            val year = child.child("year").getValue(String::class.java) ?: ""
                            val genre = child.child("genre").getValue(String::class.java) ?: ""
                            val link = child.child("link").getValue(String::class.java) ?: ""
                            val director = child.child("director").getValue(String::class.java) ?: ""
                            val storyline = child.child("storyline").getValue(String::class.java) ?: ""
                            val isPremium = child.child("isPremium").getValue(Boolean::class.java) ?: false
                            val isNew = child.child("isNew").getValue(Boolean::class.java) ?: false
                            val qualityBadge = child.child("qualityBadge").getValue(String::class.java) ?: ""

                            val castList = mutableListOf<com.manacinema.app.models.CastMember>()
                            val castSnap = child.child("cast")
                            if (castSnap.exists()) {
                                for (c in castSnap.children) {
                                    try {
                                        val cName = c.child("name").getValue(String::class.java) ?: ""
                                        val cPhoto = c.child("photo").getValue(String::class.java) ?: ""
                                        castList.add(com.manacinema.app.models.CastMember(cName, cPhoto))
                                    } catch (e: Exception) {}
                                }
                            }

                            val finalMovie = com.manacinema.app.models.Movie(
                                id = id, title = title, poster = poster, backdrop = backdrop,
                                category = category, rating = rating, year = year, genre = genre,
                                link = link, director = director, storyline = storyline,
                                isPremium = isPremium, isNew = isNew, qualityBadge = qualityBadge,
                                cast = castList
                            )
                            list.add(finalMovie)"""

content = re.sub(r'val movie = child.getValue\(Movie::class.java\).*?list\.add\(finalMovie\)\s*\}', movie_parsing, content, flags=re.DOTALL)


series_parsing_additions = """                            val isPremium = child.child("isPremium").getValue(Boolean::class.java) ?: false
                            val isNew = child.child("isNew").getValue(Boolean::class.java) ?: false
                            val qualityBadge = child.child("qualityBadge").getValue(String::class.java) ?: ""

                            val castList = mutableListOf<com.manacinema.app.models.CastMember>()
                            val castSnap = child.child("cast")
                            if (castSnap.exists()) {
                                for (c in castSnap.children) {
                                    try {
                                        val cName = c.child("name").getValue(String::class.java) ?: ""
                                        val cPhoto = c.child("photo").getValue(String::class.java) ?: ""
                                        castList.add(com.manacinema.app.models.CastMember(cName, cPhoto))
                                    } catch (e: Exception) {}
                                }
                            }"""

content = content.replace('val storyline = child.child("storyline").getValue(String::class.java) ?: ""', 'val storyline = child.child("storyline").getValue(String::class.java) ?: ""\n' + series_parsing_additions)

content = content.replace('storyline = storyline,\n                                episodes = episodes', 'storyline = storyline,\n                                isPremium = isPremium,\n                                isNew = isNew,\n                                qualityBadge = qualityBadge,\n                                cast = castList,\n                                episodes = episodes')

# Also need to update cache mapping!
content = content.replace('stars = it.stars,', 'castJson = com.google.gson.Gson().toJson(it.cast),\n                        isPremium = it.isPremium,\n                        isNew = it.isNew,\n                        qualityBadge = it.qualityBadge,')
content = content.replace('stars = "", // Not stored in cache yet', 'castJson = "", isPremium = false, isNew = false, qualityBadge = "",')
content = content.replace('stars = entity.stars,', 'cast = com.google.gson.Gson().fromJson(entity.castJson, Array<com.manacinema.app.models.CastMember>::class.java).toList(),\n                    isPremium = entity.isPremium,\n                    isNew = entity.isNew,\n                    qualityBadge = entity.qualityBadge,')
content = content.replace('episodesJson = com.google.gson.Gson().toJson(it.episodes)', 'castJson = com.google.gson.Gson().toJson(it.cast),\n                        isPremium = it.isPremium,\n                        isNew = it.isNew,\n                        qualityBadge = it.qualityBadge,\n                        episodesJson = com.google.gson.Gson().toJson(it.episodes)')
content = content.replace('episodes = com.google.gson.Gson().fromJson(entity.episodesJson, Array<com.manacinema.app.models.Episode>::class.java).toList()', 'cast = try { com.google.gson.Gson().fromJson(entity.castJson, Array<com.manacinema.app.models.CastMember>::class.java).toList() } catch(e:Exception) { emptyList() },\n                    isPremium = entity.isPremium,\n                    isNew = entity.isNew,\n                    qualityBadge = entity.qualityBadge,\n                    episodes = try { com.google.gson.Gson().fromJson(entity.episodesJson, Array<com.manacinema.app.models.Episode>::class.java).toList() } catch(e:Exception) { emptyList() }')


with open('app/src/main/java/com/manacinema/app/repository/MovieRepository.kt', 'w') as f:
    f.write(content)
