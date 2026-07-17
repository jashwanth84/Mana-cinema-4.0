import re

with open('app/src/main/java/com/manacinema/app/MainActivity.kt', 'r') as f:
    ma_content = f.read()

ma_content = re.sub(r'androidx\.compose\.material\.icons\.Icons\.Default\.Close', '', ma_content)
ma_content = re.sub(r'androidx\.compose\.material3\.Icon\(androidx\.compose\.material\.icons\.Icons\.Default\.Warning.*?size\(64\.dp\)\)', '', ma_content)

with open('app/src/main/java/com/manacinema/app/MainActivity.kt', 'w') as f:
    f.write(ma_content)

with open('app/src/main/java/com/manacinema/app/repository/MovieRepository.kt', 'r') as f:
    repo_content = f.read()

repo_content = re.sub(r'com\.google\.gson\.Gson\(\)\.toJson\(it\.cast\)', '""', repo_content)
repo_content = re.sub(r'com\.google\.gson\.Gson\(\)\.toJson\(s\.cast\)', '""', repo_content)

with open('app/src/main/java/com/manacinema/app/repository/MovieRepository.kt', 'w') as f:
    f.write(repo_content)

with open('app/src/main/java/com/manacinema/app/ui/MainScreens.kt', 'r') as f:
    ms_content = f.read()

ms_content = ms_content.replace('FilterTabButton(\n                        label =', 'FilterTabButton(\n                        title =')
ms_content = ms_content.replace('label = cat', 'title = cat')

with open('app/src/main/java/com/manacinema/app/ui/MainScreens.kt', 'w') as f:
    f.write(ms_content)

with open('app/src/main/java/com/manacinema/app/ui/MovieViewModel.kt', 'r') as f:
    vm_content = f.read()

vm_content = re.sub(r'            repository\.getLiveTvChannelsFromFirebase\(\).*?_liveTvChannels\.value = it.*?\}', '', vm_content, flags=re.DOTALL)
vm_content = re.sub(r'    fun fetchLiveTvChannels\(\).*?\}', '', vm_content, flags=re.DOTALL)
vm_content = re.sub(r'            repository\.getLiveTvChannelsFromFirebase\(\).*?\}', '', vm_content, flags=re.DOTALL)


with open('app/src/main/java/com/manacinema/app/ui/MovieViewModel.kt', 'w') as f:
    f.write(vm_content)
