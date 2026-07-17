import re

with open('app/src/main/java/com/manacinema/app/ui/MainScreens.kt', 'r') as f:
    content = f.read()

# Replace for movies
movie_badge_code = """                            AsyncImage(
                                model = movie.poster,
                                contentDescription = movie.title,
                                contentScale = ContentScale.Crop,
                                modifier = Modifier.fillMaxSize()
                            )
                            Column(modifier = Modifier.align(Alignment.TopEnd).padding(4.dp), verticalArrangement = Arrangement.spacedBy(4.dp), horizontalAlignment = Alignment.End) {
                                if (movie.isNew) {
                                    Box(modifier = Modifier.background(Color(0xFFE50914), RoundedCornerShape(4.dp)).padding(horizontal = 4.dp, vertical = 2.dp)) {
                                        Text("NEW", color = Color.White, fontSize = 8.sp, fontWeight = FontWeight.Bold)
                                    }
                                }
                                if (movie.qualityBadge.isNotEmpty()) {
                                    Box(modifier = Modifier.background(Color.Black.copy(alpha=0.7f), RoundedCornerShape(4.dp)).padding(horizontal = 4.dp, vertical = 2.dp)) {
                                        Text(movie.qualityBadge, color = Color.White, fontSize = 8.sp, fontWeight = FontWeight.Bold)
                                    }
                                }
                                if (movie.isPremium) {
                                    Box(modifier = Modifier.background(Color(0xFFFFB300), RoundedCornerShape(4.dp)).padding(horizontal = 4.dp, vertical = 2.dp)) {
                                        Text("PRO", color = Color.Black, fontSize = 8.sp, fontWeight = FontWeight.Bold)
                                    }
                                }
                            }"""

content = re.sub(r'                            AsyncImage\(\s*model = movie\.poster,\s*contentDescription = movie\.title,\s*contentScale = ContentScale\.Crop,\s*modifier = Modifier\.fillMaxSize\(\)\s*\)', movie_badge_code, content)

# Replace for series
series_badge_code = """                            AsyncImage(
                                model = series.poster,
                                contentDescription = series.title,
                                contentScale = ContentScale.Crop,
                                modifier = Modifier.fillMaxSize()
                            )
                            Column(modifier = Modifier.align(Alignment.TopEnd).padding(4.dp), verticalArrangement = Arrangement.spacedBy(4.dp), horizontalAlignment = Alignment.End) {
                                if (series.isNew) {
                                    Box(modifier = Modifier.background(Color(0xFFE50914), RoundedCornerShape(4.dp)).padding(horizontal = 4.dp, vertical = 2.dp)) {
                                        Text("NEW", color = Color.White, fontSize = 8.sp, fontWeight = FontWeight.Bold)
                                    }
                                }
                                if (series.qualityBadge.isNotEmpty()) {
                                    Box(modifier = Modifier.background(Color.Black.copy(alpha=0.7f), RoundedCornerShape(4.dp)).padding(horizontal = 4.dp, vertical = 2.dp)) {
                                        Text(series.qualityBadge, color = Color.White, fontSize = 8.sp, fontWeight = FontWeight.Bold)
                                    }
                                }
                                if (series.isPremium) {
                                    Box(modifier = Modifier.background(Color(0xFFFFB300), RoundedCornerShape(4.dp)).padding(horizontal = 4.dp, vertical = 2.dp)) {
                                        Text("PRO", color = Color.Black, fontSize = 8.sp, fontWeight = FontWeight.Bold)
                                    }
                                }
                            }"""

content = re.sub(r'                            AsyncImage\(\s*model = series\.poster,\s*contentDescription = series\.title,\s*contentScale = ContentScale\.Crop,\s*modifier = Modifier\.fillMaxSize\(\)\s*\)', series_badge_code, content)

with open('app/src/main/java/com/manacinema/app/ui/MainScreens.kt', 'w') as f:
    f.write(content)
