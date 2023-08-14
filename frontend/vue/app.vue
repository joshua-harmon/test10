<script setup>
import { onMounted } from 'vue';
import { useUserStore } from '@/stores/user';

const userStore = useUserStore()

onMounted(() => {
  userStore.initStore()
})

useSeoMeta({
    title: 'Portal de Empleo',
    ogTitle: 'Portal de Empleo',
    description: 'The description'
})
</script>

<template>
  <div>
    <!-- Adds layout for every page -->
    <NuxtLayout>
      <!-- Adds a "route" for the rest of the pages -->
      <NuxtPage/>
    </NuxtLayout>
  </div>
</template>
