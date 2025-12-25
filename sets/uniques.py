def analyze_article_tags(tag_lists):
    if tag_lists == []:
        return {
            "unique": set(),
            "common": set(),
            "exclusive": set(),
        }

    if tag_lists and isinstance(tag_lists[0], str):
        tag_lists = [tag_lists]

    uniques = set(tag_lists[0])
    commons = set(tag_lists[0])
    exc_list = count_tags(tag_lists)

    for i in range(1, len(tag_lists)):
        uniques = uniques.union(tag_lists[i])
        commons = commons.intersection(tag_lists[i])

    return {
        "unique": uniques, "common": commons, "exclusive": exc_list,
    }


def count_tags(tag_lists):
    if tag_lists and isinstance(tag_lists[0], str):
        tag_lists = [tag_lists]

    tags_lists = {}
    for i, tag_list in enumerate(tag_lists):
        for tag in tag_list:
            if tag not in tag_lists:
                tags_lists[tag] = set()
            tags_lists[tag].add(i)

    exclusive_tags = {
        tag for tag, list_indices in tags_lists.items() if len(list_indices) == 1}
    return exclusive_tags


tags = [
    ["python", "sets", "tutorial"],
    ["python", "dictionaries", "tutorial"],
    ["python", "sets", "advanced"],
]

print(analyze_article_tags(tags))
print(analyze_article_tags(["python", "python", "sets", "guide", "guide"]))
