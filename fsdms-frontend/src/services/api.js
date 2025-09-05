const API_BASE_URL = 'http://localhost:8000';

async function request(endpoint, options = {}) {
  const token = localStorage.getItem('authToken');
  const headers = {
    'Content-Type': 'application/json',
    ...(token ? { Authorization: `Token ${token}` } : {})
  };

  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    headers,
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'API request failed');
  }
  if (response.status === 204) return null; // No Content
  return response.json();
}

export function login(username, password) {
  return request('/login/', {
    method: 'POST',
    body: JSON.stringify({ username, password }),
  });
}

export function register(userData) {
  return request('/register/', {
    method: 'POST',
    body: JSON.stringify(userData),
  });
}

export function getAccounts() {
  return request('/accounts/');
}

export function getAccount(id) {
  return request(`/accounts/${id}/`);
}

export function createAccount(accountData) {
  return request('/accounts/', {
    method: 'POST',
    body: JSON.stringify(accountData),
  });
}

export function updateAccount(id, data) {
  return request(`/accounts/${id}/`, {
    method: 'PUT',
    body: JSON.stringify(data),
  });
}

export function deleteAccount(id) {
  return request(`/accounts/${id}/`, {
    method: 'DELETE',
  });
}
