# Open file with outdated dependencies
with open("dependent.txt", "r") as depend:

    # If the file is empty, this means all dependencies are up to date
    if depend == "":
        print("## :heavy_check_mark: All dependencies up to date :heavy_check_mark:")

    # If the file is not empty, we make a table out of it's content
    else:

        # Header
        print(
            "## :small_red_triangle_down: Outdated Dependencies List :small_red_triangle_down:"
        )

        # Read file line-by-line
        for line in depend:
            listings = list(line.split())
            length = len(listings)

            # Read line word-by-word
            for i in range(length):

                # If it is the last word in the line, advance to next line after printing
                if i == length - 1:
                    print(listings[i])

                # All other words will be printed as is with a '|' to make a table
                else:
                    print(listings[i], end=" ")

        # Instructions outlining how to update outdated dependencies
        print("##")
        print("### Updating **SPECIFIC** Dependencies:")
        print(
            """- Ensure that, at least, the dependency that is being updated in the ***package.json*** file has a
    '***^***' in front of the version number (i.e. ***"@aws-sdk/client-dynamodb": "^3.351.0"***"""
        )
        print("- Go inside the folder with the ***package.json*** file from your CLI")
        print(
            "- Run one of the following command in your CLI to update the dependency to the latest version:"
        )
        print("  - ***npm update {DEPENDENCY_NAME}***")
        print("  - ***npm install {DEPENDENCY_NAME}@latest***")
        print(
            "- Run the following command in your CLI to update the dependency to a specific version:"
        )
        print("  - ***npm install {DEPENDENCY_NAME}@{VERSION}***")

        print(
            "### Updating **ALL** Dependencies **(not recommended, will update dependencies with major updates)**:"
        )
        print(
            """- Ensure that ALL dependencies in the ***package.json*** file has a
    '***^***' in front of the version number (i.e. ***"@aws-sdk/client-dynamodb": "^3.351.0"***"""
        )
        print("- Go inside the folder with the ***package.json*** file from your CLI")
        print("- Run the following command in your CLI to update all dependencies:")
        print("  - ***npm update***")
depend.close()

# Open file again for clean reading
with open("dependent.txt", "r") as depend:
    content = depend.read()

    # Print a line
    print("##")

    # Check for major updates
    if "Major" in content:
        print(
            "#### :warning: MAJOR DEPENDENCY UPDATE(S): Make sure to check the dependency docs before updating :warning:"
        )

    # Check for minor updates
    if "Minor" in content:
        print(
            "#### :x: MINOR DEPENDENCY UPDATE(S): Update these dependencies, otherwise the check will keep failing :x:"
        )
