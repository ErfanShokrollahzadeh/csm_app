# ForgotPass2.vue

This Vue.js component is used for the "Forgot Password" functionality. It includes a form where the user can enter a One-Time Password (OTP) received via SMS.

## Data Properties

- `input1`, `input2`, `input3`, `input4`: These are bound to the input fields where the user enters the OTP. Each can contain a single digit.
- `error`: This is a boolean that becomes `true` if the entered OTP is invalid.
- `otp`: This is the correct OTP. In a real application, it should be sent via SMS and stored securely, not hardcoded.

## Methods

- `limitInput`: This method is called when the user types in an input field. It limits the input to a single digit.
- `checkCode`: This method is called when the form is submitted. It concatenates the values of the input fields and compares the result to `otp`. If they don't match, it sets `error` to `true`.
- `goToVerification`: This method is called when the "Verify" button is clicked. It calls `checkCode` to check the OTP. If `error` is `false` (meaning the OTP is valid), it navigates to the verification page.

## Styling

- `.error-input`: This class is added to an input field if `error` is `true`. It styles the input field with a red border and red background.
- `.error-text`: This class styles the error message with red text.

## Usage

To use this component, the user should enter the OTP received via SMS into the input fields and click the "Verify" button. If the entered OTP is invalid, an error message will be displayed, and the input fields will be highlighted in red.
