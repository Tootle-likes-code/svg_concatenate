# svg_concatenate
A program to add many svg's into a single file given a list of file names and a directory to trawl through.

# Using svg_concatenate

## Adding Filters

Upon clicking the `Add Search Filter` button, a new window will open called `New Filter`, with a dropdown box and an
area to update your filters.  Initially this will start with a File Type filter, but the other available filters are in
the dropdown.  Select the filter you want to use and look at the following section that explains that Filter.

### File Type Filter

A file type filter will limit the files that svg_concatenate will look at.  By default, this will include `.svg`,
but the ability to look at other File Types is provided.  

> Warning, other files that are not `svg` files under the hood are likely to cause an error and prevent svg_concatenate
> from completing its task.

To create/update a File Type filter, you enter the file suffixes you want to filter from the file into the text field.
Each file type should be seperated by a `,`.  Spaces will be trimmed off of each File Type.

#### Pasting
Pasting will convert a list of text into a list separated by commas for you.  I.e.

```
.svg
.xml
.img
.mp4
```

Becomes `.svg, .xml, .img, .mp4`.

### Names Filter

When processing, this filter will look for files with the names given when doing the search.

> #### For Example
> You have 4 files `abc.svg, def.svg, ghi.svg, jkl.svg` and you create a Names filter for `abc, xyz`, when searching,
> svg_concatenate will only find `abc.svg`.

To create a Names Filter, you need to add a value in the `New Name` text box.  When you are happy with it, click Add.
It will add it to the list above.  Only values in that list box will be used.

To remove an entry from the list box, select the entries to delete and click the remove button.  Alternatively you can just press Delete or
Backspace to remove selected entries.

> #### Pasting
> When pasting with this option selected, behaviour depends on what contains focus.  Essentially, if nothing or the list
> have focus, then a pasted list of names (each name being on it's own line) will be entered into the list box.
> 
> If you paste whilst the text box is selected, the text will be pasted there as normal, essentially, putting your
> content into wherever it is selected.

For example:

If you paste the below with nothing selected or the list selected, the list will show the same as below.
```
apple
banana
orange
grape
pear
cherry
peach
mango
kiwi
plum
```

However, if you paste the above into the New Name text box, you will get 
`applebananaorangegrapepearcherrypeachmangokiwiplum`.

> **Important Note:** If you have the cursor in the new name text box, and you paste and the values are appearing there
> and you want to paste a list of data, you need to click on the list box first, and try again.
