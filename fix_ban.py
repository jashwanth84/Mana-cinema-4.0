import re

with open('app/src/main/java/com/manacinema/app/ui/MovieViewModel.kt', 'r') as f:
    content = f.read()

# Add _isBanned state
isbanned_state = """    private val _isBanned = MutableStateFlow(false)
    val isBanned: StateFlow<Boolean> = _isBanned

    private val _isGuestUser = MutableStateFlow(true)"""
content = content.replace('    private val _isGuestUser = MutableStateFlow(true)', isbanned_state)

ban_check_code = """                    createdAt = System.currentTimeMillis()
                )
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
                    })"""

content = content.replace('                    createdAt = System.currentTimeMillis()\n                )', ban_check_code)

with open('app/src/main/java/com/manacinema/app/ui/MovieViewModel.kt', 'w') as f:
    f.write(content)
