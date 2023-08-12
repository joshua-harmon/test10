<script setup>
import { useUserStore } from '@/stores/user'

const userStore = useUserStore()
</script>

<template>
  <div>
    <nav class="p-6 flex items-center justify-between bg-teal-800">
      <NuxtLink to="/" class="text-xl text-white">Portal de Empleo</NuxtLink>
      <div class="flex items-center space-x-4">
        <!-- This creates <a></a> link with nuxt is like a button-->
        <NuxtLink to="/" class="text-white py-4 px-6 hover:bg-gray-800 border-2 border-teal-700 rounded-xl duration-200">Home</NuxtLink>
        <nuxt-link to="/browse" class="text-white py-4 px-6 hover:bg-gray-800 border-2 border-teal-700 rounded-xl duration-200">Browse</nuxt-link>
      </div>
    </nav>
    <!-- In slot we will be passing different components -->
    <slot />
    <footer class="p-6 flex flex-wrap items-center justify-between bg-gray-800">
      <p class="text-gray-300">Copyrigth(c) 2023 - Nikita Prueba</p>
      <div class="flex mt-6 md:mt-0 items-center space-x-4">

        <template v-if="userStore.user.isAuthenticated">
        <nuxt-link to="/myjobs" class="py-4 px-6 pg-teal-800 border-2 border-teal-700 hover:bg-teal-700 text-white rounded-xl duration-200">My jobs</nuxt-link>
        <nuxt-link to="/createjobs" class="py-4 px-6 pg-teal-800 border-2 border-teal-700 hover:bg-teal-700 text-white rounded-xl duration-200">Create job</nuxt-link>
        <nuxt-link to="/logout" class="py-4 px-6 pg-teal-800 border-2 border-red-700 hover:bg-red-500 text-white rounded-xl duration-200">Log out</nuxt-link>
        </template>

        <template v-else>
        <nuxt-link to="/login" class="py-4 px-6 pg-teal-800 border-2 border-teal-700 hover:bg-teal-700 text-white rounded-xl duration-200">Login</nuxt-link>
        <nuxt-link to="/signup" class="py-4 px-6 pg-teal-800 border-2 border-teal-700 hover:bg-teal-700 text-white rounded-xl duration-200">Sign Up</nuxt-link>
      </template>
      
      </div>
    </footer>
  </div>
</template>