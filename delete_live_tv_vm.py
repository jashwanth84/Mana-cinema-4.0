import re

with open('app/src/main/java/com/manacinema/app/ui/MovieViewModel.kt', 'r') as f:
    content = f.read()

content = re.sub(r'    private val _liveTvChannels.*?val liveTvChannels: StateFlow<List<com.manacinema.app.models.LiveTvChannel>> = _liveTvChannels\n', '', content, flags=re.DOTALL)
content = re.sub(r'    private val _isLiveTvLoading.*?val isLiveTvLoading: StateFlow<Boolean> = _isLiveTvLoading\n', '', content, flags=re.DOTALL)
content = re.sub(r'    fun fetchLiveTvChannels\(\).*?_isLiveTvLoading.value = false\n        }\n    }\n', '', content, flags=re.DOTALL)

with open('app/src/main/java/com/manacinema/app/ui/MovieViewModel.kt', 'w') as f:
    f.write(content)
