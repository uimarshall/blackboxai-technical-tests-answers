const loginForm = document.getElementById('login-form');
const loginButton = document.getElementById('login-form-submit');
const loginErrorMsg = document.getElementById('login-error-msg');

loginButton.addEventListener('click', (e) => {
  e.preventDefault();
  const email = loginForm.email.value;
  const password = loginForm.password.value;

  if (email === 'ben@gmail.com' && password === 'pass123') {
    alert('You have successfully logged in.');
    location.reload();
  } else {
    loginErrorMsg.style.opacity = 1;
  }
});
