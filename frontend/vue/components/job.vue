<script setup>
import { useUserStore } from '@/stores/user'


// This is how you can emit events from child to a parent
const emit = defineEmits(['deleteJob'])
const userStore = useUserStore()

const props = defineProps({
  my: {
    type: [Boolean]
  },
  job: {
    type: [Object]
  }
})

async function deleteJob(id) {
  await $fetch('http://127.0.0.1:8000/api/v1/jobs/' + id + '/delete/', {
    method: 'DELETE',
    // We define headers and pass token stored in localStorage of the user
    headers: {
        'Authorization': 'token ' + userStore.user.token,
        'Content-Type': 'application/json'
    }
  }).then(response => {
    console.log('response', response)
    // After receiving a succesful response, we emit an event to a parent 
    // you can pass as many parameters as you want
    emit('deleteJob', id)
  }).catch(error => {
    console.log('error: ', error)
  })
}
</script>

<template>
    <div class="p-6 flex items-center justify-between bg-gray-100 rounded-xl">
      <div>
        <h3 class="mb-2 text-xl font-semibold">{{ job.title }}</h3>
        <p class="text-gray-600">{{ job.company_name }}</p>
      </div>
      <div>
        <p class="mb-2"> {{ job.position_location }}</p>
        <p>{{ job.position_salary }}</p>
      </div>
      <div>
        <p>{{ job.created_at_formatted }}</p>
      </div>
      <div>
        <!-- This is how to create a dynamic url based on job.id -->
        <nuxt-link :to="'/browse/' + job.id" class="mx-2 py-4 px-6 bg-gray-200 rounded-xl hover:bg-gray-300 duration-200">Details</nuxt-link>
        <nuxt-link v-if="my" :to="'/editjob/' + job.id" class="mx-2 py-4 px-6 bg-gray-200 rounded-xl hover:bg-cyan-500 duration-200">Edit</nuxt-link>
        <a @click="deleteJob(job.id)" v-if="my" class="cursor-pointer mx-2 py-4 px-6 bg-gray-200 rounded-xl hover:bg-red-400 duration-200">Delete</a>
      </div>
    </div>
</template>