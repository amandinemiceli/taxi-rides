<template>
    <div>
        <button class="focus:outline-none"
          v-bind:id="ride.id"
          v-on:click="onRideClick"
          >
            <p>Ride: {{ ride.id }} <span class="uppercase font-bold" v-if="clickCounter > 0">- clicked</span></p>
            <p>Price: {{ ride.price }} EUR</p>
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
        onRideClick() {
            this.message = 'display duration + end time';
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