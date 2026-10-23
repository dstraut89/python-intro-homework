# Creating two hard coded lists of programming languages (some overlap, some unique to each list). Conver each to a set and print.
FstackWeb = {"HTML", "CSS", "JavaScript", "TypeScript", "Python", "SQL", "PHP", "Java", "Ruby", "C#", "Rust"}
Software = {"Python", "Java", "C", "C++", "C#", "JavaScript", "Rust", "Ruby", "PHP", "Zig", "TypeScript"}

# The Union (All languages from both lists, no duplicates)
print(FstackWeb.union(Software))
# The Intersection (Languages in both lists)
print(FstackWeb.intersection(Software))
# The difference ( Languages on in the first list)
print(FstackWeb.difference(Software))