<script setup>
let email = ref('')
let password1 = ref('')
let password2 = ref('')
let errors = ref([])

// This is how we instantiate the router so we can use to for example: go to another page in function
const router = useRouter()

console.log('email - ', email.value)
// console.log('password1 - ', password1.value)
// console.log('password2 - ', password2.value)

// Aquí se puede ver para que necesitamos function watch !!! Es una función de Vue3,
// que hace la misma función de .subscribe() esta función es de Prueba para verlo nada más
watch([email, password1] , (newValue, oldValue) => {
  // console.log('Email: ' ,email.value)
  // console.log('Password :' , password1.value)
})
// We make it async so it waits the response to be completed
async function submitForm() {
    console.log('submitForm')

    errors.value = []

    await $fetch('http://127.0.0.1:8000/api/v1/users/', {
        method: 'POST',
        body: {
            username: email.value,
            password: password1.value
        }
    })
    .then(response => {
        console.log('response', response)

        router.push({path: '/login'})
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
}
</script>

<template>
  <div class="py-10 px-6">
    <div class="max-w-sm mx-auto py-10 px-6 bg-gray-100 rounded-xl flex flex-col items-center">
      <h1 class="mb-16 text-2xl">Sign up</h1>
      <!--todo Aquí vindeamos algo... -->
      <!-- With v-on we attach an event listener to the element -->
      <form v-on:submit.prevent="submitForm" class="flex flex-col justify-center">
        <input v-model="email" type="email" placeholder="Your email address..." class="w-full mb-4 py-2 px-6 rounded-xl">
        <input v-model="password1" type="password" placeholder="Your password..." class="w-full mb-4 py-2 px-6 rounded-xl">
        <input v-model="password2" type="password" placeholder="Repeat password..." class="w-full mb-4 py-2 px-6 rounded-xl">
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