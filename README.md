# Kenneys Prototype Textures - Custom edition
This is a modified version of the [Prototype Textures](https://www.kenney.nl/assets/prototype-textures) by [Kenney](http://www.kenney.nl/). It includes the svg files to generate the textures using a [script](render.py).

## How to use the render script
Run the script with `python render.py`. You can change the values in the `CONFIGURATION` section to add custom colors or use Kenneys original palette and to change the output path.

If you want to use custom colors you need to set the `custom_color` variable to `True`. You can define custom colors between the two square brackets like this:

```python
custom_colors = [
    Color("name", "hex"),
    Color("red", "#ff0000")
]
```

As you can see you first need to set a name that will be used for the output folder and the color in hex format. All color definitions are separated by a comma.

## License
The original work is distributed under CC0 and so my version is CC0 too. See [LICENSE](LICENSE) for more information.
