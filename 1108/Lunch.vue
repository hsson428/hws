<template>
  <div>
    <h1>Lunch</h1>
    <button @click="pickMenu">pick</button>
    <p>{{ pick }}</p>
    <h3>로또를 뽑아보자</h3>
    <button @click="moveToLotto">Pick Lotto</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'Lunch',
  data: function () {
    return {
      menus: ['짜장면', '김치찌개', '고등어구이'],
      pick: '',
    }
  },
  methods: {
    pickMenu () {
      this.pick = _.sample(this.menus)
    },
    moveToLotto() {
      this.$router.push({ name: 'Lotto'})
    }
  }
}
</script>

<style>

</style>