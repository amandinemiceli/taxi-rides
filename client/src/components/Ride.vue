<template>
    <div>
        <button class="focus:outline-none"
          v-bind:id="ride.id"
          v-on:click="onRideClick"
        >
            <p>Ride: {{ ride.id }} <span class="uppercase font-bold" v-if="clickCounter > 0">- clicked</span></p>
            <p>Price: {{ ride.price }} EUR</p>
        </button>
    </div>
</template>

<script>
export default {
    name: 'Ride',
    props: ['ride'],
    data() {
        return {
            clickCounter: 0
        }
    },
    methods: {
        onRideClick() {
            alert('display duration + end time');
            this.clickCounter += 1;
        }
    }
};
</script>