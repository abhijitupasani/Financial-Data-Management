<template>
  <div>
    <h2>Your Accounts</h2>
    <router-link to="/accounts/new">Create New Account</router-link>
    <button @click="fetchAccounts">Refresh</button>
    <div v-if="loading">Loading accounts...</div>
    <div v-if="error" style="color:red;">{{ error }}</div>
    <ul v-if="accounts.length">
      <li v-for="account in accounts" :key="account.id">
        {{ account.account_name }} ({{ account.account_number }}) — Balance: {{ account.balance }}
        <router-link :to="{ name: 'account-edit', params: { id: account.id } }">Edit</router-link>
        <button @click="deleteAccountById(account.id)">Delete</button>
      </li>
    </ul>
    <div v-else>No accounts found.</div>
  </div>
</template>

<script>
import { getAccounts, deleteAccount } from '../services/api';

export default {
  data() {
    return {
      accounts: [],
      loading: false,
      error: null,
    };
  },
  methods: {
    async fetchAccounts() {
      this.loading = true;
      this.error = null;
      try {
        const data = await getAccounts();
        this.accounts = data.results || data;
      } catch (err) {
        this.error = err.message || 'Failed to fetch accounts.';
      } finally {
        this.loading = false;
      }
    },
    async deleteAccountById(id) {
      if (!confirm('Are you sure you want to delete this account?')) return;
      try {
        await deleteAccount(id);
        this.fetchAccounts();
      } catch (err) {
        alert(err.message || 'Failed to delete account.');
      }
    },
  },
  mounted() {
    this.fetchAccounts();
  },
};
</script>
