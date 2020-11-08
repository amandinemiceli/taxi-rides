<template>
    <div v-show="popupOpened" class="bg-blue-200 border-2 border-blue-300 text-blue-600 px-4 py-3 mt-3" role="alert">
      <p class="italic">{{ message }}</p>
      <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 mt-2 rounded"
        v-on:click="onCloseClick">OK</button>
    </div>
</template>

<script>
export default {
    name: 'Alert',
    props: ['message', 'isDisplayed'],
    data() {
        return {
            popupOpened: this.isDisplayed,
        }
    },
    methods: {
        onCloseClick() {
            if (this.popupOpened == true) {
                this.popupOpened = false;
            }
            this.$emit('onButtonClick', this.popupOpened);
        }
    }
};
</script>