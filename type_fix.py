import re

with open('app/src/main/java/com/manacinema/app/ui/MovieViewModel.kt', 'r') as f:
    vm_content = f.read()

# Fix combine lambda types
vm_content = re.sub(r'combine\(movies, _activeProfile\) \{ movieList, profile ->', r'combine(movies, _activeProfile) { movieList: List<com.manacinema.app.models.Movie>, profile: com.manacinema.app.models.MovieProfile? ->', vm_content)
vm_content = re.sub(r'combine\(webSeries, _activeProfile\) \{ seriesList, profile ->', r'combine(webSeries, _activeProfile) { seriesList: List<com.manacinema.app.models.WebSeries>, profile: com.manacinema.app.models.MovieProfile? ->', vm_content)

with open('app/src/main/java/com/manacinema/app/ui/MovieViewModel.kt', 'w') as f:
    f.write(vm_content)
