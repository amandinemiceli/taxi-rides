<template>
    <div class="rides m-5">
        <h3 class="text-lg">{{ title }}</h3>
        <div class="grid grid-cols-3 xl:grid-cols-5 place-content-center mt-8"
          v-if="content.length > 0">
            <div class="box-content border-2 m-3 p-3"
              v-for="(ride, index) in content"
              v-bind:key="index"
              v-bind:id="ride.id"
              v-bind:class="{ 'bg-red-500': ride.distance > 2 }"
            >
                <p>Ride ID: {{ ride.id }}</p>
                <p>Distance: {{ ride.distance }}</p>
                <p>Start time: {{ ride.startTime }}</p>
                <p>Duration: {{ ride.duration }}</p>
            </div>
        </div>
        <div class="error-message" v-else>{{ error }}</div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'RideList',
    components: {},
    data() {
        return {
            title: 'Here are the different rides available!',
            content: '',
            error: ''
        };
    },
    methods: {
        getRideDetails() {
            const API_PATH = 'http://localhost:5000';
            axios.get(API_PATH + '/rides')
            .then((response) => {
                if (response.data.status_code == 200) {
                    this.content = response.data.data;
                } else {
                    this.error = response.data.message;
                }
            })
            .catch((error) => {
                console.error(error);
            });
        },
    },
    created() {
        this.getRideDetails();
    },
};
</script>