## Structure

- `source.py`: contains functions to acquire financial data. Each function must output a dataset.

- `transform.py`: contains functions to transform datasets. Each function must have as both input and output a dataset.

- `display.py`: contains functions to display datasets. They're transforms with side effects.

- `compose.py` contains primitives to build pipelines.

### Compose
`Compose` is a class to build a list transform by chaining them through the calling of `then`. It's itself a `Transform`.

### ForkLeft
`ForkLeft` is a class that takes two transforms as constructor parameters and is itself a `Transform`.

Its `apply` method does so:

    - first it calls the second parameter `apply`, discarding its output. It's useful if it's a `Display` or a `Compose` chaining one or more `Display` among other transforms;
    - then it calls the first parameter `apply`, returning its result.
