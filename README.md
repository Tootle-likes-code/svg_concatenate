# svg_concatenate
A program to add many svg's into a single file given a list of file names and a directory to trawl through.

# Using svg_concatenate

svg_concatenate works using a series of filters and a given location to find the files described by those filters to
then concatenate the `svg` contents in those files into a single file.  Reporting on missing files, and saving the
report and the merged `svg` into a user defined output folder.

## Adding Filters

Upon clicking the `Add Search Filter` button, a new window will open called `New Filter`, with a dropdown box and an
area to update your filters.  Initially this will start with a File Type filter, but the other available filters are in
the dropdown.  Select the filter you want to use and look at the following section that explains that Filter.

The `Enter` and `Return` keys are set up to be shortcuts for the Create button.

### Filters
Filters are important for the working of svg_concatenate.  They act as a white-list for files, meaning that if a file
doesn't match the file is rejected.

The filters are essentially, defining what files you want processed by svg_concatenate.

### File Type Filter

A file type filter will limit the files that svg_concatenate will look at.  By default, this will include `.svg`,
but the ability to look at other File Types is provided.  

> Warning, other files that are not `svg` files under the hood are likely to cause an error and prevent svg_concatenate
> from completing its task.

To create/update a File Type filter, you enter the file suffixes you want to filter from the file into the text field.
Each file type should be seperated by a `,`.  Spaces will be trimmed off of each File Type.

There can only ever be one File Type filter at a time, so attempts to add a new File Type filter updates the existing
File Type filter instead.

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

To create a Names Filter, you need to add a value in the `New Name` text box.  When you are happy with it, click `Add`.
It will add it to the list above.  Only values in that list box will be used.

To remove an entry from the list box, select the entries to delete and click the remove button.  Alternatively you can just press Delete or
Backspace to remove selected entries.

There can only ever be one Name filter at a time, so attempts to add another updates the current Name filter instead.

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

#### Enter Override
If the cursor is in the `New Name` text box, then the `Return` key will instead, count as clicking the `Add` 
Button instead. The `Enter` key retains the Create Shortcut, however.

### Inverse Filter
Inverse Filters work on another Filter, converting it to a black list.  For example, if I have an Inverse Filter based
on a File Type filter on `txt` files then instead of reading `txt` files like a File Type filter normally would, it
rejects `txt` files and allows all others.

To create a new Inverse Filter you need to select another Filter Type in the `Select Inverted Filter` box. The selection
will bring up a form for the selected filter.  Fill out the form as normal for that kind of filter.  See those sections
for details.

When ready, click the `Create` button as normal.

> #### In Short
> This filter asks you to make another filter and then just flips the result of the check.  When using it, just think
> 'Filter this if it's NOT ___'