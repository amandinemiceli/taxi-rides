<template>
    <div class="rides m-5">
        <h2 class="text-xl">{{ title }}</h2>
        <div class="grid grid-cols-3 xl:grid-cols-5 place-content-center mt-8"
          v-if="content.length > 0">
            <Ride class="box-content border-2 m-3 p-3"
              v-bind:class="{ 'bg-red-500': ride.distance > 2 }"
              v-for="(ride, index) in content"
              v-bind:key="index"
              v-bind:ride="ride"
            />
        </div>
        <div class="font-bold mt-8 error-message" v-else>{{ error }}</div>
    </div>
</template>

<script>
import Ride from './Ride';
import axios from 'axios';

export default {
    name: 'RideList',
    components: { Ride },
    data() {
        return {
            title: 'Here are the different rides!',
            content: [],
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
                    if (this.content.length == 0) {
                        this.error = 'There is no ride to display.';
                    }
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