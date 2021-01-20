# Edit documentation site

To preview the documentation page run with docker:

=== "Unix"

    ```
    docker run --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material
    ```

=== "Windows"

    ```
    docker run --rm -it -v "%cd%":/docs squidfunk/mkdocs-material
    ```

Then point your browser to localhost:8000 to show the preview.