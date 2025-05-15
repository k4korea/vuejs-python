<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <div class="buttons">
      <button @click="fetchHello" :disabled="loading">
        {{ loading ? 'Loading...' : 'Get Hello Message' }}
      </button>
      <button @click="fetchTest" :disabled="loading">
        {{ loading ? 'Loading...' : 'Test Connection' }}
      </button>
    </div>
    <div v-if="error" class="error-message">
      {{ error }}
    </div>
    <div v-if="clientInfo" class="client-info">
      <h3>Client Information:</h3>
      <pre>{{ JSON.stringify(clientInfo, null, 2) }}</pre>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      message: 'Welcome to Vue.js!',
      loading: false,
      error: null,
      clientInfo: null
    }
  },
  methods: {
    async fetchHello() {
      this.loading = true
      this.error = null
      this.clientInfo = null
      try {
        const response = await axios.get('http://192.168.0.10:5000/api/hello')
        this.message = response.data.message
        this.clientInfo = response.data.client_info
        alert(`API Response: ${JSON.stringify(response.data, null, 2)}`)
      } catch (error) {
        console.error('Error fetching hello message:', error)
        this.error = 'Failed to fetch hello message'
        this.message = 'Error occurred'
        alert('Error: Failed to fetch hello message')
      } finally {
        this.loading = false
      }
    },
    async fetchTest() {
      this.loading = true
      this.error = null
      this.clientInfo = null
      try {
        const response = await axios.get('http://192.168.0.10:5000/api/test')
        this.message = response.data.message
        this.clientInfo = response.data.client_info
        alert(`API Response: ${JSON.stringify(response.data, null, 2)}`)
      } catch (error) {
        console.error('Error testing connection:', error)
        this.error = 'Failed to test connection'
        this.message = 'Error occurred'
        alert('Error: Failed to test connection')
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.buttons {
  margin-top: 20px;
}

button {
  background-color: #42b983;
  color: white;
  border: none;
  padding: 10px 20px;
  margin: 0 10px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

button:hover:not(:disabled) {
  background-color: #3aa876;
}

button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.error-message {
  color: #dc3545;
  margin-top: 20px;
  padding: 10px;
  border-radius: 4px;
  background-color: #f8d7da;
  border: 1px solid #f5c6cb;
}

.client-info {
  margin-top: 20px;
  padding: 20px;
  background-color: #f8f9fa;
  border-radius: 4px;
  text-align: left;
}

.client-info pre {
  background-color: #fff;
  padding: 10px;
  border-radius: 4px;
  border: 1px solid #dee2e6;
  overflow-x: auto;
}
</style> 