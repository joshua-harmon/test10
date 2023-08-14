<script setup>
import { onMounted } from 'vue';
import { useUserStore } from '@/stores/user';

// Asign userStore variable so we can access to the token of the store
const userStore = useUserStore()
const router = useRouter()

// We make an API call to retrieve categories
let {data:categories} = await useFetch('http://127.0.0.1:8000/api/v1/jobs/category/')

// Asign reactive variables for a form 
let category = ref('')
let title = ref('')
let description = ref('')
let position_salary = ref('')
let position_location = ref('')
let company_name = ref('')
let company_location = ref('')
let company_email = ref('')

let errors = ref([])

onMounted(() => {
  if (!userStore.user.isAuthenticated) {
    router.push('/login')
  }
})


async function submitForm() {
  console.log('submitForm')

  errors.value = []

  // Validations
  if (category.value == '') { errors.value.push('You must select a category')}
  if (title.value == '') { errors.value.push('The title field is missing')}
  if (description.value == '') { errors.value.push('The description field is missing')}
  if (position_salary.value == '') { errors.value.push('The position salary field is missing')}
  if (position_location.value == '') { errors.value.push('The position location field is missing')}
  if (company_name.value == '') { errors.value.push('The company name field is missing')}
  if (company_location.value == '') { errors.value.push('The company location field is missing')}
  if (company_email.value == '') { errors.value.push('The company email field is missing')}


  if (errors.value.length == 0) {
        await $fetch('http://127.0.0.1:8000/api/v1/jobs/create/', {
            method: 'POST',
            // We define headers and pass token stored in localStorage of the user
            headers: {
                'Authorization': 'token ' + userStore.user.token,
                'Content-Type': 'application/json'
            },
            body: {
                category: category.value,
                title: title.value,
                description: description.value,
                position_salary: position_salary.value,
                position_location: position_location.value,
                company_name: company_name.value,
                company_location: company_location.value,
                company_email: company_email.value
            }
        })
        .then(response => {
            console.log('response', response)

            router.push({path: '/myjobs'})
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
}
</script>

<template>
  <div class="py-10 px-6">
    <h1 class="mb-6 text-2xl">Create a job</h1>

    <form  @submit.prevent="submitForm" class="space-y-4">
      <div class="flex flex-col">
        <label>Category</label>
        <select v-model="category" name="" id="" class="w-full max-w-xs mt-2 py-2 px-4 rounded-xl bg-gray-100">
          <option value="">Select category</option>
          <option 
          :key="category.id" 
          v-for="category in categories" 
          :value="category.id">{{ category.title }}</option>
        </select>
      </div>

      <div>
        <label>Title</label>
        <input v-model="title" type="text" class="w-full mt-2 py-2 px-4 rounded-xl bg-gray-100">
      </div>

      <div>
        <label>Description</label>
        <textarea v-model="description" type="text" class="w-full mt-2 py-2 px-4 rounded-xl bg-gray-100"></textarea>
      </div>

      <div>
        <label>Salary</label>
        <input v-model="position_salary" type="text" class="w-full mt-2 py-2 px-4 rounded-xl bg-gray-100">
      </div>

      <div>
        <label>Location</label>
        <input v-model="position_location" type="text" class="w-full mt-2 py-2 px-4 rounded-xl bg-gray-100">
      </div>

      <div>
        <label>Company name</label>
        <input v-model="company_name" type="text" class="w-full mt-2 py-2 px-4 rounded-xl bg-gray-100">
      </div>

      <div>
        <label>Company Location</label>
        <input v-model="company_location" type="text" class="w-full mt-2 py-2 px-4 rounded-xl bg-gray-100">
      </div>

      <div>
        <label>Company e-mail</label>
        <input v-model="company_email" type="text" class="w-full mt-2 py-2 px-4 rounded-xl bg-gray-100">
      </div>

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
</template>