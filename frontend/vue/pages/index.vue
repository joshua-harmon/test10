<script setup>

// This is how we retrieve the data from backend and save it into a variable
const { data: jobs } = await useFetch('http://127.0.0.1:8000/api/v1/jobs/newest/')
</script>

<template>
	<div>
		<div class="py-20 px-6 bg-teal-700 text-center">
			<h1 class="mb-12 text-5xl text-white">Find a job anywhere</h1>
			<nuxt-link to="/browse" class="inline-block py-4 px-8 bg-teal-900 text-white rounded-xl hover:scale-125 duration-200" >Browse</nuxt-link>
		</div>
		<div class="py-10 px-6">
			<h2 class="mb-8 text-3xl text-center">Newest Jobs</h2>
			<!-- We create a folder with components and then show use this component -->
			<!-- Div element with jobs -->
			<!-- Will take 3 spans when from medium screen -->
			<div class="md:col-span-3 bg-gray-100 rounded-xl">
				<div class="space-y-8">
					<!-- We declare v-for loop and v-bind so Vue has a unique key for iteration -->
          <Job v-for="job in jobs" :key="job.id" :job="job" :my="true" />
				</div>
			</div>
		</div>
	</div>
</template>
