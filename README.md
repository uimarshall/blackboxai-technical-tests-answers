# blackboxai-technical-tests-answers

This repository is for answers to the basic questions for Microverse Developer Agency for blackbox.io project.

# 1. SIMPLE LOGIN PAGE

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Simple Login Page</title>
    <link rel="stylesheet" href="css/styles.css" />
  </head>
  <body>
    <section class="container">
      <div id="login-error-msg-holder">
        <p id="login-error-msg">
          Invalid username
          <span id="error-msg-second-line">and/or password</span>
        </p>
      </div>
      <form id="login-form" class="login-form" action="#">
        <header class="form-header">
          <h3>Login Form</h3>
        </header>
        <!--Email Input-->
        <div class="field email-field">
          <div class="form-group input-field">
            <input
              name="email"
              type="email"
              class="form-input email"
              placeholder="Enter your email"
            />
          </div>
        </div>
        <!--Password Input-->
        <div class="create-password">
          <div class="form-group input-field">
            <input
              name="password"
              type="password"
              class="form-input password"
              placeholder="password"
            />
          </div>
        </div>
        <!--Login Button-->
        <div class="form-group">
          <input
            id="login-form-submit"
            class="form-button"
            type="submit"
            value="Login"
          />
        </div>
        <div class="form-footer">
          Don't have an account? <a href="#">Sign Up</a>
        </div>
      </form>
    </section>

    <!-- JavaScript -->
    <script src="js/script.js"></script>
  </body>
</html>
```

> ![screenshot](login.png)
