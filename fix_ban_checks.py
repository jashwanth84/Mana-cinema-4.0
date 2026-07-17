import re

with open('app/src/main/java/com/manacinema/app/ui/MovieViewModel.kt', 'r') as f:
    content = f.read()

# Replace all the injected ban checks with just the one for valid user.
# But since I already injected it, I'll just replace the broken `user.uid` with `user?.uid` or remove it.
# Actually, I can just replace `users/${user.uid}/isBanned` with `users/${user?.uid ?: "guest"}/isBanned` to make it compile, but it's pointless for guest.
# Let's remove the ones for guest.
content = re.sub(r'                com\.google\.firebase\.database\.FirebaseDatabase\.getInstance\(\)\.getReference\("users/\$\{user\.uid\}/isBanned"\)\n                    \.addValueEventListener\(object : com\.google\.firebase\.database\.ValueEventListener \{\n                        override fun onDataChange.*?\}\)\n', '', content, flags=re.DOTALL)

# And put one back properly.
proper_ban_check = """                if (user != null) {
                    com.google.firebase.database.FirebaseDatabase.getInstance().getReference("users/${user.uid}/isBanned")
                        .addValueEventListener(object : com.google.firebase.database.ValueEventListener {
                            override fun onDataChange(snapshot: com.google.firebase.database.DataSnapshot) {
                                val banned = snapshot.getValue(Boolean::class.java) ?: false
                                _isBanned.value = banned
                                if (banned) {
                                    com.google.firebase.auth.FirebaseAuth.getInstance().signOut()
                                    _currentUserProfile.value = null
                                }
                            }
                            override fun onCancelled(error: com.google.firebase.database.DatabaseError) {}
                        })
                }"""

# Insert it at the end of `observeUserSession` try block
content = content.replace('            loadProfiles()', proper_ban_check + '\n            loadProfiles()')

with open('app/src/main/java/com/manacinema/app/ui/MovieViewModel.kt', 'w') as f:
    f.write(content)
