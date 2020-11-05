<template>
    <div class="rides">
        <h3>{{ title }}</h3>
        <div v-if="content.length > 0">
            <div v-for="(ride, index) in content" v-bind:key="index" v-bind:id="ride.id">
                <p>ID: {{ ride.id }}</p>
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
        getMessage() {
            const path = 'http://localhost:5000/rides';
            axios.get(path)
            .then((response) => {
                if (response.data.code == 200) {
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
        this.getMessage();
    },
};
</script>