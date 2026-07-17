import re

with open('app/src/main/java/com/manacinema/app/MainActivity.kt', 'r') as f:
    content = f.read()

replacement = """                        val isBanned by viewModel.isBanned.collectAsState()
                        if (isBanned) {
                            androidx.compose.foundation.layout.Box(modifier = androidx.compose.ui.Modifier.fillMaxSize().background(Color.Black), contentAlignment = androidx.compose.ui.Alignment.Center) {
                                androidx.compose.foundation.layout.Column(horizontalAlignment = androidx.compose.ui.Alignment.CenterHorizontally) {
                                    androidx.compose.material.icons.Icons.Default.Block
                                    androidx.compose.material3.Icon(androidx.compose.material.icons.Icons.Default.Warning, contentDescription = null, tint = Color.Red, modifier = androidx.compose.ui.Modifier.size(64.dp))
                                    androidx.compose.foundation.layout.Spacer(modifier = androidx.compose.ui.Modifier.height(16.dp))
                                    androidx.compose.material3.Text("Your account has been suspended", color = Color.White, fontSize = 20.sp, fontWeight = androidx.compose.ui.text.font.FontWeight.Bold)
                                }
                            }
                        } else if (isAuthenticated || isGuestUser) {"""

content = content.replace('                        if (isAuthenticated || isGuestUser) {', replacement)

with open('app/src/main/java/com/manacinema/app/MainActivity.kt', 'w') as f:
    f.write(content)
