from string import Template

templ = Template("abc ${placeholder1} def ${placeholder2}")

print(templ.substitute({
    "placeholder1": "123",
    "placeholder2": "456"
}))
