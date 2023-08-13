import { defineStore } from 'pinia'

//? This function is from Pinia! Check the documentation of how it works
export const useUserStore = defineStore({
  id: 'user',
  state: () => ({
    user: {
      isAuthenticated: false,
      email: null,
      token: null
    }
  }),

  actions: {
    initStore() {
      this.user.isAuthenticated = false

      if (localStorage.getItem('user.token')) {
        this.user.token = localStorage.getItem('user.token')
        this.user.email = localStorage.getItem('user.email')
        this.user.isAuthenticated = true;

        console.log('Initialized user: ', this.user)
      }
    },
    setToken(token, email) {
      console.log('setToken: ', token, email)
      this.user.token = token
      this.user.email = email
      this.user.isAuthenticated = true

      // Now we need to save this information in localStorage
      localStorage.setItem('user.token', token)
      localStorage.setItem('user.email', email)
    },
    removeToken() {
      console.log('removeToken: ')
      this.user.token = null
      this.user.email = null
      this.user.isAuthenticated = null

      localStorage.setItem('user.token', null)
      localStorage.setItem('user.email', null)
    }
  }
})