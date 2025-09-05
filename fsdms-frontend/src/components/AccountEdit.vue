<template>
  <form @submit.prevent="handleUpdate" class="account-form" v-if="account">
    <div>
      <label>Account Number:</label>
      <input v-model="account.account_number" required disabled />
    </div>
    <div>
      <label>Account Name:</label>
      <input v-model="account.account_name" required />
    </div>
    <div>
      <label>Account Type:</label>
      <select v-model="account.account_type" required>
        <option value="Savings">Savings</option>
        <option value="Checking">Checking</option>
      </select>
    </div>
    <div>
      <label>Balance:</label>
      <input v-model="account.balance" type="number" step="0.01" required />
    </div>
    <button type="submit" :disabled="loading">Update Account</button>
    <p v-if="error" style="color:red">{{ error }}</p>
    <p v-if="success" style="color:green">Account updated successfully!</p>
  </form>
  <div v-else>
    Loading account...
  </div>
</template>

<script>
import { getAccount, updateAccount } from '../services/api';

export default {
  data() {
    return {
      account: null,
      loading: false,
      error: null,
      success: false,
    };
  },
  methods: {
    async fetchAccount() {
      this.error = null;
      try {
        this.account = await getAccount(this.$route.params.id);
      } catch (err) {
        this.error = err.message || 'Failed to load account';
      }
    },
    async handleUpdate() {
      this.loading = true;
      this.error = null;
      this.success = false;
      try {
        await updateAccount(this.$route.params.id, this.account);
        this.success = true;
        this.$router.push({ name: 'accounts' });
      } catch (err) {
        this.error = err.message || 'Failed to update account';
      } finally {
        this.loading = false;
      }
    }
  },
  mounted() {
    this.fetchAccount();
  }
};
</script>

<style>
.account-form div {
  margin-bottom: 8px;
}
</style>
