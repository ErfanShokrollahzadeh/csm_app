# SelectCountry.vue

This Vue component is used to display a list of countries and allow the user to select one.

## Template

The template consists of several parts:

- Back Navigation: A link that navigates back to the signup page.
- Title: A title that says "Select your Country".
- Search Bar: An input field where the user can type to search for a country. The `v-model` directive is used to bind the input to the `searchText` data property.
- Country List: A list of countries. Each country is represented by a list item that includes an image and the country's name. The `v-for` directive is used to create a list item for each country in the `countries` data property.
- Next Button: A button that navigates to the next page when clicked. The `@click` directive is used to call the `goto` method when the button is clicked.

## Script

The script imports a JavaScript module named `SelectCountry` and uses its properties and methods in the Vue component. The `name` property of the component is set to "SelectCountry".

## Style

The styles for this component are scoped, meaning they only apply to this component. The styles are imported from a separate CSS file named `SelectCountry.css`.

## Usage

To use this component, import it into the parent component and include it in the parent component's template. When the `SelectCountry` component is rendered, it will display a list of countries and a search bar. The user can type into the search bar to filter the list of countries. When a country is clicked, the component will navigate to the next page.

## Dependencies

This component depends on Vue Router for navigation and the `SelectCountry` JavaScript module for its data and methods. Make sure Vue Router is properly installed and configured in your project, and that the `SelectCountry` module is correctly imported.
