## Structure

- `source.py`: contains functions to acquire financial data. Each function must output a dataset.

- `transform.py`: contains functions to transform datasets. Each function must have as both input and output
    - a dataset
    - an object containing information about transform domain and codomain (i.e. which columns it accepts and which it outputs).

- `display.py`: contains functions to display datasets. They're of the form `DataFrame -> void`.

Then it's easy to write pipelines such:

```
[ pipeline(source, transform1, transform2, [transform3, display1], transfrom4, display2]
```

Better classes and not functions so that they can statically check for input/outputs ?
