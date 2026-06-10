# Day 19 Concepts: JSON Data Files

JSON is a simple text format for storing structured data.
It is widely used in apps and APIs.

## 1) Why JSON is useful

JSON helps you save and share data like:
1. lists
2. dictionaries
3. configuration
4. API responses

## 2) Python object to JSON and back

Use json.dumps() to convert Python object to JSON string.
Use json.loads() to convert JSON string back to Python object.

Example:
json_text = json.dumps(data)
obj = json.loads(json_text)

## 3) Save JSON to file

Use:
json.dump(data, file)

Or simple path helper:
Path("file.json").write_text(json.dumps(data, indent=2))

## 4) Load JSON from file

Use:
json.load(file)

Or:
json.loads(Path("file.json").read_text())

## 5) Pretty printing

Use indent=2 or indent=4 to make JSON easier to read.

## 6) Common beginner mistakes

1. Trying to save Python set directly to JSON
2. Forgetting to read/write as text
3. Confusing dump with dumps
4. Assuming JSON file stays updated automatically

## 7) Practice checklist

After Day 19, you should be able to:
1. create JSON from Python list/dict
2. save JSON to file
3. load JSON back into Python
4. update structured data and resave it
5. work with simple app data files
