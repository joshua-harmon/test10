<!-- Here we do something similar to when Sign Up, but we also need to
     save the Token returned from the server in session -->
<script setup>
import {useUserStore} from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()

let email = ref('')
let password = ref('')
let errors = ref([])

// We do something similar as with Sign Up but calling a different url
async function submitForm() {
    console.log('submitForm')

    errors.value = []

    await $fetch('http://127.0.0.1:8000/api/v1/token/login/', {
        method: 'POST',
        body: {
            username: email.value,
            password: password.value
        }
    })
    .then(data => {
        console.log('response', data.auth_token)

        userStore.setToken(data.auth_token, email.value)

        router.push({path: '/'})
    })
    .catch(error => {
        if (error.response) {
            for (const property in error.response._data) {
                errors.value.push(`${property}: ${error.response._data[property]}`)
            }
            console.log(JSON.stringify(error.response))
        } else if (error.message) {
            errors.value.push('Something went wrong. Please try again')
            
            console.log(JSON.stringify(error))
        }
    })
}</script>


<!-- Here we do the same as with register form -->
<template>
  <div class="py-10 px-6">
    <div class="max-w-sm mx-auto py-10 px-6 bg-gray-100 rounded-xl flex flex-col items-center">
      <h1 class="mb-16 text-2xl">Log in</h1>
      <form v-on:submit.prevent="submitForm" class="flex flex-col justify-center">
        <input v-model="email" type="email" placeholder="Your email address..." class="w-full mb-4 py-2 px-6 rounded-xl">
        <input v-model="password" type="password" placeholder="Your password..." class="w-full mb-4 py-2 px-6 rounded-xl">

          <!-- If there're errors, show new Dev with them -->
        <div 
        v-if="errors.length" 
        class="mb-6 py-4 px-6 bg-rose-400 text-white rounded-xl">
          <p v-for="error in errors" :key="error">
            {{ error }}
          </p>
        </div>

        <button class="py-2 my-8 px-6 bg-gray-400 text-white rounded-xl border-2 border-gray-400 hover:border-gray-500 duration-150">Submit</button>
      </form>
    </div>
  </div>
</template>