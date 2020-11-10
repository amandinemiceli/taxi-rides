<template>
    <div>
        <button class="focus:outline-none"
          v-bind:id="ride.id"
          v-on:click="onRideClick(ride.id)"
          >
            <p>Ride: {{ ride.id }} <span class="uppercase font-bold" v-if="clickCounter > 0">- clicked</span></p>
            <p>Price: {{ ride.cost }} EUR</p>
        </button>
        <Alert
          v-show="isDisplayed"
          v-bind:isDisplayed="isDisplayed"
          v-bind:message="message"
          v-on:onButtonClick="onCloseClick"
          />
    </div>
</template>

<script>
import Alert from './Alert';
import axios from 'axios';

export default {
    name: 'Ride',
    props: ['ride'],
    components: { Alert },
    data() {
        return {
            clickCounter: 0,
            isDisplayed: false,
            message: ''
        }
    },
    methods: {
        onRideClick(rideId) {
            const API_PATH = 'http://localhost:5000';
            axios.get(API_PATH + '/rides/' + rideId)
            .then((response) => {
                if (response.data.status_code == 200) {
                    let data = response.data.data;
                    this.message = data.readableDuration + ' - ' + data.endTime;
                } else {
                    this.error = response.data.message;
                }
            })
            .catch((error) => {
                console.error(error);
            });

            this.clickCounter += 1;
            if (this.isDisplayed == false) {
                this.isDisplayed = true;
            }
        },
        onCloseClick(value) {
            this.isDisplayed = value;
        }
    }
};
</script>