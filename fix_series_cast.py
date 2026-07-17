import re

with open('app/src/main/java/com/manacinema/app/ui/MainScreens.kt', 'r') as f:
    content = f.read()

replacement = """                Spacer(modifier = Modifier.height(24.dp))
                if (series.cast.isNotEmpty()) {
                    Text("CAST", color = Color.Gray, fontSize = 12.sp, fontWeight = FontWeight.Bold)
                    Spacer(modifier = Modifier.height(12.dp))
                    androidx.compose.foundation.lazy.LazyRow(horizontalArrangement = Arrangement.spacedBy(16.dp)) {
                        items(series.cast) { actor ->
                            Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier.width(80.dp)) {
                                androidx.compose.foundation.Image(
                                    painter = coil.compose.rememberAsyncImagePainter(actor.photo),
                                    contentDescription = actor.name,
                                    modifier = Modifier.size(60.dp).clip(androidx.compose.foundation.shape.CircleShape).background(Color.DarkGray),
                                    contentScale = androidx.compose.ui.layout.ContentScale.Crop
                                )
                                Spacer(modifier = Modifier.height(4.dp))
                                Text(actor.name, color = Color.LightGray, fontSize = 11.sp, textAlign = androidx.compose.ui.text.style.TextAlign.Center, maxLines = 2, overflow = androidx.compose.ui.text.style.TextOverflow.Ellipsis)
                            }
                        }
                    }
                    Spacer(modifier = Modifier.height(24.dp))
                }
                Text("EPISODES LISTING","""

content = content.replace('Spacer(modifier = Modifier.height(24.dp))\n                Text("EPISODES LISTING",', replacement)

with open('app/src/main/java/com/manacinema/app/ui/MainScreens.kt', 'w') as f:
    f.write(content)
