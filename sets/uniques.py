def analyze_article_tags(tag_lists):
    uniques = set(tag_lists[0])

    for i in range(1, len(tag_lists)):
        uniques += uniques.union(tag_lists[i])

    return uniques

tags= [
    ["python", "sets", "tutorial"],
    ["python", "dictionaries", "tutorial"],
    ["python", "sets", "advanced"],
]

print(analyze_article_tags(tags))
