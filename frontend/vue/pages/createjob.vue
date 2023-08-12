<template>
  <div class="py-10 px-6">
    <h1 class="mb-6 text-2xl">Create a job</h1>
    <form  class="space-y-4">
      <div class="flex flex-col">
        <label>Category</label>
        <select name="" id="" class="w-full max-w-xs mt-2 py-2 px-4 rounded-xl bg-gray-100">
          <option value="">Select category</option>
          <option value="cat1">Category 1</option>
          <option value="cat2">Category 1</option>
        </select>
      </div>

      <div>
        <label>Title</label>
        <input type="text" class="w-full mt-2 py-2 px-4 rounded-xl bg-gray-100">
      </div>

      <div>
        <label>Description</label>
        <textarea type="text" class="w-full mt-2 py-2 px-4 rounded-xl bg-gray-100"></textarea>
      </div>

      <div>
        <label>Salary</label>
        <input type="text" class="w-full mt-2 py-2 px-4 rounded-xl bg-gray-100">
      </div>

      <div>
        <label>Location</label>
        <input type="text" class="w-full mt-2 py-2 px-4 rounded-xl bg-gray-100">
      </div>

      <div>
        <label>Company name</label>
        <input type="text" class="w-full mt-2 py-2 px-4 rounded-xl bg-gray-100">
      </div>

      <div>
        <label>Company e-mail</label>
        <input type="text" class="w-full mt-2 py-2 px-4 rounded-xl bg-gray-100">
      </div>

      <button class="py-2 my-8 px-6 bg-gray-400 text-white rounded-xl border-2 border-gray-400 hover:border-gray-500 duration-150">Submit</button>
      
    </form>
  </div>
</template>