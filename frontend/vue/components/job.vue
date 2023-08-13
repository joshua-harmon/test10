<script setup>
const props = defineProps({
  my: {
    type: [Boolean]
  },
  job: {
    type: [Object]
  }
})
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
        <nuxt-link v-if="my" to="/browse/1/" class="mx-2 py-4 px-6 bg-gray-200 rounded-xl hover:bg-cyan-500 duration-200">Edit</nuxt-link>
        <nuxt-link v-if="my" to="/browse/1/" class="mx-2 py-4 px-6 bg-gray-200 rounded-xl hover:bg-red-400 duration-200">Delete</nuxt-link>
      </div>
    </div>
</template>