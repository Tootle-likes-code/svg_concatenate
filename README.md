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
> from completing it's task.

To create/update a File Type filter, you enter the file suffixes you want to filter from the file into the text field.
Each file type should be seperated by a `,`.  Spaces will be trimmed off of each File Type.