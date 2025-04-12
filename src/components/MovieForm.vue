<template>
  <form id="movieForm" @submit.prevent="saveMovie" class="p-4">
    <!-- Success message -->
    <div v-if="message" class="alert alert-success mt-3">{{ message }}</div>

    <!-- Error messages -->
    <div v-if="errors.length" class="alert alert-danger mt-3">
      <ul>
        <li v-for="(error, index) in errors" :key="index">{{ error }}</li>
      </ul>
    </div>
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input v-model="title" type="text" name="title" class="form-control" />
    </div>

    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea v-model="description" name="description" class="form-control"></textarea>
    </div>

    <div class="form-group mb-3">
      <label for="poster" class="form-label">Photo Upload</label>
      <input @change="handleFileUpload" type="file" name="poster" class="form-control" />
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>

  </form>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const title = ref('');
const description = ref('');
const poster = ref(null);
const csrf_token = ref('');
const message = ref('');
const errors = ref([]);

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
      csrf_token.value = data.csrf_token;
    });
}

onMounted(() => {
  getCsrfToken();
});

function handleFileUpload(event) {
  poster.value = event.target.files[0];
}

function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

function saveMovie() {
  errors.value = [];
  message.value = '';

  let form_data = new FormData();
  form_data.append('title', title.value);
  form_data.append('description', description.value);
  form_data.append('poster', poster.value);

  fetch('/api/v1/movies', {
  method: 'POST',
  body: form_data,
  headers: {
    'X-CSRFToken': csrf_token.value,
  },
})
  .then(async (response) => {
    const data = await response.json();

    if (response.ok) {
      message.value = data.message;
      title.value = '';
      description.value = '';
      poster.value = null;
      document.getElementById('movieForm').reset(); // reset file input
      errors.value = []; // clear old errors
    } else {
      if (Array.isArray(data.errors)) {
        errors.value = data.errors;
      } else if (typeof data.errors === 'object') {
        errors.value = Object.entries(data.errors).flatMap(
            ([field, msgs]) => msgs.map(msg => `Error in the ${capitalize(field)} field - ${msg}`)
        );
      } else {
        errors.value = ['Something went wrong but no error messages were returned.'];
      }
    }
  })
  .catch((error) => {
    console.error('Unexpected error:', error);
    errors.value = ['An unexpected error occurred.'];
  });

}

</script>

<style scoped>
</style>
