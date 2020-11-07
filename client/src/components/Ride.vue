<template>
    <div>
        <div v-bind:id="ride.id">
            <p>Ride: {{ ride.id }}</p>
            <p>Price: {{ ride.price }} EUR</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Ride',
    props: ['ride']
};
</script>