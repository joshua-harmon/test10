<script setup>
const props = defineProps({
  my: {
    type: [Boolean]
  }
})
</script>

<template>
    <div class="p-6 flex items-center justify-between bg-gray-100 rounded-xl">
      <div>
        <h3 class="mb-2 text-xl font-semibold">Job Position</h3>
        <p class="text-gray-600">The Company Name</p>
      </div>
      <div>
        <p class="mb-2">Worldwide</p>
        <p>$90-120k</p>
      </div>
      <div>
        <p>Posted December 1, 2023</p>
      </div>
      <div>
        <nuxt-link to="/browse/1/" class="mx-2 py-4 px-6 bg-gray-200 rounded-xl hover:bg-gray-300 duration-200">Details</nuxt-link>
        <nuxt-link v-if="my" to="/browse/1/" class="mx-2 py-4 px-6 bg-gray-200 rounded-xl hover:bg-cyan-500 duration-200">Edit</nuxt-link>
        <nuxt-link v-if="my" to="/browse/1/" class="mx-2 py-4 px-6 bg-gray-200 rounded-xl hover:bg-red-400 duration-200">Delete</nuxt-link>
      </div>
    </div>
</template>