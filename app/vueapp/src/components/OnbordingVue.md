# OnbordingVue.vue

`OnbordingVue.vue` is a Vue.js component designed to manage and display onboarding information.

## Structure

The component is structured into three main sections:

1. **Template**: This section contains the HTML structure of the component. It includes a loop that iterates over the `Onbording` array and displays each item. It also includes "Next" and "Back" buttons for navigation.

2. **Script**: This section contains the Vue.js code that powers the component. It includes:

   - `data`: This function returns the initial state of the component. It includes `Onbording` (an array for the onboarding items) and `currentSlide` (a number for tracking the current slide).

   - `computed`: This object contains computed properties for the component. It includes `nextButtonText`, which returns "Next" or "Get Started" based on the current slide.

   - `created`: This lifecycle hook is used to fetch the onboarding data from the API when the component is created.

   - `methods`: This object contains methods for the component. It includes `next`, which increments `currentSlide` if it's less than the total number of onboarding items minus one, and `back`, which decrements `currentSlide` if it's greater than zero.

3. **Style**: This section contains the CSS styles for the component. It uses the `scoped` attribute to limit the styles to this component only.

## Usage

To use this component, you can import it in another Vue.js component or in your main Vue.js instance and include it in your template. You'll also need to ensure that the API endpoint is correctly set up to return the onboarding data.

```javascript
import OnbordingVue from "./OnbordingVue.vue";

new Vue({
  el: "#app",
  components: {
    "onbording-vue": OnbordingVue,
  },
});
```
