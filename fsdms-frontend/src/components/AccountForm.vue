<template>
  <form @submit.prevent="handleSubmit" class="account-form">
    <div>
      <label>Account Number:</label>
      <input v-model="account_number" required />
    </div>
    <div>
      <label>Account Name:</label>
      <input v-model="account_name" required />
    </div>
    <div>
      <label>Account Type:</label>
      <select v-model="account_type" required>
        <option value="Savings">Savings</option>
        <option value="Checking">Checking</option>
      </select>
    </div>
    <div>
      <label>Balance:</label>
      <input v-model="balance" type="number" step="0.01" required />
    </div>
    <button type="submit" :disabled="loading">Create Account</button>
    <p v-if="error" style="color:red">{{ error }}</p>
    <p v-if="success" style="color:green">Account created successfully!</p>
  </form>
</template>

<script>
import { createAccount } from '../services/api';

export default {
  data() {
    return {
      account_number: '',
      account_name: '',
      account_type: 'Savings',
      balance: '',
      loading: false,
      error: null,
      success: false,
    };
  },
  methods: {
    async handleSubmit() {
      this.error = null;
      this.success = false;
      this.loading = true;

      try {
        const userId = 1; // Replace with actual user ID retrieval logic
        const payload = {
          account_number: this.account_number,
          account_name: this.account_name,
          account_type: this.account_type,
          balance: this.balance,
          user: userId,
        };
        await createAccount(payload);
        this.success = true;
        this.account_number = '';
        this.account_name = '';
        this.balance = '';
        this.$router.push({ name: 'accounts' });
      } catch (err) {
        this.error = err.message || 'Failed to create account';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style>
.account-form div {
  margin-bottom: 8px;
}
</style>
