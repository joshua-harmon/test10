<script setup>
// Declare a variable route with useRoute() to access the id of the routed link
const route = useRoute()
console.log(route)
// With doing request, add route.params.id to add a parameter as id
const {data:job} = await useFetch('http://127.0.0.1:8000/api/v1/jobs/' + route.params.id + '/')
</script>

<template>
  <div class="py-10 px-6 grid md:grid-cols-4 gap-3">
    <div class="md:col-span-3">
      <h1 class="mb-6 text-3xl">{{ job.title }}</h1>
      <p> {{ job.description }}</p>
      <!-- Here is an example of how you can bind a variable inside a DOM element -->
      <a :href="'mailto:' +  job.company_email " class="inline-block mt-6 py-4 px-6 bg-teal-700 text-white rounded-xl hover:scale-105 duration-150">Apply</a>
    </div>

    <div class="md:col-span-1 p-6 bg-gray-100 rounded-xl">

      <h3 class="mb-6 text-2xl"> Company</h3>
      <p class="mb-2"> {{ job.company_name }}</p>
      <p class="mb-2"> {{ job.company_location }}</p>
      <hr class="my-6">

      <h3 class="mb-6 text-2xl">{{ job.position_location }}</h3>
      <p class="mb-2">{{ job.position_salary }}</p>
      <p>Salary</p>
      <hr class="my-6">
      
      <p>Posted {{ job.created_at_formatted }}</p>
    </div>
  </div>
</template>