<template>
  <form @submit.prevent="handleLogin" class="login-form">
    <input v-model="username" placeholder="Username" required />
    <input v-model="password" type="password" placeholder="Password" required />
    <button type="submit">Login</button>
    <p v-if="error" class="error">{{ error }}</p>
  </form>
</template>

<script>
import { login } from '../services/api';

export default {
  data() {
    return {
      username: '',
      password: '',
      error: null,
    };
  },
  methods: {
    async handleLogin() {
      this.error = null;
      try {
        const data = await login(this.username, this.password);
        localStorage.setItem('authToken', data.token);
        alert('Login successful!');
        this.$router.push({ name: 'accounts' });
      } catch (err) {
        this.error = err.message;
      }
    },
  },
};
</script>

<style>
.login-form { max-width: 300px; margin: auto; }
.error { color: red; }
</style>
