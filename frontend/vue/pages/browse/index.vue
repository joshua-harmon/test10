<script setup>
// Filter by search name 
let queryRef = ref('')
let query = ref('')

function performSearch() {
  queryRef.value = query.value
}

// Filter by category
let selectedCategoriesRef = ref('')
let selectedCategories = []
// Make a request and pass the parameters in 'query'
const {data:jobs} = await useFetch('http://127.0.0.1:8000/api/v1/jobs/browse/', {
  query: {
    title: queryRef,
    categories: selectedCategoriesRef
  }
})
const {data:categories} = await useFetch('http://127.0.0.1:8000/api/v1/jobs/category/')


function toggleCategory(id) {
  const index = selectedCategories.indexOf(id)

  if (index === -1) {
    selectedCategories.push(id)
  } else {
    selectedCategories.splice(index, 1)
  }
  selectedCategoriesRef.value = selectedCategories.join(',')
}
</script>

<template>
	<!-- We define a grid only from medium to be 4 columns -->
	<div class="grid md:grid-cols-4 gap-3 py-10 px-6">
		<div class="md:col-span-1 px-6 py-6 bg-teal-700 rounded-xl">
      <!-- Search -->
			<div class="flex space-x-4">
        <!-- Este query no debe ser ref (reactivo) es solamente para una prueba -->
        <h1>{{ query }}</h1>
        <!-- Search Input -->
				<input
					type="search"
					placeholder="Find a job..."
					class="w-full px-6 py-2 rounded-xl"
          v-model="query"
				/>
				<button 
        class="px-4 py-2 bg-teal-900 text-white rounded-xl"
        v-on:click="performSearch"
        >
          <!-- Search Icon -->
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
          </svg>
				</button>
			</div>
      <hr class="my-6 opacity-30">
      <h3 class="mt-6 text-xl text-white">Categories</h3>
      <div class="mt-6 space-y-4">
        <!-- On click of this DOM element it will make some action based on a function -->
        <!-- We also change a color if it selected, check binded class based on if statement -->
        <p 
        @click="toggleCategory(category.id)" 
        v-for="category in categories" :key="category.id" 
        :class="{'bg-white bg-opacity-30': selectedCategoriesRef.includes(category.id)}"
        class="py-2 cursor-pointer px-6 hover:bg-white hover:bg-opacity-30 text-white rounded-xl border-2 duration-100 border-white">
        {{ category.title }}
      </p>
      </div>
		</div>
    <!-- Div element with jobs -->
		<!-- Will take 3 spans when from medium screen -->
		<div class="md:col-span-3 bg-gray-100 rounded-xl">
      <div class="space-y-8">
    <!-- Here we use again the Jobs components -->
    <Job v-for="job in jobs" :key="job.id" :job="job" />
    </div>
    </div>

	</div>
</template>
