<template>
  <div>
    <h1>Lotto</h1>
    <button @click="getLuckyNumbers">Get Lucky Numbers</button>
    <p v-if="pick.length">{{ pick }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'Lotto',
  data: function () {
    return {
      numbers: _.range(1, 46),
      pick: [],
    }
  },
  methods: {
    getLuckyNumbers () {
      this.pick = _.sortBy(_.sampleSize(this.numbers, 6))
    },
  }
}
</script>

<style>

</style>